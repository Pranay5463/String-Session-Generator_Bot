import os
class Config:
    API_ID = int(os.environ.get('API_ID', 0))
    API_HASH = str(os.environ.get('API_HASH', None))
    BOT_TOKEN = str(os.environ.get('BOT_TOKEN', None))
    MONGO_URI = str(os.environ.get('MONGO_URI', None))
    UPDATES_CHANNEL = str(os.environ.get('UPDATES_CHANNEL', None)) #Start Without @
