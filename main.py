import sys

from network_security.compontents.data_ingestion import DataIngestion
from network_security.compontents.data_validation import DataValidation
from network_security.compontents.data_transformation import DataTransformation
from network_security.compontents.model_trainer import ModelTrainer

from network_security.logging import logger
from network_security.exception_handling.exception import SecurityException
from network_security.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from network_security.entity.config_entity import TrainingPipelineConfig,ModelTrainingConfig

from network_security.utils.utils import generate_schema_yaml

# generate schema file from base csv file
generate_schema_yaml('data/phisingData.csv')

if __name__ == "__main__":
    try:
        training_pipeline_config = TrainingPipelineConfig()
        #data ingestion
        data_ingestion_config = DataIngestionConfig(training_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config)
        logger.logging.info("Data Ingestion started...")
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        logger.logging.info("Data Ingestion completed...")

        # data validation
        logger.logging.info("Data validation initiated...")

        data_validation_config = DataValidationConfig(training_pipeline_config)
        data_validation = DataValidation(data_validation_config=data_validation_config,data_ingestion_artifact=data_ingestion_artifact)
        data_validation_artifact = data_validation.initiate_data_validation()

        logger.logging.info("Data Validation completed...")

        #data transformation
        logger.logging.info("Data Transformation started...")
        data_transformation_config = DataTransformationConfig(training_pipeline_config)
        data_transformation = DataTransformation(data_validation_artifact=data_validation_artifact,
                                                 data_transformation_config=data_transformation_config)
        data_transformation_artifact = data_transformation.initiated_data_transformation()
        logger.logging.info("Data Transformation completed...")

        logger.logging.info("Model training started...")
        model_trainer_config = ModelTrainingConfig(training_pipeline_config)
        model_trainer = ModelTrainer(model_trainer_config=model_trainer_config,data_transforming_artifact=data_transformation_artifact)
        model_trainer.initialize_model_trainer()
        logger.logging.info("Model training completed...")

    except Exception as e:
        raise SecurityException(e,sys)
