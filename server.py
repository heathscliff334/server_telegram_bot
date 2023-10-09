from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from command_handlers import *

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Add command handlers to the dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help_command))
dispatcher.add_handler(CommandHandler('ping', ping))
dispatcher.add_handler(CommandHandler('uptime', uptime))
dispatcher.add_handler(CommandHandler('memory', memory))
dispatcher.add_handler(CommandHandler('custom_command', custom_command))

def main():    
    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
