import json

import pandas as pd
import pymongo
from network_security.logging import logger
from network_security.exception_handling.exception import SecurityException
import os
from dotenv import load_dotenv
import sys
load_dotenv()


def convert_csv_to_json(csv_file):
    try:
        logger.logging.info("starting to csv file to json")

        df = pd.read_csv(csv_file)
        record = list(json.loads(df.T.to_json()).values())

        logger.logging.info("csv file successfully converted to json")
        return record
    except Exception as e:
        raise SecurityException(e,sys)


class NetworkDataExtractor:
    def __init__(self):
        self.record = None
        self.collection = None
        self.database = None
        try:
            url = f"mongodb+srv://{os.environ.get('MONGO_DB_USERNAME')}:{os.environ.get('MONGO_DB_PASSWORD')}@cluster0.nlx3aur.mongodb.net/?appName=Cluster0"
            self.client = pymongo.MongoClient(url)
        except Exception as e:
            raise SecurityException(e,sys)

    def insert_data_to_db(self, record,database,collection):
        try:
            logger.logging.info("starting to insert data to db")
            self.database = database
            self.collection = collection
            self.record = record

            self.database = self.client[self.database]
            self.collection = self.database[self.collection]

            self.collection.insert_many(self.record)
            logger.logging.info("data inserted successfully to db")
        except Exception as e:
            raise SecurityException(e,sys)

if __name__ == "__main__":
    FILE_PATH = "data/phisingData.csv"
    DATABASE_NAME = "STRANGER"
    COLLECTION_NAME = "PHISING"

    data_extractor = NetworkDataExtractor()
    records = convert_csv_to_json(FILE_PATH)
    data_extractor.insert_data_to_db(records,DATABASE_NAME,COLLECTION_NAME)











