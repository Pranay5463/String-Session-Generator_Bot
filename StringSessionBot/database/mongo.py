from pymongo import MongoClient
import os
from Config import MONGO_URI

MONGO_NAME = "SessionStringBot"
MONGO_URI = MONGO_URI

Flux = MongoClient(MONGO_URI)
self = Flux[MONGO_NAME]
self = self["DB"]

def insert(chat_id):
    user_id = int(chat_id)
    userge = {"_id":user_id}
    try:
        self.insert_one(userge)
    except:
        pass
    
def find_one(id):
	return self.find_one({"_id":id})
