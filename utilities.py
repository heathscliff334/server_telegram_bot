import psutil
import json

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

authorized_users = config['authorized_users']

def is_authorized(user_id):
    return str(user_id) in authorized_users

def bytes_to_readable(bytes):
    # Convert bytes to MB or GB as appropriate
    if bytes < 1024**2:
        return f"{bytes / 1024:.2f} MB"
    elif bytes < 1024**3:
        return f"{bytes / (1024**2):.2f} GB"
    else:
        return f"{bytes / (1024**3):.2f} GB"

__all__ = [
    'is_authorized',
    'bytes_to_readable'
]
