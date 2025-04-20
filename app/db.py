from pymongo import MongoClient
import os

def init_db(app):
    MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
    MONGO_PORT = int(os.environ.get('MONGO_PORT', 27017))
    MONGO_DB = os.environ.get('MONGO_DB', 'daily_db')

    client = MongoClient(f"mongodb://{MONGO_HOST}:{MONGO_PORT}/")
    app.db = client[MONGO_DB]
