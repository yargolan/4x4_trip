
import json



class AppData(object):

    with open("../config/app_config.json") as ac:
        config_data = json.load(ac)

    # DB related configuration
    cfg_db_name     = config_data['db']['database_name']
    cfg_client_name = config_data['db']['client']


    # Application related configuration
    cfg_debug = (config_data['app']['debug'] == "True")
