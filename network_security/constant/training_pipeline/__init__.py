
"""
Define some common constant variable for training pipeline
"""
TARGET_COLUMN_NAME:str = "result"
PIPELINE_NAME:str = "PHISING"
ARTIFACT_DIR:str = "artifacts"
FILE_NAME:str = "phisingData.csv"

TRAIN_FILE_NAME:str = "train.csv"
TEST_FILE_NAME:str = "test.csv"

"""
Data Ingestion VAR start with DATA_INGESTION
"""
DATA_INGESTION_DATABASE_NAME:str = "STRANGER"
DATA_INGESTION_COLLECTION_NAME:str = "PHISING"
DATA_INGESTION_DIR_NAME:str = "data_ingestion"
DATA_INGESTION_FEATURE_STORED_DIR:str = "feature_stored"
DATA_INGESTION_INGESTED_DIR:str = "features"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float = 0.2