
import json


class AppData(object):

    # Read the application config file.
    with open("../config/app_config.json") as ac:
        config_data = json.load(ac)

    new_requests_dir     = config_data['requests']['new_requests_dir']
    handled_requests_dir = config_data['requests']['handled_requests_dir']
    stop_scanning_file   = config_data['stop_scanning_file']
