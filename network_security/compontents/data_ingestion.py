from network_security.exception_handling.exception import SecurityException
from network_security.logging import logger
import sys
from network_security.entity.config_entity import DataIngestionConfig
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import pymongo
from dotenv import load_dotenv
import os
from network_security.entity.artifact_entity import DataIngestionArtifact

load_dotenv()

client = pymongo.MongoClient(os.environ.get('MONGO_DB_URL'))

class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise SecurityException(e,sys)

    def export_collection_as_dataframe(self):
        """
        This method will export the data ingestion collection as a dataframe
        :return:
        """
        try:
            database_name = self.data_ingestion_config.database_name
            collection_name = self.data_ingestion_config.collection_name

            collection = client[database_name][collection_name]
            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns:
                df.drop(columns=["_id"], axis=1, inplace=True)

            df.replace({"na":np.nan}, inplace=True)
            return df
        except Exception as e:
            raise SecurityException(e, sys)

    def export_data_into_features_stored(self,df:pd.DataFrame):
        """
        This method will export the data ingestion collection as a dataframe
        :param df:
        :return:
        """
        try:
            features_stored_dir = os.path.dirname(self.data_ingestion_config.feature_stored_file_path)
            os.makedirs(features_stored_dir,exist_ok=True)

            df.to_csv(self.data_ingestion_config.feature_stored_file_path)
            return df
        except Exception as e:
            raise SecurityException(e,sys)

    def split_data_for_train_and_test(self,df:pd.DataFrame):
        try:
            logger.logging.info("Splitting data into train and test")
            split_ratio = self.data_ingestion_config.train_test_split_ratio

            train_set, test_set = train_test_split(df, test_size=split_ratio)

            dir_path = os.path.dirname(self.data_ingestion_config.training_file_path)
            print(dir_path)
            os.makedirs(dir_path, exist_ok=True)

            train_set.to_csv(self.data_ingestion_config.training_file_path)
            test_set.to_csv(self.data_ingestion_config.test_file_path)
            logger.logging.info("Train and Test split complete")

            return (train_set, test_set)
        except Exception as e:
            raise SecurityException(e,sys)

    def initiate_data_ingestion(self):
        try:
            df = self.export_collection_as_dataframe()
            df = self.export_data_into_features_stored(df)
            self.split_data_for_train_and_test(df)
            data_ingestion_artifact_config = DataIngestionArtifact(trained_file_path=self.data_ingestion_config.training_file_path,
                                                                   testing_file_path=self.data_ingestion_config.test_file_path)
            return data_ingestion_artifact_config
        except Exception as e:
            raise SecurityException(e,sys)

