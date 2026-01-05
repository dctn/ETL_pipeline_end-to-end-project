import os

from network_security.constant import training_pipeline
from datetime import datetime


class TrainingPipelineConfig:
    def __init__(self):
        timestamp = datetime.now().strftime("%d_%m_%y_%H_%M_%S")
        self.pipeline_name = training_pipeline.PIPELINE_NAME
        self.artifact_name = training_pipeline.ARTIFACT_DIR
        self.artifact_dir = os.path.join(self.artifact_name, timestamp)
        self.timestamp = timestamp


class DataIngestionConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.data_ingestion_dir: str = os.path.join(
            training_pipeline_config.artifact_dir,
            training_pipeline.DATA_INGESTION_DIR_NAME
        )

        self.feature_stored_file_path: str = os.path.join(
            self.data_ingestion_dir,
            training_pipeline.DATA_INGESTION_FEATURE_STORED_DIR,
            training_pipeline.FILE_NAME
        )

        self.training_file_path: str = os.path.join(
            self.data_ingestion_dir,
            training_pipeline.DATA_INGESTION_INGESTED_DIR,
            training_pipeline.TRAIN_FILE_NAME
        )

        self.test_file_path: str = os.path.join(
            self.data_ingestion_dir,
            training_pipeline.DATA_INGESTION_INGESTED_DIR,
            training_pipeline.TEST_FILE_NAME
        )

        self.database_name = training_pipeline.DATA_INGESTION_DATABASE_NAME
        self.collection_name = training_pipeline.DATA_INGESTION_COLLECTION_NAME
        self.train_test_split_ratio: float = training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO


class DataValidationConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        # base data validation dir path
        self.data_validation_dir: str = os.path.join(training_pipeline_config.artifact_dir,
                                                     training_pipeline.DATA_VALIDATION_DIR_NAME)

        # valid dir inside base dir
        self.data_validation_valid_dir: str = os.path.join(
            self.data_validation_dir, training_pipeline.DATA_VALIDATION_VALID_DIR
        )
        ## valid train and test file inside valid dir
        self.data_validation_valid_train_file = os.path.join(self.data_validation_valid_dir,
                                                             training_pipeline.TRAIN_FILE_NAME)

        self.data_validation_valid_test_file = os.path.join(self.data_validation_valid_dir,
                                                             training_pipeline.TEST_FILE_NAME)

        # invalid dir inside base dir
        self.data_validation_invalid_dir: str = os.path.join(self.data_validation_valid_dir,
                                                             training_pipeline.DATA_VALIDATION_INVALID_DIR)

        ## invalid train and test file inside invalid dir
        self.data_validation_invalid_train_file = os.path.join(self.data_validation_invalid_dir, training_pipeline.TRAIN_FILE_NAME)
        self.data_validation_invalid_test_file = os.path.join(self.data_validation_invalid_dir, training_pipeline.TEST_FILE_NAME)

        # final report dir
        self.data_validation_drift_report_dir: str = os.path.join(
            self.data_validation_dir, training_pipeline.DATA_VALIDATION_DRIFT_REPORT_DIR
        )

        # final report file
        self.data_validation_drift_report_file: str = os.path.join(self.data_validation_drift_report_dir,
                                                                   training_pipeline.DATA_VALIDATION_DRIFT_REPORT_FILE_NAME)


class DataTransformationConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.data_transformation_dir: str = os.path.join(
            training_pipeline_config.artifact_dir,training_pipeline.DATA_TRANSFORMATION_DIR_NAME
        )

        self.data_transformed_dir: str = os.path.join(
            self.data_transformation_dir,training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_DIR
        )

        self.data_transformed_objects_dir:str = os.path.join(
            self.data_transformation_dir, training_pipeline.DATA_TRANSFORMATION_OBJECTS_DIR
        )

        self.transformed_train_file_path: str = os.path.join(
            self.data_transformed_dir,training_pipeline.TRAIN_FILE_NAME.replace('csv','npy')
        )

        self.transformed_test_file_path: str = os.path.join(
            self.data_transformed_dir,training_pipeline.TEST_FILE_NAME.replace('csv','npy')
        )

        self.transformed_objects_file_path: str = os.path.join(
            self.data_transformed_objects_dir, training_pipeline.DATA_TRANSFORMATION_OBJECT_FILE_NAME
        )

class ModelTrainingConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.model_training_dir:str = os.path.join(
            training_pipeline_config.artifact_dir,training_pipeline.MODEL_TRAINER_DIR_NAME
        )

        self.model_trained_dir:str = os.path.join(
            self.model_training_dir, training_pipeline.MODEL_TRAINER_DIR_NAME
        )

        self.model_trained_file_path: str = os.path.join(
            self.model_trained_dir,training_pipeline.MODEL_TRAINED_NAME_FILE_NAME
        )

        self.model_expected_accuracy = training_pipeline.MODEL_TRAINED_EXPECTED_SCORE

        self.model_trainer_overfitting_threshold = training_pipeline.MODEL_TRAINED_OVERFITTING_THRESHOLD













