
import pymongo
from src import Logger
from src.AppData import AppData



client = pymongo.MongoClient(AppData.client)
my_db = client[AppData.db_name]
col_participants = my_db[AppData.col_name_participants]



def user_add(data):
    if is_user_exists(data['name'], data['email']):
        Logger.debug(f"The user '{data['name']}' already exists in the DB.")
    else:
        col_participants.insert_one(data)



def user_del(data):
    if is_user_exists(data['name'], data['email']):
        col_participants.delete_one(data)
    else:
        Logger.debug(f"The user '{data['name']}' does not exist in the DB.")



def user_edit(data):
    if is_user_exists(data['name'], data['email']):
        old_data = {"name": data['name'], "email": data['email'], "vehicle_index": data['vehicle_index']}
        user_del(old_data)

    # Now add the new details.
    new_data = {"name": data['new_name'], "email": data['new_email'], "vehicle_index": data['new_vehicle_index']}
    user_add(new_data)



def is_user_exists(name, email):
    data = {"name": name, "email": email}
    result = col_participants.find_one(data)
    return result is not None
