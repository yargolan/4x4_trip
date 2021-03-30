
import os
import json
import pymongo
from src.AppData import AppData



def set_initial_data():

    # Set the root folder.
    root_folder = os.path.realpath(f"{os.path.dirname(os.path.realpath(__file__))}/../..")


    # Read the initial data file.
    with open(f"{root_folder}/config/initial_data.json") as i:
        initial_data = json.load(i)


    # Set the Mongo client
    client = pymongo.MongoClient(AppData.client)
    my_db  = client[AppData.db_name]
    col_vehicles = my_db[AppData.col_name_vehicles]


    # Read the list of vehicles
    all_vehicles = initial_data.get(AppData.col_name_vehicles)

    for make_and_model in all_vehicles:

        # Get the make name.
        make = make_and_model.get('make')

        # Get the models dict.
        models_dict = make_and_model.get('models')

        for model in models_dict:
            model_name  = model.get('name')
            model_index = model.get('index')

            data = {"index": model_index, "make": make, "name": model_name}

            col_vehicles.insert_one(data)


    # Insert the list of participants
    all_participants = initial_data.get(AppData.col_name_participants)

    col_participants = my_db[AppData.col_name_participants]

    for p in all_participants:

        col_participants.insert_one(p)



def drop_tables():

    # Set the Mongo client
    client = pymongo.MongoClient(AppData.client)
    my_db  = client[AppData.db_name]
    cols = my_db.list_collection_names()
    for col in cols:
        my_db.drop_collection(col)
