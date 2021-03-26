import os
import sys
import json
import pymongo
from pprint import pprint
from db import init_db
from db import db_users
from AppData import AppData


# Global variables.
db_config  = {}
app_config = {}



def main(arguments):

    # init the application.
    init_app()


    # Init the database.
    init_database()


    # Perform user's actions
    if len(arguments) == 2:
        json_file = arguments[1]
        if os.path.isfile(json_file):
            perform_action(json_file)
        else:
            print(f"\nError:\nThe json file '{json_file}' is absent.")
            sys.exit(0)
    else:
        sys.exit(0)



def init_database():

    mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")

    db_name = db_config['database_name']

    if AppData.cfg_debug:
        print("DEBUG: Init the database")

    # Drop the database if the flag enables it.
    if db_config['drop_db_allowed'] == "True":
        mongo_client.drop_database(db_name)


    db_list = mongo_client.list_database_names()
    if db_name in db_list:
        if AppData.cfg_debug:
            print("DEBUG: The database exists.")
        return
    else:
        if AppData.cfg_debug:
            print(f"DEBUG: Create the database '{db_name}'.")

    init_db.set_initial_data(mongo_client)



def init_app():
    with open('../config/config.json') as c:
        global app_config
        app_config = json.load(c)

    with open('../config/db_config.json') as db:
        global db_config
        db_config = json.load(db)

    if AppData.cfg_debug:
        print("\n*** Running in DEBUG mode. ***\n\n")



def perform_action(action_file):

    # Read the allowed actions file.
    with open("../config/requests.json") as ar:
        allowed_requests = json.load(ar)

    # Read the user's requests file.
    with open(action_file) as af:
        user_action_file = json.load(af)

    user_request = user_action_file['action']

    if user_request in allowed_requests['allowed_requests']:
        if user_request == "user_add":
            db_users.user_add(user_action_file['data'])
        elif user_request == "user_del":
            db_users.user_del(user_action_file['data'])
        else:
            print(f"Cannot find what to do with the '{user_request}' action.")
    else:
        print(f"ERROR: The request '{user_request}' is not allowed.")







if __name__ == '__main__':
    main(sys.argv)
