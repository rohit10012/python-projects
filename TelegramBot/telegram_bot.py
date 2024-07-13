import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext
from dotenv import load_dotenv
import os
from queue import Queue

my_queue = Queue()

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(filename='chat.log', format='%(asctime)s - %(message)s', level=logging.INFO)
logger = logging.getLogger()

# Telegram Bot token from environment variables
TOKEN = os.getenv('TOKEN')

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello! I am your bot. How can I help you today?')

def handle_message(update: Update, context: CallbackContext):
    user = update.message.from_user
    text = update.message.text
    
    # Log the chat message
    logger.info(f"User {user.username}: {text}")

    # Process the message
    response = "I received your message!"

    # Send the response back to the user
    update.message.reply_text(response)

def main():
    # Create the Updater with the update queue
    updater = Updater(TOKEN, update_queue=my_queue)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register command handlers
    dp.add_handler(CommandHandler("start", start))

    # Register message handler to handle text messages
    dp.add_handler(MessageHandler(filters.text & ~filters.command, handle_message))

    # Start the Bot
    updater.start_polling()
    logger.info("Bot started polling...")

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM, or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
