from networksecurity.components.data_ingestion import DataIngestion
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
        
        
    except Exception as e:
        raise NetworkSecurityException(e,sys)

