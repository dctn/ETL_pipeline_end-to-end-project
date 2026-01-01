import pandas as pd
from scipy.stats import ks_2samp
from network_security.logging import logger
from network_security.exception_handling.exception import SecurityException
from network_security.entity.config_entity import DataValidationConfig
from network_security.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from network_security.constant.training_pipeline import DATA_SCHEMA_FILE_PATH
from network_security.utils.utils import *
import sys,os



class DataValidation:
    def __init__(self,data_validation_config: DataValidationConfig,data_ingestion_artifact: DataIngestionArtifact):
        try:
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact
            self.schema_config  = read_yaml_file(DATA_SCHEMA_FILE_PATH)
        except Exception as e:
            raise SecurityException(e,sys)

    def validate_no_of_columns(self,df: pd.DataFrame)->bool:
        try:
            number_of_columns = len(self.schema_config['columns'])
            logger.logging.info(f"Number of columns needed : {number_of_columns}")
            logger.logging.info(f"Number of columns has : {len(df.columns)}")
            if number_of_columns == len(df.columns):
                return True
            else:
                return False

        except Exception as e:
            raise SecurityException(e,sys)

    def detect_data_drift(self,base_df, current_df, threshold=0.05)->bool:
        try:
            drift_report = {}
            for columns in base_df.columns:
                base_col = base_df[columns]
                current_col = current_df[columns]
                sample_distribution_distance = ks_2samp(base_col,current_col)
                if threshold <= sample_distribution_distance.pvalue:
                    is_found = False
                    status = False
                else:
                    is_found = True
                    status = True
                drift_report.update(
                    {columns: {
                        "is_found": is_found,
                        "sample_distribution_distance": float(sample_distribution_distance.pvalue),
                    }}
                )

            drift_report_dir = os.path.dirname(self.data_validation_config.data_validation_drift_report_file)
            os.makedirs(drift_report_dir, exist_ok=True)
            write_yaml_file(self.data_validation_config.data_validation_drift_report_file, drift_report)
            return status
        except Exception as e:
            raise SecurityException(e,sys)

    def initiate_data_validation(self)-> DataValidationArtifact:
        try:
            train_file_path = self.data_ingestion_artifact.trained_file_path
            test_file_path = self.data_ingestion_artifact.testing_file_path

            # get file in DataFrame
            train_df =read_file_to_df(train_file_path)
            test_df =read_file_to_df(test_file_path)

            #validate no of columns
            train_status = self.validate_no_of_columns(train_df)
            test_status = self.validate_no_of_columns(test_df)

            if train_status:
                error_msg = f"Train df does not have enough columns : {len(train_df.columns)}"
            elif test_status:
                error_msg = f"Test df does not have enough columns : {len(test_df.columns)}"

            ## checking for data drift
            is_data_drift = self.detect_data_drift(train_df, test_df)

            if not is_data_drift:
                valid_file_dir = os.path.dirname(self.data_validation_config.data_validation_valid_train_file)
                os.makedirs(valid_file_dir, exist_ok=True)
                train_df.to_csv(self.data_validation_config.data_validation_valid_train_file, index=False)
                test_df.to_csv(self.data_validation_config.data_validation_valid_test_file, index=False)
            else:
                invalid_file_dir = os.path.dirname(self.data_validation_config.data_validation_invalid_test_file)
                os.makedirs(invalid_file_dir, exist_ok=True)
                train_df.to_csv(self.data_validation_config.data_validation_invalid_test_file, index=False)
                test_df.to_csv(self.data_validation_config.data_validation_invalid_train_file, index=False)

            data_validation_artifact = DataValidationArtifact(
                validation_status=is_data_drift,
                valid_train_file_path=self.data_validation_config.data_validation_valid_train_file,
                valid_test_file_path=self.data_validation_config.data_validation_valid_test_file,
                invalid_train_file_path=self.data_validation_config.data_validation_invalid_train_file,
                invalid_test_file_path=self.data_validation_config.data_validation_invalid_test_file,
                drift_file_report_path=self.data_validation_config.data_validation_drift_report_file,
            )
            return data_validation_artifact
        except Exception as e:
            raise SecurityException(e,sys)
