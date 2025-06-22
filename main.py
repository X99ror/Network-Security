from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.entity.config_entity import DataValidationConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys


if __name__=='__main__':
    try:
        training_pipeline=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(training_pipeline)
        data_ingestion= DataIngestion(dataingestionconfig)
        logging.info("Initiating the data ingestion")
        data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation Completed")
        print(data_ingestion_artifact)
        data_validation_config=DataValidationConfig(training_pipeline)
        data_validation=DataValidation(
            data_ingestion_artifact=data_ingestion_artifact,
            data_validation_config=data_validation_config
            )
        
        logging.info("Initiating the data validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("Data validation Complete")
        
    except Exception as e:
        raise NetworkSecurityException(e,sys)

