
import os
import re
import sys
import Logger
from AppData import AppData
import RequestsHandler



def main():

    # Get into the root folder.
    os.chdir(AppData.requests_dir_full_path)

    # Go over the requests folder content.
    with os.scandir(".") as entries:

        for entry in entries:
            entry_path = entry.path
            entry_name = entry.name
            try:
                handle_current_entry(entry_name, entry_path)
            except Exception as e:
                sys.exit(e)



def handle_current_entry(entry_name, entry_path):

    # Ignore the already handled folder.
    if os.path.isdir(entry_path):
        return


    # If the file is with the needed format, handle it.
    regex = re.search(AppData.request_regex, entry_name)
    if regex is None:
        Logger.info(f"Invalid file ({entry_name}), deleting...")
        os.unlink(entry_path)
        return


    Logger.debug(f"Handling request '{entry_name}'")
    request_full_path = "/".join([AppData.requests_dir_full_path, entry_name])

    try:
        RequestsHandler.handle_request(request_full_path)

    except KeyError as ke:

        # Delete the request file
        os.unlink(request_full_path)

        raise Exception(f"Invalid request file. Missing key: {str(ke)}")

    finally:

        # Move the request to backup
        os.rename(request_full_path, f"{AppData.handled_requests_dir_name}/{entry_name}")



if __name__ == '__main__':
    main()
