
import pymongo
from src import Logger
from src.AppData import AppData
from pprint import pprint



client       = pymongo.MongoClient(AppData.client)
my_db        = client[AppData.db_name]
col_vehicles = my_db[AppData.col_name_vehicles]



def add(data):
    if is_exists(data['make'], data['model']):
        Logger.debug(f"The vehicle '{data['make']}' already exists in the DB.")
    else:
        index = get_next_index()
        print(index)
        # col_vehicles.insert_one(data)



def get_makes():

    makes = {}

    all_data = col_vehicles.find()

    for line in all_data:

        # Get the current index
        print(line)











def get_next_index():

    all_data = col_vehicles.find()

    max_index = 0
    for line in all_data:
        if int(line['index']) > max_index:
            max_index = int(line['index'])

    return max_index



def delete(data):
    if is_exists(data['make'], data['model']):
        col_vehicles.delete_one(data)
    else:
        Logger.debug(f"The vehicle '{data['make']}/{data['model']}' does not exist in the DB.")



def edit(data):
    if is_exists(data['make'], data['model']):
        old_data = {"make": data['make'], "model": data['model'], "vehicle_index": data['vehicle_index']}
        delete(old_data)

    # Now add the new details.
    new_data = {"make": data['new_make'], "model": data['new_model'], "vehicle_index": data['new_vehicle_index']}
    add(new_data)



def is_exists(make, model):
    data = {"make": make, "model": model}
    result = col_vehicles.find_one(data)
    return result is not None
