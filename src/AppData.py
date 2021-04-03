
import os
import json


class AppData(object):

    # +------------------------------------
    # |  Hard coded information
    # +------------------------------------
    table_name     = "4x4_trips"
    request_regex  = "^user_request_\\d{8}_\\d{6}.json$"
    sleep_interval = 3


    # +------------------------------------
    # |  Set the root folder
    # +------------------------------------
    root_folder = os.path.realpath(f"{os.path.dirname(os.path.realpath(__file__))}/..")


    # +------------------------------------
    # |  Read the config files
    # +------------------------------------
    with open(f"{root_folder}/config/app_config.json") as ac:
        config_data = json.load(ac)

    debug_mode                 = config_data['debug_mode'].lower() == "true"
    requests_dir               = config_data['requests']['new_requests_dir']
    stop_scanning_file         = config_data['stop_scanning_file']
    handled_requests_dir_name  = config_data['requests']['handled_requests_dir']
    requests_dir_full_path     = f"{root_folder}/{requests_dir}"
    handled_requests_full_path = f"{requests_dir_full_path}/{handled_requests_dir_name}"

    with open(f"{root_folder}/config/db_config.json") as dbc:
        db_data = json.load(dbc)

    allow_drop              = db_data['drop_db_allowed'].lower == "true"
    database_dir            = db_data['database_dir']
    database_file           = db_data['database_file']
    table_name_vehicles     = db_data['table_name_vehicles']
    table_name_participants = db_data['table_name_participants']
    database_file_full_path = "/". join([root_folder, database_dir, database_file])

    # Vehicles
    col_vehicles_id         = db_data['col_vehicles_id']
    col_vehicles_make       = db_data['col_vehicles_make']
    col_vehicles_model      = db_data['col_vehicles_model']
    col_vehicles_make_index = db_data['col_vehicles_make_index']

    # Participants
    col_participant_name          = db_data['col_participant_name']
    col_participant_email         = db_data['col_participant_email']
    col_participant_vehicle_index = db_data['col_participant_vehicle_index']

    # +------------------------------------
    # |  Set the initial data file
    # +------------------------------------
    initial_data_file = "/".join([root_folder, "config", config_data['initial_data_file']])
