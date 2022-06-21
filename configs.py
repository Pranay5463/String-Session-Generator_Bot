import os
class Config:
    API_ID = int(os.environ.get('API_ID', 0))
    API_HASH = str(os.environ.get('API_HASH', None))
    BOT_TOKEN = str(os.environ.get('BOT_TOKEN', None))
    MONGO_URI = str(os.environ.get('MONGO_URI', "mongodb+srv://Mrperfect1234:mrperfect2222@mrperfect.u31bh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"))
    UPDATES_CHANNEL = str(os.environ.get('UPDATES_CHANNEL', None)) #Start Without @
