#!/usr/bin/python

import os
import re
import time
import json
from src import Random, ActionsUser, Logger
from AppData import AppData
from Hardcoded import Hardcoded
from src.db import init_db



def verify_folders():

    os.chdir("..")

    if not os.path.isdir(AppData.new_requests_dir):
        Logger.info("Create the 'requests' folder")
        os.mkdir(AppData.new_requests_dir)

    if not os.path.isdir(AppData.handled_requests_dir):
        Logger.info("Create the 'requests/.handled' folder")
        os.mkdir(AppData.handled_requests_dir)



def scan_requests_dir():

    keep_scanning = True

    new_requests_dir = AppData.new_requests_dir

    while keep_scanning:

        # sleep for 'x' seconds between iterations.
        time.sleep(AppData.sleep_interval)


        # Get the folder's content
        content = os.listdir(new_requests_dir)

        for item in content:

            item_full_path = f"{new_requests_dir}/{item}"

            # Handle only files.
            if os.path.isfile(item_full_path):

                # Verify if the scan should be stopped.
                if item == AppData.stop_scanning_file:
                    os.unlink(item_full_path)
                    Logger.info("Shutting down requests scanning process...")
                    Logger.info("OK.")
                    Logger.info("")
                    keep_scanning = False
                else:

                    # Verify if we need to process a request.
                    regex = re.search("^user_request_.*.json$", item)
                    if regex is not None:
                        process_user_requests(item, item_full_path)
                    else:
                        Logger.info(f"Invalid file ({item}), deleting...")
                        os.unlink(item_full_path)



def process_user_requests(user_request_file, user_request_file_full_path):

    Logger.info(f"Handling user request '{user_request_file}'")

    # Read the request.
    with open(user_request_file_full_path) as r:
        request = json.load(r)


    # Validate the request.
    try:
        action = request['action']
    except KeyError:
        Logger.error(" - The request file is invalid.")
        Logger.error(" - Missing 'action' key")
        os.unlink(user_request_file_full_path)
        return


    try:
        if action == Hardcoded.action_user_add:
            ActionsUser.user_add(request['data'])
        elif action == Hardcoded.action_user_del:
            ActionsUser.user_del(request['data'])
        elif action == Hardcoded.action_user_edit:
            ActionsUser.user_edit(request['data'])
        else:
            Logger.error(f"Error: Invalid action ({action}).")
            return

    except KeyError as ke:
        Logger.error(f"Error running the '{action}' action: " + str(ke))


    # Move the request into the 'handled' folder.
    random_string = Random.generate_random_string(20)

    os.rename(user_request_file_full_path, f"{AppData.handled_requests_dir}/{random_string}")

    Logger.info("OK.")
    Logger.info("")



def verify_database():
    if AppData.allow_drop is True:
        Logger.debug("Dropping the current DB.")
        init_db.drop_tables()
        Logger.debug("ok.")

        Logger.debug("Create the DB.")
        init_db.set_initial_data()
        Logger.debug("ok.")



def init_app():

    # Verify folders.
    verify_folders()

    # Verify database.
    verify_database()



def main():

    # Init the app
    init_app()

    # Scan the new requests folder until we find a sign to break
    scan_requests_dir()



if __name__ == '__main__':
    main()
