"""
Made by Naboraj Sarkar (Nishant Sarkar)

This script automatically fetches memes from Reddit and posts them to a Telegram channel.
It uses the PRAW (Python Reddit API Wrapper) library to interact with Reddit,
and the Telegram Bot API to send memes with random funny captions.

To use this script safely:
1. Replace the placeholders below (TELEGRAM_BOT_TOKEN, TELEGRAM_CHANNEL, REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET)
   with your own credentials.
2. Never commit your real keys/tokens to GitHub. Use environment variables instead (os.getenv).
"""

import praw
import requests
import random
import time
import os

# ================== CONFIGURATION ==================
# Replace with your own tokens/IDs or load them from environment variables
telegram_bot_token = "YOUR_TELEGRAM_BOT_TOKEN"   # Get from BotFather
telegram_channel = "@your_channel_username"      # Example: @nsmeems

# Initialize Reddit client with credentials (create an app on https://www.reddit.com/prefs/apps)
reddit = praw.Reddit(
   client_id="YOUR_REDDIT_CLIENT_ID",
   client_secret="YOUR_REDDIT_CLIENT_SECRET",
   user_agent="NS_MEME_BOT"  # A short name for your bot
)

# List of meme subreddits to fetch memes from
subreddits = ["IndianDankMemes", "DesiHumor", "BollywoodRealism", "MemeEconomy", "WholesomeMemes"]

# File to keep track of already posted memes (prevents reposting)
posted_memes_file = "posted_memes.txt"
if not os.path.exists(posted_memes_file):
    open(posted_memes_file, 'w').close()

# ================== FUNCTIONS ==================

def get_random_meme():
    """
    Fetches a random meme from one of the chosen subreddits.
    Ensures the meme has not been posted before by checking against a local file.
    """
    try:
        # Choose a random subreddit
        subreddit = reddit.subreddit(random.choice(subreddits))

        # Fetch top 100 hot posts from the subreddit
        for submission in subreddit.hot(limit=100):
            # Only allow image posts (jpg/png/jpeg)
            if submission.url.endswith(("jpg", "png", "jpeg")):
                # Read previously posted URLs
                with open(posted_memes_file, 'r') as f:
                    posted_urls = f.read().splitlines()

                # If this meme hasn't been posted yet
                if submission.url not in posted_urls:
                    # Save this meme URL to the posted list
                    with open(posted_memes_file, 'a') as f:
                        f.write(submission.url + "\n")
                    return submission.url  # Return the meme URL

        print("No new meme found.")
    except Exception as e:
        print(f"Error fetching meme: {e}")
    return None


def post_to_telegram(meme_url):
    """
    Sends a meme (image URL) to the configured Telegram channel with a random funny caption.
    """
    try:
        # A large pool of captions (funny/emojis) to add variety
        captions = [
            "🤣🤣🤣", "😂😂😂😂", "🔥🔥🔥🔥", "😎😎😎", "😜😜😜",
            "Brooo 💀", "Internet undefeated 🤣", "This killed me 😂😂",
            "Ok, who made this? 💀", "Legends only 😂🔥", "Bruh moment 🤣",
            "Certified meme material ✅", "Made my day 😂🙌",
            "Why is this so accurate 💀😂", "Mood = this meme 🤣",
            "I can’t stop laughing 😂🔥", "Comedy gold 🔥🤣",
            "This aged like fine wine 🍷😂", "Relatable AF 😂",
            "Straight to the hall of fame 🏆🤣", "Peak humor right here 🤣",
            "Absolute chaos 😂🔥", "Send help, I’m dying laughing 💀😂",
            "Memes > Therapy 🤣", "So true it hurts 😂🔥",
            "Brain: don’t laugh… Me: 😂😂😂", "This should be in the textbooks 📚😂",
            "Dumb but hilarious 😂", "0% logic, 100% comedy 😂",
            "This hits different 😂🔥", "Pure chaos 💀🔥",
            "Legendary meme spotted 🏆🤣", "Proof humanity is still funny 😂",
            "Best medicine = memes 💊😂", "GG EZ 😂", "Respawn my humor 💀",
            "Lagging but still funny 😂", "OP content only 🔥",
            "Achievement unlocked: Laughed till tears 😂",
            "Straight outta meme factory 🔥🤣", "National treasure 🏆😂",
            "Meme economy is booming 📈🤣", "This deserves a Nobel Prize 🏅😂",
            "When reality is a meme 💀", "Memes are modern poetry 📖😂",
            "If memes were currency, I’d be rich 💸🤣", "Best bug in the matrix 🤣",
            "Universe approves this meme 🌌🤣", "Comedy central material 🔥😂",
            "Doctor’s prescription: 1 meme a day 💊😂", "My brain cells left the chat 💀",
            "Relatable on a spiritual level 🧘😂", "Powered by memes ⚡🤣",
            "Top tier humor 🤣", "Hall of fame moment 🏆😂",
            "Peak comedy detected 🎯😂", "Warning: too funny to handle ⚠️🤣",
            "Perfect 10/10 meme ⭐🤣", "World peace through memes ☮️😂",
            "Clown energy at its finest 🤡😂", "Instant serotonin boost 💊🤣",
            "Memes run the world 🌍🤣", "Unexpected but hilarious 😂",
            "Somebody give this meme a medal 🥇😂", "Approved by the meme gods 🔥😂",
            "LOL factory open 24/7 😂", "Internet historians will remember this 🤣",
            "Peak relatability 🔥😂", "I’ll never recover from this meme 😂",
            "Unskippable meme ad 😂🔥", "Forbidden meme energy 🚫🤣",
            "If memes were food, I’d be obese 🍔😂", "Zero context, maximum comedy 🤣",
            "The evolution of humor 😂🔥", "Infinite laughter loop 🔁😂",
            "Chaos level: 1000 🔥🤣", "Straight facts 😂",
            "Memes make Mondays better ☕🤣", "This is meme history 📖🤣",
            "We live in a society 🤡😂", "One does not simply skip this meme 🗡️🤣",
            "Cursed but funny 😂🔥", "Too accurate it hurts 😂",
            "Peak internet culture 🤣", "Future archaeologists will study this meme 🏺😂"
        ]

        # Pick a random caption
        caption = random.choice(captions)

        # Telegram API endpoint for sending images
        telegram_api_url = f"https://api.telegram.org/bot{telegram_bot_token}/sendPhoto"

        # Send the meme
        response = requests.post(telegram_api_url, data={
            "chat_id": telegram_channel,
            "photo": meme_url,
            "caption": caption
        })

        # Check for success
        if response.status_code == 200:
            print(f"Successfully posted: {meme_url} with caption: {caption}")
        else:
            print(f"Failed to post: {response.status_code} - {response.json()}")
    except Exception as e:
        print(f"Error posting meme: {e}")


# ================== MAIN LOOP ==================

# Infinite loop to keep fetching and posting memes
while True:
    try:
        # Fetch a meme
        meme = get_random_meme()

        if meme:
            # If meme found, post to Telegram
            post_to_telegram(meme)
        else:
            # If no meme found, retry after 2 minutes
            print("Retrying in 2 minutes...")

        # Wait 30 seconds before the next attempt
        # (Change this to time.sleep(600) if you want a 10 min delay)
        time.sleep(120)

    except Exception as e:
        # Catch any unexpected error and keep script running
        print(f"Script encountered an error: {e}")
