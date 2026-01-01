import sys

from network_security.compontents.data_ingestion import DataIngestion
from network_security.compontents.data_validation import DataValidation
from network_security.logging import logger
from network_security.exception_handling.exception import SecurityException
from network_security.entity.config_entity import DataIngestionConfig,DataValidationConfig
from network_security.entity.config_entity import TrainingPipelineConfig

from network_security.utils.utils import generate_schema_yaml

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
        logger.logging.info("Data validation started...")

        data_validation_config = DataValidationConfig(training_pipeline_config)
        data_validation = DataValidation(data_validation_config=data_validation_config,data_ingestion_artifact=data_ingestion_artifact)
        data_validation_artifact = data_validation.initiate_data_validation()

        logger.logging.info("Data Validation completed...")

    except Exception as e:
        raise SecurityException(e,sys)
