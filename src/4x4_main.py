
import json
import pymongo
from db import init_db


# Global variables.
db_config  = {}
app_config = {}
debug_mode = False



def main():

    # init the application.
    init_app()

    global debug_mode
    if app_config.get('debug').lower() == "true":
        debug_mode = True

    # Init the database.
    init_database()



def init_database():

    mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")

    db_name = db_config['databases']['name']

    my_db = mongo_client[db_name]

    if debug_mode:
        print("Init the database")
        mongo_client.drop_database(db_name)


    db_list = mongo_client.list_database_names()
    if db_name in db_list:
        if debug_mode:
            print("The database exists.")
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



if __name__ == '__main__':
    main()














"""

from db import init_db








def main():

    # init the application.
    # 
    # # init the database.
    # init_database()




"""
