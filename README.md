# 🔄 X to LinkedIn & Telegram Auto-Poster (REVERSE BOT)

**Post on X → Auto-posts to LinkedIn & Telegram!**

This bot monitors your X/Twitter account and automatically cross-posts your tweets to LinkedIn and Telegram. **No expensive X API needed!** Uses FREE read-only X API.

---

## 💡 How It Works

```
1. You post on X/Twitter manually (like you normally do)
   ↓
2. Bot checks your X account every 5 minutes
   ↓
3. Detects new tweet
   ↓
4. Auto-posts to LinkedIn ✅
   ↓
5. Auto-sends to your Telegram channel/chat ✅
```

**💰 Cost: $0/month** (uses FREE X API read-only access)

---

## ✨ Features

- ✅ **FREE X API** - Read-only (no $100/month cost!)
- ✅ **Auto-posts to LinkedIn** - Full integration
- ✅ **Sends to Telegram** - Your channel or personal chat
- ✅ **Excludes retweets/replies** - Only your original posts
- ✅ **Configurable check interval** - Default: 5 minutes
- ✅ **Runs 24/7 on cloud** - No PC needed

---

## 📋 Prerequisites

- X/Twitter account
- LinkedIn account
- Telegram account
- GitHub account
- Free hosting (Railway recommended)

---

## 🚀 Quick Start

### Step 1: Get Your API Credentials

You need **4 things**:

1. ✅ **X/Twitter Bearer Token** (FREE - read-only)
2. ✅ **LinkedIn Access Token**
3. ✅ **Telegram Bot Token**
4. ✅ **Telegram Chat ID**

