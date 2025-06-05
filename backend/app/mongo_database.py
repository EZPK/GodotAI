import os
from pymongo import MongoClient

MONGO_URL = os.getenv("MONGO_URL", "mongodb://mongo:27017")

_client = MongoClient(MONGO_URL, connect=False)
_db = _client[os.getenv("MONGO_DB", "godotai")]


def get_mongo_db():
    return _db
