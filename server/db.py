from pymongo import MongoClient, TEXT
from bson.objectid import ObjectId
import os
from dotenv import load_dotenv
import urllib
load_dotenv()



class DB:
    def __init__(self):
        print('[*] Initializing DB object')
        DB_USER = os.getenv('DB_USER')
        DB_PASS = os.getenv('DB_PASS')
        DB_URL = os.getenv('DB_URL')
        #client = MongoClient('mongodb://' + DB_USER + ':' + urllib.parse.quote(DB_PASS)  + DB_URL)
        client = MongoClient('mongodb://localhost:27017/')
        self.db = client.twitrender
        # self.db = client['twitter-bot-db']
        self.db.tweets.create_index([('status', TEXT)])

    def search(self, word):
        print('[*] Searching for word: ', word)
        return self.db.tweets.count_documents( { '$text': { '$search': word } } )
