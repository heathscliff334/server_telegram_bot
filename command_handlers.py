import os
import psutil
import subprocess
import json
from utilities import *
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = config['TOKEN']

authorized_users = config['authorized_users']

# Define command handlers
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your VPS control bot. Send /help to see available commands.')

def ping(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Pong!")

def help_command(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.username  # Get the user's username
    if is_authorized(user_id):
        update.message.reply_text('Available commands:\n'
                              '/help - Check available commands\n'
                              '/ping - Check server response\n'
                              '/uptime - Check server uptime\n'
                              '/memory - Check memory usage\n'
                              '============================\n\n'
                              '/custom_command - Custom command\n')
    else:
        update.message.reply_text('Available commands:\n'
                              '/help - Check available commands\n'
                              '/ping - Check server response')
    
def uptime(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.username  # Get the user's ID
    if is_authorized(user_id):
        uptime = os.popen('uptime').read()
        update.message.reply_text(uptime)
    else:
        update.message.reply_text("You are not authorized to use this command.")

def memory(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.username  # Get the user's ID
    if is_authorized(user_id):
        memory_info = psutil.virtual_memory()
    
        # Calculate memory usage percentages
        used_percent = (memory_info.used / memory_info.total) * 100
        available_percent = 100 - used_percent
        
        # Convert bytes to gigabytes (GB)
        total_gb = memory_info.total / (1024 ** 3)
        available_gb = memory_info.available / (1024 ** 3)
        used_gb = memory_info.used / (1024 ** 3)
        
        # Format the response message
        message = (
            f'Memory Usage:\n'
            f'Total: {total_gb:.2f} GB\n'
            f'Available: {available_gb:.2f} GB ({available_percent:.2f}%)\n'
            f'Used: {used_gb:.2f} GB ({used_percent:.2f}%)'
        )
        
        update.message.reply_text(message)
    else:
        update.message.reply_text("You are not authorized to use this command.")

def custom_command(update: Update, context: CallbackContext):
    user_id = update.effective_user.username  # Get the user's ID
    if is_authorized(user_id):
        command = context.args  # Extract the command from the user's message
        try:
            result = os.popen(' '.join(command)).read()
            update.message.reply_text(result)
        except Exception as e:
            update.message.reply_text(f"Error: {str(e)}")
    else:
        update.message.reply_text("You are not authorized to use this command.")

__all__ = [
    'start',
    'ping',
    'help_command',
    'uptime',
    'memory',
    'custom_command',
    'TOKEN'
]
