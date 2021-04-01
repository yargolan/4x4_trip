
import os
import re
import time
from AppData import AppData
import Logger



def main():

    keep_scanning = True

    new_requests_dir = AppData.new_requests_dir

    os.chdir("..")

    while keep_scanning:

        # sleep for 'x' seconds between iterations.
        if AppData.debug_mode:
            Logger.debug(f"Sleeping for {AppData.sleep_interval} seconds ...")
        time.sleep(AppData.sleep_interval)


        # Get the folder's content
        content = os.listdir(new_requests_dir)
        if AppData.debug_mode:
            if content is None:
                Logger.debug("Nothing to handle.")

        for item in content:

            # Get the full path of the request file.
            item_full_path = f"{new_requests_dir}/{item}"


            # Handle only files.
            if not os.path.isfile(item_full_path):
                continue


            # Verify if the scan should be stopped.
            if item == AppData.stop_scanning_file:
                os.unlink(item_full_path)
                Logger.info("Shutting down requests scanning process...")
                Logger.info("OK.")
                Logger.info("")
                keep_scanning = False
                continue

            # Handle the request file.
            handle_request(item, item_full_path)



def handle_request(item, item_full_path):

    Logger.info(f"Handling request file '{item_full_path}'.")

    regex = re.search("^user_request_.*.json$", item)

    if regex is not None:
        Logger.info(f"Invalid file ({item}), deleting...")
        os.unlink(item_full_path)





if __name__ == '__main__':
    main()
