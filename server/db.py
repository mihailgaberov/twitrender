from pymongo import MongoClient, TEXT
from bson.objectid import ObjectId
from dotenv import load_dotenv
from datetime import datetime
import os
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

    def search(self, word, start_date, end_date):
        print('[*] Searching for word: ', word)
        print('[*] Searching for selected dates -> from: ', start_date, ' to: ', end_date)
        # No dates selected - search the whole database
        if start_date ==  'None' and end_date == 'None':
            return self.db.tweets.count_documents( { '$text': { '$search': word } } )
        # Start date provided - search the database from this date to the end
        elif start_date != 'None' and end_date == 'None':
            start_date = start_date.split('-')
            start_date_for_search = datetime(int(start_date[0]), int(start_date[1]), int(start_date[2]))
            return self.db.tweets.count_documents( { '$text': { '$search': word }, 'created_at': { '$gte': start_date_for_search } } )
        # End date provided - search the database from the beginning to this date
        elif start_date == 'None' and end_date != 'None':
            end_date = end_date.split('-')
            end_date_for_search = datetime(int(end_date[0]), int(end_date[1]), int(end_date[2]))
            return self.db.tweets.count_documents( { '$text': { '$search': word },  'created_at': { '$lte': end_date_for_search } } )
        # Start and end dates provided - search the database between these dates
        elif start_date != 'None' and end_date != 'None':
            start_date = start_date.split('-')
            start_date_for_search = datetime(int(start_date[0]), int(start_date[1]), int(start_date[2]))
            end_date = end_date.split('-')
            end_date_for_search = datetime(int(end_date[0]), int(end_date[1]), int(end_date[2]))
            return self.db.tweets.count_documents( { '$and': [{ 'created_at': { '$gte': start_date_for_search } }, { 'created_at': { '$lte': end_date_for_search } }, { '$text': { '$search': word } } ] } )
