
import json
from pprint import pprint

import pymongo
from src import Logger
from src.AppData import AppData



client = pymongo.MongoClient(AppData.client)
my_db = client[AppData.db_name]
col_participants = my_db[AppData.col_name_participants]



def user_add(request_file):

    with open(request_file) as r:
        request = json.load(r)

    data = request['data']

    if is_user_exists(data['name'], data['email']):
        Logger.debug(f"The user '{data['name']}' already exists.")
    else:
        col_participants.insert_one(data)


def user_del(request_file):

    with open(request_file) as r:
        request = json.load(r)

    data = request['data']

    if is_user_exists(data['name'], data['email']):
        col_participants.delete_one(data)
    else:
        Logger.debug(f"The user '{data['name']}' does not exist.")


def user_edit(request_file):
    pass


def is_user_exists(name, email):
    data = {"name": name, "email": email}
    result = col_participants.find_one(data)
    return result is not None
