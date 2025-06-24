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
import sys,os
from networksecurity.entity.artifact_entity import (
    DataIngestionArtifact,
    DataValidationArtifact,
    DataTransformationArtifact,
    ModelTrainingArtifact
)

class Trainingpipeline:
    def __init__(self,):
        self.training_pipeline_config=TrainingPipelineConfig()
    
    def start_data_ingestion(self):
        try:
            self.data_ingestion_config=DataIngestionConfig(self.training_pipeline_config)
            logging.info("Started data Ingestion")
            data_ingestion=DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
            logging.info("data Ingestion completed")
            return data_ingestion_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)    
    
    def start_data_validation(self,data_ingestion_artifact:DataIngestionArtifact):
        try:
            self.data_validation_config=DataValidationConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("started data validation")
            data_validation=DataValidation(data_ingestion_artifact=data_ingestion_artifact,data_validation_config=self.data_validation_config)
            data_validation_artifact=data_validation.initiate_data_validation()
            logging.info("Data validation Completed")
            return data_validation_artifact
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
        
    def start_data_transformation(self,data_validation_artifact:DataValidationArtifact):
        try:
            self.data_transformation_config=DataTransformationConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("started data transformation")
            data_transformation=DataTranformation(data_transformation_config=self.data_transformation_config,data_validation_artifact=data_validation_artifact)
            data_transformation_artifact=data_transformation.initiate_dat_transformation()
            logging.info("data transformation completed")
            return data_transformation_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def start_model_training(self,data_transformation_artifact:DataTransformationArtifact):
        try:
            logging.info("Model training started")
            self.model_training_config=ModelTrainerConfig(training_pipeline_config=self.training_pipeline_config)
            model_training_artifact=ModelTrainer(data_transformation_artifact=data_transformation_artifact,model_trainer_config=self.model_training_config)
            model_training_artifact.initiate_model_trainer()
            logging.info("Model training artifact created")
            return model_training_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def run_pipeline(self):
        try:
            data_ingestion_artifact=self.start_data_ingestion()
            data_validation_artifact=self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            data_transformation_artifact=self.start_data_transformation(data_validation_artifact=data_validation_artifact)
            model_trainer_artifact=self.start_model_training(data_transformation_artifact=data_transformation_artifact)
            return model_trainer_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)
                            