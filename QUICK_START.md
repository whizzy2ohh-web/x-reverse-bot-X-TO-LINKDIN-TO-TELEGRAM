# 🚀 Quick Deployment Guide - Reverse Bot

Get your bot running in 20 minutes!

---

## ⚡ Super Quick Setup

### 1. Get Your 4 Credentials (15 minutes)

#### A) X/Twitter Bearer Token (FREE - 5 min)
1. Go to https://developer.twitter.com/en/portal/dashboard
2. Sign up for **FREE tier**
3. Create project and app
4. Copy **Bearer Token**
5. Note your X username (without @)

✅ **FREE - No credit card needed!**

#### B) LinkedIn Token (5 min)
1. Go to https://www.linkedin.com/developers/apps
2. Create app
3. Get OAuth token
4. Get your Person ID

#### C) Telegram Bot Token (2 min)
1. Open Telegram
2. Search **@BotFather**
3. Send `/newbot`
4. Copy token

#### D) Telegram Chat ID (3 min)
1. Search **@userinfobot** in Telegram
2. Start bot
3. Copy your Chat ID

---

### 2. Deploy to Railway (5 minutes)

#### Step 1: Upload to GitHub
```bash
git clone https://github.com/YOUR_USERNAME/x-reverse-bot.git
cd x-reverse-bot
# Push to YOUR GitHub
```

#### Step 2: Connect to Railway
1. Go to https://railway.app/
2. Sign up with GitHub
3. New Project → Deploy from GitHub
4. Select your repo

#### Step 3: Add Variables
In Railway → Variables → Raw Editor:

```env
TWITTER_BEARER_TOKEN=your_bearer_token_here
TWITTER_USERNAME=your_x_username_without_@
LINKEDIN_ACCESS_TOKEN=your_linkedin_token
LINKEDIN_PERSON_ID=your_person_id
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_chat_id
CHECK_INTERVAL=300
```

**Save → Bot starts automatically!**

---

## 🧪 Testing (5 minutes)

### Step 1: Check Railway Logs
Look for:
```
✅ Bot is now monitoring. Post something on X to test!
```

### Step 2: Post on X
Tweet anything: "Testing my bot! 🚀"

### Step 3: Wait 5 Minutes
Bot checks every 5 minutes

### Step 4: Verify
- ✅ Check LinkedIn for your post
- ✅ Check Telegram for message
- ✅ Check Railway logs for "NEW TWEET DETECTED"

---

## 📋 Checklist

Before deploying:
- [ ] Got X Bearer Token (FREE tier)
- [ ] Noted X username (without @)
- [ ] Got LinkedIn token & Person ID
- [ ] Created Telegram bot
- [ ] Got Telegram Chat ID
- [ ] Pushed to GitHub
- [ ] Signed up for Railway

After deploying:
- [ ] Added all environment variables
- [ ] Checked logs show "monitoring"
- [ ] Posted test tweet
- [ ] Waited 5 minutes
- [ ] Verified LinkedIn post
- [ ] Verified Telegram message

**All done? You're live! 🎉**

---

## 🔧 Quick Fixes

| Problem | Solution |
|---------|----------|
| "Could not get user ID" | Check `TWITTER_USERNAME` (no @) |
| No new tweets detected | Wait 5 min, post AFTER bot started |
| LinkedIn fails | Check token isn't expired |
| Telegram not working | Verify Chat ID is correct |
| Bot not running | Check Railway deployment logs |

---

## 💡 Pro Tips

1. **First run** stores your latest tweet ID - post something NEW after starting
2. **Check interval** - 5 minutes is perfect, don't go lower
3. **LinkedIn tokens** - Expire after 60 days, refresh them
4. **Free forever** - Railway gives 500 hours/month (20+ days)
5. **Monitor logs** - Railway shows exactly what's happening

---

## 🎯 How It Works

```
┌─────────────────────────────────────┐
│  You post on X manually             │
└──────────┬──────────────────────────┘
           │
           ↓
┌─────────────────────────────────────┐
│  Bot checks X every 5 minutes       │
│  (Uses FREE read-only API)          │
└──────────┬──────────────────────────┘
           │
           ↓
┌─────────────────────────────────────┐
│  New tweet detected?                │
└──────────┬──────────────────────────┘
           │
     ┌─────┴─────┐
     │ YES       │ NO → Wait & check again
     ↓           
┌─────────────────────────────────────┐
│  Cross-post to:                     │
│  • LinkedIn ✅                      │
│  • Telegram ✅                      │
└─────────────────────────────────────┘
```

---

## 💰 Cost: $0/month

| What | Cost |
|------|------|
| X API (read) | FREE |
| LinkedIn API | FREE |
| Telegram | FREE |
| Railway | FREE |
| **Total** | **$0** |

**vs $100/month for X posting API!**

---

## 📱 Example Output

**You tweet:**
> Just launched my new product! 🚀

**5 minutes later:**

**LinkedIn:**
> Just launched my new product! 🚀
> 
> Originally posted on X: https://twitter.com/you/status/123...

**Telegram:**
> 🐦 New post from X:
> 
> Just launched my new product! 🚀
> 
> 🔗 https://twitter.com/you/status/123...

---

## 🆘 Need More Help?

See the full **README.md** for:
- Detailed API setup instructions
- Advanced configuration
- Troubleshooting guide
- Alternative deployment options

---

**Ready? Let's go! 🚀**

1. Get credentials (15 min)
2. Deploy to Railway (5 min)  
3. Post on X and test! (5 min)

**Total: 25 minutes to auto cross-posting!**
