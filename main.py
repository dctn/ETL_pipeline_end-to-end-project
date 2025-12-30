import sys

from network_security.compontents.data_ingestion import DataIngestion
from network_security.logging import logger
from network_security.exception_handling.exception import SecurityException
from network_security.entity.config_entity import DataIngestionConfig
from network_security.entity.config_entity import TrainingPipelineConfig

if __name__ == "__main__":
    try:
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config)
        logger.logging.info("Data Ingestion started...")
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        logger.logging.info("Data Ingestion completed...")
    except Exception as e:
        raise SecurityException(e,sys)
