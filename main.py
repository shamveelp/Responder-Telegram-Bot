from typing import Final
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application,CommandHandler,MessageHandler,filters, ContextTypes,ApplicationBuilder


# Load environment variables from .env file
load_dotenv()


# Access the token
TOKEN = os.getenv("BOT_TOKEN")
BOT_USERNAME: Final = '@conv_erte_r_bot'


# Commands to the bot 
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Thanks for chating with me..! I am a bot created by Coding Aashan!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Type Something so I Can Respond!')

async def aashanod_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('You wanna tell something to coding aashan')


# Handle Responses 
def handle_reponse(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hey there!'
    
    if 'how are you' in processed:
        return 'I am good!'
    
    if 'i love python' in processed:
        return 'Remember to subscribe!'
    
    return 'I do not understand what you wrote...'



async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME,'').strip()
            response: str = handle_reponse(new_text)
        else:
            return
    else:
        response: str = handle_reponse(text)
    
    print('Bot',response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print('Starting Bot...')
    app = Application.builder().token(TOKEN).build()

    # Commands 
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('aashanod', aashanod_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3)


