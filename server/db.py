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
        # client = MongoClient('mongodb://' + DB_USER + ':' + urllib.parse.quote(DB_PASS)  + DB_URL)
        # self.db = client['twitter-bot-db']
        client = MongoClient('mongodb://localhost:27017/')
        self.db = client.twitrender
        self.db.tweets.create_index([('status', TEXT)])


    # Prepare dates to be used for searching by using python datetime lib
    def prepare_date_for_search(self, date):
        date = date.split('-')
        return datetime(int(date[0]), int(date[1]), int(date[2]))

    # Search by given start date (till the end of the database) and a word
    def search_by_start(self, start_date, word):
        start_date_for_search = self.prepare_date_for_search(start_date)
        aggregated_results = self.db.tweets.aggregate([
            {
                '$match': {
                    '$text': { '$search': word },
                },
            },
            {
                '$addFields': {
                    'created_at': {
                        '$toDate': '$created_at'
                    },
                }
            },
             {
                '$match': {
                    'created_at': {
                        '$gte': start_date_for_search
                    },
                },
             },
        ])

        result = len(list(aggregated_results))
        print('[*] Search results for word: \"%s\" and start date: [%s] ==> %d ' % (word, start_date_for_search, result))
        return result

    # Search by given end date (from the beginning of the database) and a word
    def search_by_end(self, end_date, word):
            end_date_for_search = self.prepare_date_for_search(end_date)
            aggregated_results = self.db.tweets.aggregate([
                {
                    '$match': {
                        '$text': { '$search': word },
                    },
                },
                {
                    '$addFields': {
                        'created_at': {
                            '$toDate': '$created_at'
                        },
                    }
                },
                 {
                    '$match': {
                        'created_at': {
                            '$lte': end_date_for_search
                        },
                    },
                 },
            ])

            result = len(list(aggregated_results))
            print('[*] Search results for word: \"%s\" and end date: [%s] ==> %d ' % (word, end_date_for_search, result))
            return result

    # Search by given date and end dates and a word
    def search_by_both(self, start_date, end_date, word):
                start_date_for_search = self.prepare_date_for_search(start_date)
                end_date_for_search = self.prepare_date_for_search(end_date)
                aggregated_results = self.db.tweets.aggregate([
                    {
                        '$match': {
                            '$text': { '$search': word },
                        },
                    },
                    {
                        '$addFields': {
                            'created_at': {
                                '$toDate': '$created_at'
                            },
                        }
                    },
                     {
                        '$match': {
                            'created_at': {
                                '$gte': start_date_for_search,
                                '$lte': end_date_for_search
                            },
                        },
                     },
                ])

                result = len(list(aggregated_results))
                print('[*] Search results for word: \"%s\" and dates from [%s] to [%s] ==> %d ' % (word, start_date_for_search, end_date_for_search, result))
                return result

    def search(self, word, start_date, end_date):
        print('[*] Searching for word: ', word)
        print('[*] Searching for selected dates -> from: ', start_date, ' to: ', end_date)

        # No dates selected - search the whole database
        if start_date ==  'None' and end_date == 'None':
            return self.db.tweets.count_documents( { '$text': { '$search': word } } )

        # Start date provided - search the database from this date to the end
        elif start_date != 'None' and end_date == 'None':
            return self.search_by_start(start_date, word)

        # End date provided - search the database from the beginning to this date
        elif start_date == 'None' and end_date != 'None':
            return self.search_by_end(end_date, word)

        # Start and end dates provided - search the database between these dates
        elif start_date != 'None' and end_date != 'None':
            return self.search_by_both(start_date, end_date, word)
