from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
import os
from handle_response import ResponseHandler

# Load environment variables from .env
load_dotenv()

# Constants
TOKEN: Final[str] = os.getenv('TOKEN')
BOT_USERNAME: Final[str] = os.getenv('BOT_USERNAME')

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello There! Nice to meet you. Let\'s Chat!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Just type something and I will respond to you!')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command')

async def handle_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    handler = ResponseHandler()
    message_text = update.message.text
    response = handler.get_response(message_text)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error: {context.error}')

def main():
    print('Starting up bot...')

    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    
    # Messages
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_response))

    # Errors
    app.add_error_handler(error)

    print('Polling...')
    app.run_polling(poll_interval=5)

if __name__ == '__main__':
    main()
