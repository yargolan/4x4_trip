
import json
import pymongo


db_config = {}


if __name__ == '__main__':

    mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")

    with open('../config/db_config.json') as db:
        db_config = json.load(db)

    db_name = db_config['databases']['name']

    my_db = mongo_client[db_name]

    col_vehicles = my_db["Vehicles"]

    for x in col_vehicles.find():
        print(x)

