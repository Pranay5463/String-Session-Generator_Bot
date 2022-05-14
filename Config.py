import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    MONGO_URI = os.environ.get('MONGO_URI', None)
    UPDATES_CHANNEL = os.environ.get('UPDATES_CHANNEL', None)
    if UPDATES_CHANNEL.startswith("@"):
        UPDATES_CHANNEL = UPDATES_CHANNEL[1:]
