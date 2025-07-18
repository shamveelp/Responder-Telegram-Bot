from typing import Final
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application,CommandHandler,MessageHandler,filter, ContextTypes,ApplicationBuilder


# Load environment variables from .env file
load_dotenv()

# Access the token
TOKEN = os.getenv("BOT_TOKEN")
BOT_USERNAME: Final = '@conv_erte_r_bot'

# Commands to the bot 
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPES):
    await update.message.reply_text('Hello! Thanks for chating with me..! I am a bot created by Coding Aashan!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPES):
    await update.message.reply_text('Type Something so I Can Respond!')

async def aashanod_command(update: Update, context: ContextTypes.DEFAULT_TYPES):
    await update.message.reply_text('You wanna tell something to coding aashan')





