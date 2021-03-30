
import pymongo
from src.AppData import AppData



# Insert the data into the DB.
db_name = AppData.cfg_db_name



def user_add(data):

    reason = ""
    allowed_to_add = True

    mongo_client     = pymongo.MongoClient(AppData.cfg_client_name)
    my_db            = mongo_client[db_name]
    col_participants = my_db["Participants"]

    for result in col_participants.find():
        if result['name'] == data['name']:
            reason = "Same name"
            allowed_to_add = False
            break

        if result['email'] == data['email']:
            reason = "Same email"
            allowed_to_add = False
            break

    if allowed_to_add:
        if AppData.cfg_debug:
            print("Debug: Add the user.")

        col_participants.insert_one(data)
    else:
        print("Cannot add the user: " + reason)



def user_del(data):

    mongo_client     = pymongo.MongoClient(AppData.cfg_client_name)
    my_db            = mongo_client[db_name]
    col_participants = my_db["Participants"]

    details = {"name": data['name'], "email": data['email']}

    col_participants.delete_one(details)

