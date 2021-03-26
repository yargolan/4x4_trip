
import sys
import pymongo
from AppData import AppData



def main(arguments):
    if len(arguments) == 1:
        print()
        print("1. Participants")
        print("2. Vehicles")
        index = input("Which query to run ? ")
    else:
        index = arguments[1]

    run_query(index)



def run_query(query_index):

    print()

    if query_index == "1":
        relevant_column = "Participants"
    elif query_index == "2":
        relevant_column = "Vehicles"
    else:
        sys.exit("Invalid query")


    client  = AppData.cfg_client_name

    db_name = AppData.cfg_db_name

    mongo_client = pymongo.MongoClient(client)

    my_db = mongo_client[db_name]

    data = my_db[relevant_column]

    for result in data.find():
        del result['_id']
        print(result)





if __name__ == '__main__':
    main(sys.argv)
