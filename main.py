"""
X to LinkedIn & Telegram Cross-Poster Bot (REVERSE)
Monitors your X/Twitter account and auto-posts new tweets to LinkedIn and Telegram
Uses FREE X API (read-only)
"""

import os
import logging
import time
import requests
import tweepy
from datetime import datetime
from dotenv import load_dotenv
from telegram import Bot
import asyncio

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


class ReverseBot:
    def __init__(self):
        # X/Twitter credentials (FREE tier - read-only)
        self.twitter_bearer_token = os.getenv('TWITTER_BEARER_TOKEN')
        self.twitter_username = os.getenv('TWITTER_USERNAME')  # Your X username (without @)
        
        # LinkedIn credentials
        self.linkedin_access_token = os.getenv('LINKEDIN_ACCESS_TOKEN')
        self.linkedin_person_id = os.getenv('LINKEDIN_PERSON_ID')
        
        # Telegram credentials
        self.telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
        self.telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID')  # Your chat ID or channel
        
        # Tracking
        self.last_tweet_id = None
        self.check_interval = int(os.getenv('CHECK_INTERVAL', '300'))  # Default: 5 minutes
        
        # Initialize clients
        self.init_twitter()
        self.init_telegram()
    
    def init_twitter(self):
        """Initialize Twitter/X API client (FREE - read-only)"""
        try:
            self.twitter_client = tweepy.Client(bearer_token=self.twitter_bearer_token)
            logger.info("✅ Twitter client initialized successfully (READ-ONLY)")
        except Exception as e:
            logger.error(f"❌ Failed to initialize Twitter client: {e}")
            self.twitter_client = None
    
    def init_telegram(self):
        """Initialize Telegram bot"""
        try:
            self.telegram_bot = Bot(token=self.telegram_bot_token)
            logger.info("✅ Telegram bot initialized successfully")
        except Exception as e:
            logger.error(f"❌ Failed to initialize Telegram bot: {e}")
            self.telegram_bot = None
    
    def get_twitter_user_id(self):
        """Get user ID from username"""
        try:
            user = self.twitter_client.get_user(username=self.twitter_username)
            if user.data:
                logger.info(f"✅ Found Twitter user: @{self.twitter_username} (ID: {user.data.id})")
                return user.data.id
            return None
        except Exception as e:
            logger.error(f"❌ Error getting user ID: {e}")
            return None
    
    def get_latest_tweets(self, user_id, max_results=5):
        """Get latest tweets from user (FREE API)"""
        try:
            tweets = self.twitter_client.get_users_tweets(
                id=user_id,
                max_results=max_results,
                exclude=['retweets', 'replies'],  # Only original tweets
                tweet_fields=['created_at', 'text']
            )
            
            if tweets.data:
                return tweets.data
            return []
        
        except Exception as e:
            logger.error(f"❌ Error fetching tweets: {e}")
            return []
    
    def post_to_linkedin(self, text, tweet_url):
        """Post to LinkedIn"""
        if not self.linkedin_access_token or not self.linkedin_person_id:
            return False, "LinkedIn credentials not configured"
        
        try:
            url = "https://api.linkedin.com/v2/ugcPosts"
            
            headers = {
                "Authorization": f"Bearer {self.linkedin_access_token}",
                "Content-Type": "application/json",
                "X-Restli-Protocol-Version": "2.0.0"
            }
            
            # Add tweet URL to the post
            full_text = f"{text}\n\nOriginally posted on X: {tweet_url}"
            
            post_data = {
                "author": f"urn:li:person:{self.linkedin_person_id}",
                "lifecycleState": "PUBLISHED",
                "specificContent": {
                    "com.linkedin.ugc.ShareContent": {
                        "shareCommentary": {
                            "text": full_text
                        },
                        "shareMediaCategory": "NONE"
                    }
                },
                "visibility": {
                    "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
                }
            }
            
            response = requests.post(url, headers=headers, json=post_data)
            
            if response.status_code == 201:
                logger.info(f"✅ Posted to LinkedIn successfully!")
                return True, "Posted to LinkedIn successfully!"
            else:
                logger.error(f"❌ LinkedIn error: {response.status_code} - {response.text}")
                return False, f"LinkedIn error: {response.status_code}"
        
        except Exception as e:
            logger.error(f"❌ LinkedIn posting error: {e}")
            return False, f"LinkedIn error: {str(e)}"
    
    async def post_to_telegram(self, text, tweet_url):
        """Post to Telegram channel/chat"""
        if not self.telegram_bot or not self.telegram_chat_id:
            return False, "Telegram not configured"
        
        try:
            # Format message for Telegram
            message = f"🐦 New post from X:\n\n{text}\n\n🔗 {tweet_url}"
            
            await self.telegram_bot.send_message(
                chat_id=self.telegram_chat_id,
                text=message
            )
            
            logger.info(f"✅ Posted to Telegram successfully!")
            return True, "Posted to Telegram successfully!"
        
        except Exception as e:
            logger.error(f"❌ Telegram posting error: {e}")
            return False, f"Telegram error: {str(e)}"
    
    async def process_new_tweet(self, tweet):
        """Process and cross-post a new tweet"""
        tweet_id = tweet.id
        tweet_text = tweet.text
        tweet_url = f"https://twitter.com/{self.twitter_username}/status/{tweet_id}"
        
        logger.info(f"📝 New tweet detected: {tweet_text[:50]}...")
        
        # Post to LinkedIn
        linkedin_success, linkedin_msg = self.post_to_linkedin(tweet_text, tweet_url)
        
        # Post to Telegram
        telegram_success, telegram_msg = await self.post_to_telegram(tweet_text, tweet_url)
        
        # Log results
        logger.info(f"📊 Cross-posting results:")
        logger.info(f"  LinkedIn: {'✅' if linkedin_success else '❌'} {linkedin_msg}")
        logger.info(f"  Telegram: {'✅' if telegram_success else '❌'} {telegram_msg}")
        
        return linkedin_success or telegram_success
    
    async def monitor_and_crosspost(self):
        """Main loop - monitor X and cross-post"""
        logger.info("🚀 Starting X monitoring bot...")
        
        # Get user ID
        user_id = self.get_twitter_user_id()
        if not user_id:
            logger.error("❌ Could not get Twitter user ID. Check username!")
            return
        
        logger.info(f"👀 Monitoring @{self.twitter_username} for new posts...")
        logger.info(f"⏰ Checking every {self.check_interval} seconds")
        
        while True:
            try:
                # Get latest tweets
                tweets = self.get_latest_tweets(user_id)
                
                if tweets:
                    # Get the most recent tweet
                    latest_tweet = tweets[0]
                    
                    # Check if this is a new tweet
                    if self.last_tweet_id is None:
                        # First run - just store the ID, don't post
                        self.last_tweet_id = latest_tweet.id
                        logger.info(f"📌 Initial tweet ID stored: {self.last_tweet_id}")
                        logger.info(f"✅ Bot is now monitoring. Post something on X to test!")
                    
                    elif latest_tweet.id != self.last_tweet_id:
                        # New tweet detected!
                        logger.info(f"🆕 NEW TWEET DETECTED!")
                        await self.process_new_tweet(latest_tweet)
                        self.last_tweet_id = latest_tweet.id
                    
                    else:
                        # No new tweets
                        logger.info(f"💤 No new tweets. Last check: {datetime.now().strftime('%H:%M:%S')}")
                
                # Wait before next check
                await asyncio.sleep(self.check_interval)
            
            except Exception as e:
                logger.error(f"❌ Error in monitoring loop: {e}")
                await asyncio.sleep(60)  # Wait 1 minute on error


def main():
    """Start the reverse bot"""
    bot = ReverseBot()
    
    # Check configuration
    if not bot.twitter_bearer_token:
        logger.error("❌ TWITTER_BEARER_TOKEN not configured!")
        return
    
    if not bot.twitter_username:
        logger.error("❌ TWITTER_USERNAME not configured!")
        return
    
    if not bot.telegram_bot_token:
        logger.error("❌ TELEGRAM_BOT_TOKEN not configured!")
        return
    
    if not bot.telegram_chat_id:
        logger.error("❌ TELEGRAM_CHAT_ID not configured!")
        return
    
    # Start monitoring
    asyncio.run(bot.monitor_and_crosspost())


if __name__ == '__main__':
    main()