Follow the [Detailed Setup Guide](#detailed-setup-guide) below.

### Step 2: Configure

```bash
cp .env.example .env
# Edit .env with your credentials
```

### Step 3: Deploy to Railway

1. Push to GitHub
2. Connect to Railway
3. Add environment variables
4. Done!

---

## 🔧 Detailed Setup Guide

### 1️⃣ Get X/Twitter Bearer Token (FREE)

**This is the FREE tier - read-only access!**

1. Go to [Twitter Developer Portal](https://developer.twitter.com/en/portal/dashboard)
2. **Sign up for FREE tier** (NOT the paid tier)
3. Create a new **Project** and **App**
4. In your app, go to **"Keys and tokens"**
5. Under **"Bearer Token"**, click **"Generate"**
6. **Copy the Bearer Token** - you'll need this!

**Important Notes:**
- ✅ FREE tier is perfect for this bot (read-only)
- ✅ You do NOT need the $100/month paid tier
- ✅ No credit card required for read access

**Add to `.env`:**
```
TWITTER_BEARER_TOKEN=AAAAAAAAAAAAA...your_bearer_token
TWITTER_USERNAME=your_twitter_handle_without_@
```

**Example:**
If your X account is `@john_doe`, use:
```
TWITTER_USERNAME=john_doe
```

---

### 2️⃣ Get LinkedIn Access Token

**Same as before - follow these steps:**

1. Go to [LinkedIn Developers](https://www.linkedin.com/developers/apps)
2. Click **"Create app"**
3. Fill in required info and create app
4. Go to **"Auth"** tab
5. Request **"w_member_social"** permission
6. Get your access token via OAuth 2.0

**Get Person ID:**
```bash
curl -H "Authorization: Bearer YOUR_ACCESS_TOKEN" https://api.linkedin.com/v2/me
```

**Add to `.env`:**
```
LINKEDIN_ACCESS_TOKEN=your_access_token
LINKEDIN_PERSON_ID=your_person_id
```

**Detailed LinkedIn guide:** See original bot README or LinkedIn OAuth documentation

---

### 3️⃣ Get Telegram Bot Token

1. Open Telegram → Search **@BotFather**
2. Send: `/newbot`
3. Follow prompts to create bot
4. **Copy the token** you receive

**Add to `.env`:**
```
TELEGRAM_BOT_TOKEN=123456789:ABCdefGHI...
```

---

### 4️⃣ Get Telegram Chat ID

**You need to tell the bot WHERE to send messages.**

#### Option A: Send to Yourself (Private Chat)

1. Open Telegram → Search **@userinfobot**
2. Start the bot
3. It will show your **Chat ID** (looks like: `123456789`)
4. Copy this number

#### Option B: Send to a Channel

1. Create a Telegram channel
2. Add your bot as an administrator
3. Post a message in the channel
4. Go to: `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
5. Look for `"chat":{"id":-1001234567890}`
6. Copy the chat ID (including the minus sign!)

#### Option C: Send to a Group

1. Create a Telegram group
2. Add your bot to the group
3. Make the bot an admin
4. Use **@RawDataBot** in the group to get the Chat ID

**Add to `.env`:**
```
TELEGRAM_CHAT_ID=123456789
# OR for channel/group:
TELEGRAM_CHAT_ID=-1001234567890
```

---

### 5️⃣ Configure Check Interval (Optional)

Set how often the bot checks for new tweets (in seconds):

```
CHECK_INTERVAL=300  # 5 minutes (default)
# CHECK_INTERVAL=180  # 3 minutes
# CHECK_INTERVAL=600  # 10 minutes
```

**Recommendation:** 5 minutes is good. Don't go below 2 minutes to avoid rate limits.

---

## 🌐 Deployment to Railway (FREE)

### Step 1: Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/x-reverse-bot.git
git push -u origin main
```

### Step 2: Deploy to Railway

1. Go to [Railway.app](https://railway.app/)
2. Sign up with GitHub
3. Click **"New Project"** → **"Deploy from GitHub repo"**
4. Select your repository
5. Railway auto-detects Python and deploys

### Step 3: Add Environment Variables

1. In Railway project, click **"Variables"** tab
2. Click **"Raw Editor"**
3. Paste your `.env` contents:

```
TWITTER_BEARER_TOKEN=your_bearer_token
TWITTER_USERNAME=your_username
LINKEDIN_ACCESS_TOKEN=your_linkedin_token
LINKEDIN_PERSON_ID=your_person_id
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
CHECK_INTERVAL=300
```

4. Click **"Update Variables"**
5. Bot restarts automatically!

### Step 4: Check Logs

1. In Railway, click **"Deployments"**
2. Click latest deployment
3. View logs to see:

```
✅ Twitter client initialized successfully (READ-ONLY)
✅ Telegram bot initialized successfully
✅ Found Twitter user: @your_username (ID: 1234567890)
👀 Monitoring @your_username for new posts...
⏰ Checking every 300 seconds
📌 Initial tweet ID stored: 1752...
✅ Bot is now monitoring. Post something on X to test!
```

---

## 🎯 Testing the Bot

### Step 1: Verify It's Running

Check Railway logs for:
```
✅ Bot is now monitoring. Post something on X to test!
```

### Step 2: Post on X

1. Go to X/Twitter
2. Post a new tweet manually: **"Testing my cross-post bot! 🚀"**

### Step 3: Wait 5 Minutes

The bot checks every 5 minutes (or whatever you set `CHECK_INTERVAL` to)

### Step 4: Check Results

**In Railway logs, you should see:**
```
🆕 NEW TWEET DETECTED!
📝 New tweet detected: Testing my cross-post bot! 🚀...
✅ Posted to LinkedIn successfully!
✅ Posted to Telegram successfully!
```

**Check LinkedIn:**
- Your post should appear with the tweet text
- Includes link to original X post

**Check Telegram:**
- Message appears in your chat/channel
- Format: "🐦 New post from X: [your tweet] 🔗 [link]"

---

## 📊 How It Works (Technical)

1. **Bot starts** → Gets your X user ID from username
2. **Every 5 minutes** → Fetches your latest tweets
3. **Compares** → Checks if there's a new tweet ID
4. **If new tweet** → Cross-posts to LinkedIn and Telegram
5. **Stores tweet ID** → Prevents duplicate posting
6. **Repeats** → Continues monitoring forever

**Flow Diagram:**
```
Start → Get User ID → Fetch Latest Tweet
  ↓
  Check if new?
  ↓ YES          ↓ NO
  Post           Wait 5 min
  ↓
  Update last ID
  ↓
  Loop back to fetch
```

---

## 🔍 Troubleshooting

### Bot Not Detecting Tweets

**Check:**
1. Is `TWITTER_USERNAME` correct? (no @ symbol!)
2. Is your X account public? (bot can't read private accounts)
3. Did you post a NEW tweet AFTER the bot started?

**Fix:**
- First run stores the current tweet ID
- Post a NEW tweet after bot starts
- Wait for next check cycle (5 minutes)

---

### "Could not get Twitter user ID"

**Issue:** Username is wrong or account doesn't exist

**Fix:**
- Check `TWITTER_USERNAME` in `.env`
- Must be exact username (case-sensitive)
- Don't include @ symbol

---

### LinkedIn Posting Fails

**Common Issues:**
1. Token expired
2. Wrong Person ID
3. Insufficient permissions

**Fix:**
- Generate new LinkedIn access token
- Verify Person ID
- Ensure `w_member_social` permission

---

### Telegram Not Receiving Messages

**Check:**
1. Is `TELEGRAM_CHAT_ID` correct?
2. Is bot admin in channel/group?
3. Did bot start successfully?

**Fix:**
- Verify Chat ID with @userinfobot
- Make bot admin if using channel/group
- Check Railway logs for Telegram errors

---

### Rate Limit Errors

**Issue:** Checking too frequently

**Fix:**
- Increase `CHECK_INTERVAL` to 300+ seconds
- Don't go below 180 seconds (3 minutes)

---

## 📝 Example `.env` File

```bash
# X/Twitter (FREE - Read-Only)
TWITTER_BEARER_TOKEN=AAAAAAAAAAAAAAAAAAAAAPABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghij
TWITTER_USERNAME=john_doe

# LinkedIn
LINKEDIN_ACCESS_TOKEN=AQVpKlMn...very_long_token
LINKEDIN_PERSON_ID=a1B2c3D4e5

# Telegram
TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklmnOPQRstuvWXYZ
TELEGRAM_CHAT_ID=987654321

# Settings
CHECK_INTERVAL=300
```

---

## 🎉 Success Checklist

After setup, verify:

- [ ] Bot starts without errors
- [ ] Logs show "Bot is now monitoring"
- [ ] Logs show "Initial tweet ID stored"
- [ ] Post new tweet on X
- [ ] Wait 5 minutes
- [ ] Check Railway logs for "NEW TWEET DETECTED"
- [ ] Verify post on LinkedIn
- [ ] Verify message in Telegram

**All checked? You're done! 🚀**

---

## 💰 Cost Breakdown

| Service | Cost |
|---------|------|
| X API (read-only) | **FREE** ✅ |
| LinkedIn API | **FREE** ✅ |
| Telegram Bot | **FREE** ✅ |
| Railway Hosting | **FREE** (500 hrs/month) ✅ |
| **TOTAL** | **$0/month** 🎉 |

**vs Original Bot with X posting: $100/month**

---

## 🔄 Workflow Comparison

### ❌ Original Bot (Expensive)
```
Telegram → Bot → X/Twitter ($100/month) + LinkedIn
```

### ✅ Reverse Bot (FREE)
```
X/Twitter (manual) → Bot (FREE) → LinkedIn + Telegram
```

**You save $100/month and still get auto-posting!**

---

## 📚 Additional Resources

- **X API Docs:** https://developer.twitter.com/en/docs/twitter-api
- **LinkedIn API:** https://learn.microsoft.com/en-us/linkedin/
- **Telegram Bots:** https://core.telegram.org/bots
- **Railway Docs:** https://docs.railway.app/

---

## 🤝 Need Help?

Check the logs first! Railway shows detailed error messages.

Common issues:
1. Wrong credentials → Double-check all tokens
2. Bot not monitoring → Check TWITTER_USERNAME
3. Not posting → Wait for check interval (5 min)

---

## 🎯 Pro Tips

1. **Test first** - Post a test tweet to verify everything works
2. **Monitor logs** - Railway logs show exactly what's happening
3. **Adjust interval** - 5 minutes is good, but you can change it
4. **LinkedIn tokens expire** - Refresh monthly
5. **Keep credentials safe** - Never commit .env to GitHub!

---

## 📄 License

MIT License - Free to use and modify!

---

**You're all set! Post on X and watch it auto-share to LinkedIn and Telegram! 🚀**
