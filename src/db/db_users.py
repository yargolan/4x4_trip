
import json
import pymongo
from pprint import pprint
from src.AppData import AppData


# Insert the data into the DB.
db_name = AppData.db_name



def user_add(data):

    allowed_to_add = True

    mongo_client = pymongo.MongoClient(AppData.client_name)
    my_db   = mongo_client[db_name]
    col_participants = my_db["Participants"]

    for result in col_participants.find():
        if result['name'] == data['name']:
            print("Same name")
            allowed_to_add = False
            break

        if result['email'] == data['email']:
            print("Same email")
            allowed_to_add = False
            break

    if allowed_to_add:
        if AppData.debug:
            print("Debug: Add the user.")

        col_participants.insert_one(data)
