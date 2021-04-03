
import os
import re
import sys
import json
import Logger
import sqlite3
import RequestsHandler
from AppData import AppData



def init_db():

    if AppData.allow_drop:
        if os.path.exists(AppData.database_file_full_path):
            Logger.info("Deleting the DB.")
            os.unlink(AppData.database_file_full_path)
        else:
            Logger.warn("The DB doesn't exist yet.")

    if os.path.exists(AppData.database_file_full_path):
        Logger.info("The database already exists.")
    else:
        Logger.info("Creating the 'vehicles' entries.")
        init_db_vehicles()
        Logger.info("OK.")
        Logger.info("")

        Logger.info("Creating the 'participants' entries.")
        init_db_participants()
        Logger.info("OK.")
        Logger.info("")



def init_db_vehicles():

    connection = sqlite3.connect(AppData.database_file_full_path)

    # Set the DB structure
    sql_command = "CREATE TABLE {} ({} INT PRIMARY KEY NOT NULL, {} INT NOT NULL, {} TEXT NOT NULL, {} TEXT NOT NULL);".format(
        AppData.table_name_vehicles,
        AppData.col_vehicles_id,
        AppData.col_vehicles_make_index,
        AppData.col_vehicles_make,
        AppData.col_vehicles_model
    )

    if AppData.debug_mode:
        print(sql_command)
    connection.execute(sql_command)


    # Add the initial data
    with open(AppData.initial_data_file) as i:
        initial_data = json.load(i)

    vehicles_list = initial_data.get('vehicles')
    for vehicle in vehicles_list:
        make_name   = vehicle.get('make')
        make_index  = vehicle.get('index')
        models_list = vehicle.get('models')

        for model in models_list:
            model_name  = model.get('name')
            model_index = model.get('index')
            sql_command = "INSERT INTO {} ({}, {}, {}, {}) VALUES ('{}', '{}', '{}', '{}')".format(
                AppData.table_name_vehicles,
                AppData.col_vehicles_id,
                AppData.col_vehicles_make_index,
                AppData.col_vehicles_make,
                AppData.col_vehicles_model,
                model_index,
                make_index,
                make_name,
                model_name
            )

            if AppData.debug_mode:
                print(sql_command)
            connection.execute(sql_command)

    connection.commit()
    connection.close()



def init_db_participants():

    connection = sqlite3.connect(AppData.database_file_full_path)

    # Set the DB structure.
    sql_command = "CREATE TABLE {} ({} TEXT PRIMARY KEY NOT NULL, {} TEXT NOT NULL, {} TEXT NOT NULL);".format(
        AppData.table_name_participants,
        AppData.col_participant_name,
        AppData.col_participant_email,
        AppData.col_participant_vehicle_index
    )


    if AppData.debug_mode:
        print(sql_command)
    connection.execute(sql_command)


    # Add the initial data
    with open(AppData.initial_data_file) as i:
        initial_data = json.load(i)

    participant_list = initial_data.get('participants')
    for participant in participant_list:

        sql_command = "INSERT INTO {} ({}, {}, {}) VALUES ('{}', '{}', '{}')".format(
            AppData.table_name_participants,
            AppData.col_participant_name,
            AppData.col_participant_email,
            AppData.col_participant_vehicle_index,
            participant.get('name'),
            participant.get('email'),
            participant.get('vehicle_index')
        )

        if AppData.debug_mode:
            print(sql_command)
        connection.execute(sql_command)

    connection.commit()
    connection.close()




def main():

    # Set the initial data into the DB.
    init_db()


    # Go over the requests folder content.
    with os.scandir(AppData.requests_dir_full_path) as entries:
        for entry in entries:
            try:
                handle_current_entry(entry.name, entry.path)
            except Exception as e:
                sys.exit(e)



def handle_current_entry(request_file_name, request_file_full_path):

    # Ignore the already handled folder.
    if os.path.isdir(request_file_full_path):
        return


    # If the file is with the needed format, handle it.
    regex = re.search(AppData.request_regex, request_file_name)
    if regex is None:
        Logger.info(f"Invalid file name ({request_file_name}), deleting...")
        os.unlink(request_file_full_path)
        return


    Logger.debug(f"Handling request '{request_file_name}'")

    try:
        RequestsHandler.handle_request(request_file_full_path)

        # Move the request to backup
        os.rename(request_file_full_path, f"{AppData.handled_requests_full_path}/{request_file_name}")

    except KeyError as ke:

        # Delete the request file
        os.unlink(request_file_full_path)

        raise Exception(f"Invalid request file. Missing key: {str(ke)}")




if __name__ == '__main__':
    main()
