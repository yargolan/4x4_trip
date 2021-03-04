
import pymongo


if __name__ == '__main__':

    mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")

    db_name = "4wd_trips_database"

    my_db = mongo_client[db_name]

    col_participants = my_db["Participants"]

    for x in col_participants.find():
        print(x)
