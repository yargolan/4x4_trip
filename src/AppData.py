
import json


class AppData(object):

    # Read the application config file.
    with open("../config/app_config.json") as ac:
        config_data = json.load(ac)


    # Read the database config file.
    with open("../config/db_config.json") as dbc:
        db_data = json.load(dbc)


    new_requests_dir     = config_data['requests']['new_requests_dir']
    handled_requests_dir = config_data['requests']['handled_requests_dir']
    stop_scanning_file   = config_data['stop_scanning_file']

    # DB related
    client     = db_data['client']
    db_name    = db_data['database_name']
    allow_drop = db_data['drop_db_allowed']
