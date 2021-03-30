
import json



# Insert the data into the DB.
db_name = ""


def set_initial_data(client):

    # Get the DB name
    with open("../config/db_config.json") as dbc:
        db_config = json.load(dbc)
        global db_name
        db_name = db_config['database_name']

    with open("../config/initial_data.json") as v:
        initial_data = json.load(v)

    # Insert the list of vehicles
    all_vehicles = initial_data.get('vehicles')
    set_vehicles(client, db_name, all_vehicles)

    # Insert the list of participants
    all_participants = initial_data.get('participants')
    set_participants(client, db_name, all_participants)



def set_participants(client, db_name, all_participants):

    for p in all_participants:

        my_db = client[db_name]

        col_participants = my_db['Participants']

        col_participants.insert_one(p)


def set_vehicles(client, db_name, all_vehicles):

    for make_and_model in all_vehicles:

        # Get the make name.
        make = make_and_model.get('make')

        # Get the models dict.
        models_dict = make_and_model.get('models')
        for model in models_dict:
            model_name  = model.get('name')
            model_index = model.get('index')

            data = {"index": model_index, "make": make, "name": model_name}

            my_db = client[db_name]

            col_vehicles = my_db['Vehicles']

            col_vehicles.insert_one(data)
