
import sys
import json
import pymongo



def main(arguments):
    if len(arguments) == 1:
        print()
        print("1. Participants")
        print("2. Vehicles")
        index = input("Which query to run ? ")
    else:
        index = arguments[1]

    run_query(index)



def run_query(query_index):

    print()

    # Read the DB properties


if __name__ == '__main__':
    main(sys.argv)





"""


db_config = {}




    mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")

    with open('../config/db_config.json') as db:
        db_config = json.load(db)

    db_name = db_config['databases']['name']

    my_db = mongo_client[db_name]

    col_vehicles = my_db["Vehicles"]

    for x in col_vehicles.find():
        print(x)


import json
import pymongo


db_config = {}


if __name__ == '__main__':

    mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")

    with open('../config/db_config.json') as db:
        db_config = json.load(db)

    db_name = db_config['databases']['name']

    my_db = mongo_client[db_name]

    col_participants = my_db["Participants"]

    for x in col_participants.find():
        print(x)
"""
