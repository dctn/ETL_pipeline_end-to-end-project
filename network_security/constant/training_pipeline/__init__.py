
"""
Define some common constant variable for training pipeline
"""
import os

TARGET_COLUMN_NAME:str = "result"
PIPELINE_NAME:str = "PHISING"
ARTIFACT_DIR:str = "artifacts"
FILE_NAME:str = "phisingData.csv"

TRAIN_FILE_NAME:str = "train.csv"
TEST_FILE_NAME:str = "test.csv"

DATA_SCHEMA_FILE_PATH:str = os.path.join('data_schema','schema.yaml')
"""
Data Ingestion VAR start with DATA_INGESTION
"""
DATA_INGESTION_DATABASE_NAME:str = "STRANGER"
DATA_INGESTION_COLLECTION_NAME:str = "PHISING"
DATA_INGESTION_DIR_NAME:str = "data_ingestion"
DATA_INGESTION_FEATURE_STORED_DIR:str = "feature_stored"
DATA_INGESTION_INGESTED_DIR:str = "features"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float = 0.2

"""
Data Validation VAR with DATA_VALIDATION
"""
DATA_VALIDATION_DIR_NAME:str = "data_validation"
DATA_VALIDATION_VALID_DIR:str = "validated"
DATA_VALIDATION_INVALID_DIR:str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR:str = "drift_reports"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME:str = "drift_report.yaml"






