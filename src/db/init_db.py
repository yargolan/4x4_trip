
import json



# Insert the data into the DB.
db_name = "4wd_trips_database"


def set_initial_data(client):

    with open("../data/initial_data.json") as v:
        initial_data = json.load(v)

    # Insert the list of vehicles
    all_vehicles = initial_data.get('vehicles')
    set_vehicles(client, all_vehicles)

    # Insert the list of participants
    all_participants = initial_data.get('participants')
    set_participants(client, all_participants)



def set_participants(client, all_participants):

    for p in all_participants:

        my_db = client[db_name]

        col_participants = my_db['Participants']

        col_participants.insert_one(p)


def set_vehicles(client, all_vehicles):

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
