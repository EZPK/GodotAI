import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from backend.app.mongo_database import get_mongo_db
from pymongo.database import Database

def test_get_mongo_db():
    db = get_mongo_db()
    assert isinstance(db, Database)
