# 🤖 NS Meme Bot  

**Made with ❤️ by [✨ Naboraj (Nishant) Sarkar ✨](https://github.com/ns-gamming)**  

---

This project is a **Reddit → Telegram Meme Bot** written in Python 🐍.  
It automatically fetches fresh memes from Reddit 🔥 and posts them to a Telegram channel 📲 with random captions 😂.  
The code is written in a **beginner-friendly style with detailed comments**, so even if you’re new to Python, you can understand and modify it easily 🎉.  

---

## 📺 Tutorial Video  

🎥 Watch the full setup guide here 👉 [YouTube Tutorial](https://youtu.be/pYEJTcH4nAc?si=gnIy_4v79l2TNQrS)  

---

## 🌟 Features  

- 🔥 Auto-fetches memes from top Indian & global meme subreddits.  
- ✅ Prevents reposts by tracking already posted memes in a text file 🗂️.  
- 🤣 Posts memes with funny random captions (120+ included).  
- 💡 Beginner-friendly code with line-by-line explanations ✍️.  
- ⏳ Adjustable posting interval (every 30s, 10m, or whatever you set ⏰).  
- 🌍 Can run locally 💻, or on free hosting platforms ☁️.  

---

## 👨‍💻 About the Creator  

Hi! I’m **Naboraj Sarkar (aka Nishant Sarkar)** 🎮💻  

- 📍 Location: Siliguri, West Bengal, India 🇮🇳  
- 📅 Born: 19 August 2010 🎂  
- 🎥 YouTuber: [@Nishant_sarkar](https://youtube.com/@Nishant_sarkar)  
- 📸 Instagram: [@nishant_sarkar__10k](https://instagram.com/nishant_sarkar__10k)  
- 🐦 Twitter (X): [@NSGAMMING699](https://x.com/NSGAMMING699)  
- 🌐 Website: [nsgamming.xyz](https://nsgamming.xyz)  
- 📧 Email: nishant.ns.business@gmail.com  

I enjoy coding 💻, memes 🤣, gaming 🎮, and building cool bots 🤖.  

---

## 🔧 Prerequisites  

You’ll need:  
- 🐍 Python **3.8+** installed  
- 🤖 A Telegram Bot Token (from BotFather)  
- 📲 A Telegram Channel where the bot can post  
- 🔑 A Reddit App Client ID + Secret  
- 🌐 Internet connection  

Install required libraries:  

```bash
pip install praw requests
```

---

## ⚡ Setup Guide  

### 1️⃣ Create a Telegram Bot  
1. Open Telegram → search **BotFather** 🤵.  
2. Type `/newbot` and follow instructions.  
3. Get your **TOKEN** 🔑.  
4. Add your bot to a **channel** and make it **Admin**.  

👉 Example test channel: [t.me/nsmeems](https://t.me/nsmeems)  

---

### 2️⃣ Get Reddit API Credentials  
1. Go to [Reddit Apps](https://www.reddit.com/prefs/apps).  
2. Click **Create App** ➕.  
3. Fill details:  
   - Name: `NS_MEME_BOT` 📝  
   - App type: `script` ⚡  
   - Redirect URI: `http://localhost:8080`  
4. Copy your:  
   - `client_id` 🆔  
   - `client_secret` 🔑  

---

### 3️⃣ Configure the Script  

Edit `main.py` and update placeholders:  

```python
telegram_bot_token = "YOUR_TELEGRAM_BOT_TOKEN"
telegram_channel = "@your_channel_username"
client_id = "YOUR_REDDIT_CLIENT_ID"
client_secret = "YOUR_REDDIT_CLIENT_SECRET"
```

---

### 4️⃣ Run the Bot  

Run in terminal:  

```bash
python meme.py
```

The bot will:  
- 🎯 Pick a random subreddit  
- 🖼️ Grab a meme (jpg/png/jpeg)  
- 🔍 Check if it’s already posted  
- 📲 Send it to your Telegram channel with a caption 🤣  

---

## 🗂 File Details  

- 📜 **main.py** → Bot script  
- 🗂️ **posted_memes.txt** → Keeps track of posted memes  

---

## ⚙️ Customization  

- ✏️ **Change Subreddits:** Update `subreddits` list.  
- ⏰ **Change Interval:** `time.sleep(30)` → change to `600` for 10 minutes.  
- 😂 **Add More Captions:** Extend `captions` list with your lines.  

---

## ☁️ Hosting Options  

- 💻 Run locally with Python.  
- 🔥 Use Replit for free online hosting.  
- 🚀 Railway / Render / Heroku for cloud hosting.  
- 🖥️ VPS for full control.  

---

## 📚 Example Output  

```
Successfully posted: https://i.redd.it/meme123.jpg with caption: "This killed me 😂😂"
Next meme in 10 minutes...
```  

On Telegram:  

📷 Meme Image  
💬 *"Ok, who made this? 💀"*  

---

## 🛡️ Safety & Notes  

- ⚠️ Don’t upload your **real keys** to GitHub 🚫.  
- Use **environment variables** instead:  

```python
import os
telegram_bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
```  

- 🐢 Slow down posting if Reddit rate-limits.  
- ❌ If Telegram rejects large images, the bot skips and continues.  

---

## 📜 License  

This project is free & open source 🎉.  
✅ You can use it in your projects.  
⚠️ Please **give credit** to the creator (Naboraj Sarkar).  

Recommended: MIT License or CC-BY.  

---

## ❤️ Credits  

Made with love ❤️ by **Naboraj (Nishant) Sarkar** ✨  
- 📩 Email: nishant.ns.business@gmail.com  
- 📲 Telegram: [@nsgamming69](https://t.me/nsgamming69)  
- 🎥 YouTube: [@Nishant_sarkar](https://youtube.com/@Nishant_sarkar)  

👉 Don’t forget to ⭐ Star & 🍴 Fork this repo if you like it!  
