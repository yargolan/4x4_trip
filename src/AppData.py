
import os
import json


class AppData(object):

    # Set the root folder.
    root_folder   = os.path.realpath(f"{os.path.dirname(os.path.realpath(__file__))}/..")
    sleep_interval = 3


    # Read the application config file.
    with open(f"{root_folder}/config/app_config.json") as ac:
        config_data = json.load(ac)


    # Read the database config file.
    with open(f"{root_folder}/config/db_config.json") as dbc:
        db_data = json.load(dbc)


    # Set the root folder.
    root_folder = os.path.realpath(f"{os.path.dirname(os.path.realpath(__file__))}/..")
    initial_data_file = "/".join([root_folder, "config", config_data['initial_data_file']])


    new_requests_dir     = config_data['requests']['new_requests_dir']
    handled_requests_dir = config_data['requests']['handled_requests_dir']
    stop_scanning_file   = config_data['stop_scanning_file']

    # DB related
    client     = db_data['client']
    db_name    = db_data['database_name']
    allow_drop = db_data['drop_db_allowed']

    col_name_vehicles     = db_data['col_vehicles']
    col_name_participants = db_data['col_participants']
