
import json
import pymongo
from db import init_db


# Global variables.
db_config  = {}
app_config = {}
debug_mode = False



def init_database():

    mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")

    db_name = db_config['databases']['name']

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

    init_db.set_initial_data(mongo_client, db_name)



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



def main():

    # init the application.
    init_app()


    # Init the database.
    init_database()



if __name__ == '__main__':
    main()
