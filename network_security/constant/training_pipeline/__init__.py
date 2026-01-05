
"""
Define some common constant variable for training pipeline
"""
import os
import numpy as np

TARGET_COLUMN_NAME:str = "Result"
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


"""
Data Transformation VAR with DATA_TRANSFORMATION
"""
DATA_TRANSFORMATION_DIR_NAME:str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DIR:str = "transformed"
DATA_TRANSFORMATION_OBJECTS_DIR:str = "transformed_objects"
DATA_TRANSFORMATION_OBJECT_FILE_NAME = "transformed_object.pkl"
DATA_TRANSFORMATION_KNN_IMPUTER_PARAMS:dict = {
    "missing_values":np.nan,
    "n_neighbors":4,
    "weights":"uniform",
}

"""
Model Training VAR with MODEL_TRAINER
"""
MODEL_TRAINER_DIR_NAME:str = "model_training"
MODEL_TRAINED_DIR:str = "trained"
MODEL_TRAINED_NAME_FILE_NAME:str = "trained_model.pkl"
MODEL_TRAINED_EXPECTED_SCORE:float = 0.6
MODEL_TRAINED_OVERFITTING_THRESHOLD:float = 0.2














