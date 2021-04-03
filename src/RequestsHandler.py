
import json
import sqlite3
from AppData import AppData
from Actions import Actions
from src import Logger


def handle_request(request):
    with open(request) as r:
        content = json.load(r)

    data   = content['data']
    action = content['action']

    if action == Actions.action_user_add:
        action_user_add(data)
        Logger.info("OK.")
        Logger.info("")
    elif action == Actions.action_user_del:
        action_user_del(data)
        Logger.info("OK.")
        Logger.info("")
    elif action == Actions.action_user_edit:
        print(data)
    elif action == Actions.action_vehicle_add:
        print(data)
    elif action == Actions.action_vehicle_del:
        print(data)
    elif action == Actions.action_vehicle_edit:
        print(data)
    else:
        raise Exception(f"The action '{action}' is invalid.")



def is_user_exists(data):
    is_exists = False

    connection = sqlite3.connect(AppData.database_file_full_path)

    sql_query = "SELECT * FROM {}".format(AppData.table_name_participants)

    cursor = connection.execute(sql_query)

    for row in cursor:
        if row[0] == data.get('name'):
            is_exists = True
            break

    return is_exists



def action_user_add(data):

    result = is_user_exists(data)

    if result:
        Logger.info(f"the user '{data.get('name')}' already exists in the database.")
        return

    connection = sqlite3.connect(AppData.database_file_full_path)

    sql_command = "INSERT INTO {} ({}, {}, {}) VALUES ('{}', '{}', '{}')".format(
        AppData.table_name_participants,
        AppData.col_participant_name,
        AppData.col_participant_email,
        AppData.col_participant_vehicle_index,
        data.get('name'),
        data.get('email'),
        data.get('vehicle_index')
    )

    if AppData.debug_mode:
        print(sql_command)

    connection.execute(sql_command)

    connection.commit()

    connection.close()



def action_user_del(data):

    result = is_user_exists(data)

    if not result:
        Logger.info(f"the user '{data.get('name')}' does not exist in the database.")
        return

    connection = sqlite3.connect(AppData.database_file_full_path)

    sql_command = "DELETE FROM {} WHERE {} = '{}'".format(
        AppData.table_name_participants,
        AppData.col_participant_name,
        data.get('name')
    )

    if AppData.debug_mode:
        print(sql_command)

    connection.execute(sql_command)

    connection.commit()

    connection.close()

