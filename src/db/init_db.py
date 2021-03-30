
import json
import pymongo
from src.AppData import AppData


def set_initial_data():

    # Read the initial data file.
    with open("../config/initial_data.json") as v:
        initial_data = json.load(v)


    # Set the Mongo client
    client = pymongo.MongoClient(AppData.client)
    my_db  = client[AppData.db_name]


    # Insert the list of vehicles
    all_vehicles = initial_data.get('vehicles')

    for make_and_model in all_vehicles:

        # Get the make name.
        make = make_and_model.get('make')

        # Get the models dict.
        models_dict = make_and_model.get('models')

        for model in models_dict:
            model_name  = model.get('name')
            model_index = model.get('index')

            data = {"index": model_index, "make": make, "name": model_name}

            col_vehicles = my_db['Vehicles']

            col_vehicles.insert_one(data)




def set_initial_data_old():

    with open("../config/initial_data.json") as v:
        initial_data = json.load(v)


    # Set the Mongo client
    client = pymongo.MongoClient(AppData.client)
    my_db  = client[AppData.db_name]


    # Insert the list of vehicles
    all_vehicles = initial_data.get('vehicles')

    for make_and_model in all_vehicles:

        # Get the make name.
        make = make_and_model.get('make')

        # Get the models dict.
        models_dict = make_and_model.get('models')

        for model in models_dict:
            model_name  = model.get('name')
            model_index = model.get('index')

            data = {"index": model_index, "make": make, "name": model_name}

            col_vehicles = my_db['Vehicles']

            col_vehicles.insert_one(data)


    # Insert the list of participants
    all_participants = initial_data.get('participants')

    for p in all_participants:

        col_participants = my_db['Participants']

        col_participants.insert_one(p)
