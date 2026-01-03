import pandas as pd
import numpy as np
import sys,os
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline

from network_security.constant.training_pipeline import TARGET_COLUMN_NAME, DATA_TRANSFORMATION_KNN_IMPUTER_PARAMS
from network_security.logging import logger
from network_security.exception_handling.exception import SecurityException
from network_security.entity.artifact_entity import DataValidationArtifact ,DataTransformingArtifact
from network_security.entity.config_entity import DataTransformationConfig,TrainingPipelineConfig
from network_security.utils.utils import *


class DataTransformation:
    def __init__(self,data_transformation_config:DataTransformationConfig, data_validation_artifact:DataValidationArtifact):
        try:
            self.data_transformation_config = data_transformation_config
            self.data_validation_artifact = data_validation_artifact

            self.validated_train_file_path = self.data_validation_artifact.valid_train_file_path
            self.validated_test_file_path = self.data_validation_artifact.valid_test_file_path

        except Exception as e:
            raise SecurityException(e,sys)

    def get_transformed_object(self,):
        try:
            logger.logging.info("Imputer object started...")
            knn_imputer = KNNImputer(**DATA_TRANSFORMATION_KNN_IMPUTER_PARAMS)
            return knn_imputer
        except Exception as e:
            raise SecurityException(e,sys)

    def initiated_data_transformation(self):
        try:
            train_df = pd.read_csv(self.validated_train_file_path)
            test_df = pd.read_csv(self.validated_test_file_path)

            ## seprating target and input features for training data
            train_input_df = train_df.drop(columns=[TARGET_COLUMN_NAME])
            train_target_df = train_df[TARGET_COLUMN_NAME].replace(-1,0)

            ## seprating target and input feature for testing data
            test_input_df = test_df.drop(columns=[TARGET_COLUMN_NAME])
            test_target_df = test_df[TARGET_COLUMN_NAME].replace(-1,0)

            preprocessor = self.get_transformed_object()
            preprocessed_train_input = preprocessor.fit_transform(train_input_df)
            preprocessed_test_input = preprocessor.transform(test_input_df)

            preprocessed_train_np = np.c_[preprocessed_train_input, np.array(train_target_df)]
            preprocessed_test_np = np.c_[preprocessed_test_input, np.array(test_target_df)]

            save_file_as_np(self.data_transformation_config.transformed_train_file_path,preprocessed_train_np)
            save_file_as_np(self.data_transformation_config.transformed_test_file_path,preprocessed_test_np)

            save_pkl_file(self.data_transformation_config.transformed_objects_file_path,preprocessor)

            artifact = DataTransformingArtifact(
                transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
                transformed_test_file_path=self.data_transformation_config.transformed_test_file_path,
                transformation_object_file_path=self.data_transformation_config.transformed_objects_file_path,
            )

            return artifact

        except Exception as e:
            raise SecurityException(e,sys)