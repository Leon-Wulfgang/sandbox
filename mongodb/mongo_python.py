from datetime import datetime
skill_doc = {
    "name": "Python",
    "category": "Programming Language",
    "firstuse": datetime(2008, 9, 1),
    "lastuse": datetime(2017, 7, 14),
    "usecount": 0,
}

from bson import objectid
user_generated_object_id = objectid.ObjectId()


def main():
    from pymongo import MongoClient
    client = MongoClient('mongodb://localhost:27017/')
    db = client['skilltrack']
    collection = db.skill
    skill_id = collection.insert_one(skill_doc).inserted_id


if __name__ == '__main__':
    main()
