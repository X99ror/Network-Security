from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.entity.config_entity import DataValidationConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.entity.config_entity import DataTransformationConfig
from networksecurity.components.data_transformation import DataTranformation
from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.entity.config_entity import  ModelTrainerConfig
import sys


if __name__=='__main__':
    try:
        training_pipeline=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(training_pipeline)
        data_ingestion= DataIngestion(dataingestionconfig)
        logging.info("Initiating the data ingestion")
        data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Ingestion Completed")
        print(data_ingestion_artifact)
        data_validation_config=DataValidationConfig(training_pipeline)
        data_validation=DataValidation(
            data_ingestion_artifact=data_ingestion_artifact,
            data_validation_config=data_validation_config
            )
        
        logging.info("Initiating the data validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        print(data_validation_artifact)
        logging.info("Data validation Complete")
        data_transformation_config=DataTransformationConfig(training_pipeline)
        data_transformation=DataTranformation(
            data_transformation_config=data_transformation_config,
            data_validation_artifact=data_validation_artifact
            )
        logging.info("Initiating Data Transformation")
        data_transformation_artifact=data_transformation.initiate_dat_transformation()
        print(data_transformation_artifact)
        logging.info("data transformation completed")
        logging.info("Model training started")
        model_training_conffig=ModelTrainerConfig(training_pipeline)
        model_training_artifact=ModelTrainer(data_transformation_artifact=data_transformation_artifact,model_trainer_config=model_training_conffig)
        model_training_artifact.initiate_model_trainer()
        logging.info("Model training artifact created")
        
        
    except Exception as e:
        raise NetworkSecurityException(e,sys)

