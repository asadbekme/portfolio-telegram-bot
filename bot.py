import os
import telebot
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Access variables
TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = os.getenv("OWNER_ID")

if not TOKEN:
    raise ValueError("BOT_TOKEN is not set in environment variables")

bot = telebot.TeleBot(TOKEN)
