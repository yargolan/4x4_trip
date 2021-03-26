import os
import sys
import json
from pprint import pprint

import pymongo
from db import init_db
from db import db_users


# Global variables.
db_config  = {}
app_config = {}
debug_mode = False



def main(arguments):

    # init the application.
    init_app()


    global debug_mode
    if app_config.get('debug').lower() == "true":
        debug_mode = True


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

    if debug_mode:
        print("Init the database")

    # Drop the database if the flag enables it.
    if db_config['drop_db_allowed'] == "True":
        mongo_client.drop_database(db_name)


    db_list = mongo_client.list_database_names()
    if db_name in db_list:
        if debug_mode:
            print("The database exists.")
        return
    else:
        if debug_mode:
            print(f"Create the database '{db_name}'.")

    init_db.set_initial_data(mongo_client)



def init_app():
    with open('../config/config.json') as c:
        global app_config
        app_config = json.load(c)

    with open('../config/db_config.json') as db:
        global db_config
        db_config = json.load(db)

    global debug_mode
    if app_config.get('debug').lower() == "true":
        debug_mode = True

    if debug_mode:
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
            pprint(user_action_file['data'])
            db_users.user_add(user_action_file['data'])
    else:
        print(f"The request '{user_request}' is not allowed.")







if __name__ == '__main__':
    main(sys.argv)
