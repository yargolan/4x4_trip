
import json


db_data  = {}
app_data = {}


class AppData(object):

    with open("../config/db_config.json") as dbc:
        db_data = json.load(dbc)

    with open("../config/config.json") as ac:
        app_data = json.load(ac)


    db_name     = db_data.get('client')
    client_name = db_data.get('database_name')


    debug = (app_data.get('debug') == "True")
