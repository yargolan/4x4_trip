#!/usr/bin/python

import os
import re
import time
import json
from src import Random
from AppData import AppData
from pprint import pprint




def verify_folders():

    os.chdir("..")

    if not os.path.isdir(AppData.new_requests_dir):
        os.mkdir(AppData.new_requests_dir)

    if not os.path.isdir(AppData.handled_requests_dir):
        os.mkdir(AppData.handled_requests_dir)


def scan_requests_dir():
    keep_scanning = True

    new_requests_dir = AppData.new_requests_dir

    while keep_scanning:

        # sleep for 5 seconds between iterations.
        time.sleep(5)


        content = os.listdir(new_requests_dir)

        for item in content:

            item_full_path = f"{new_requests_dir}/{item}"

            if os.path.isfile(item_full_path):

                # Verify if the scan should be stopped.
                if item == AppData.stop_scanning_file:
                    os.unlink(item_full_path)
                    keep_scanning = False
                    continue

                # Verify if we need to process a request.
                x = re.search("^user_request_.*.json$", item)
                if x is not None:
                    process_user_request(item, item_full_path)



def process_user_request(user_request_file, user_request_file_full_path):

    print(f"Handling user request '{user_request_file}' ...")

    # Read the request
    with open(user_request_file_full_path) as r:
        request = json.load(r)

    pprint(request)


    # Move the request into the 'handled' folder.
    random_string = Random.generate_random_string(20)

    os.rename(user_request_file_full_path, f"{AppData.handled_requests_dir}/{random_string}")



def main():
    # Verify folders.
    verify_folders()

    # Scan the new requests folder until we find a sign to break
    scan_requests_dir()


if __name__ == '__main__':
    main()
