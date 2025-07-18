from typing import Final
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


# Load environment variables from .env file
load_dotenv()

# Access the token
TOKEN = os.getenv("BOT_TOKEN")


BOT_USERNAME: Final = '@conv_erte_r_bot'






