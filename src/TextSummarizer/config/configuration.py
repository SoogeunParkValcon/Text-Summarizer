from TextSummarizer.constants import *
# the asterisk imports everything in the directory
# the 'constants' includes the CONFIG_FILE_PATH and PARAMS_FILE_PATH

from TextSummarizer.utils.common import read_yaml, create_directories
from TextSummarizer.entity import DataIngestionConfig
from TextSummarizer.entity import DataValidationConfig
from TextSummarizer.entity import DataTransformationConfig

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH
    ):
        """
        This class is used to manage the configuration of the project
        """

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_roots]) 
        # this refers to the artifacts_roots in the config.yaml
        # this creates the 'artifacts' directory
        # because self.config does the "read_yaml" function which uses ConfigBox, the artifacts_roots can be just accessed by using the dot notation

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        This function returns the data ingestion config
        """

        config = self.config.data_ingestion
        # this refers to the data_ingestion in the config.yaml which is loaded above

        create_directories([config.root_dir])
        # this creates the directory under artifacts called 'data_ingestion'
                
        # the following defineds the "DataIngestionConfig" class
        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_URL = config.source_URL,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )
        
        return data_ingestion_config

    def data_validation_config(self) -> DataValidationConfig:
        """
        This function returns the data validation config
        """
        config = self.config.data_validation
        # this refers to the data_validation in the config.yaml which is loaded above

        create_directories([config.root_dir])
        # this creates the directory under artifacts called 'data_validation'
        
        data_validation_config = DataValidationConfig(
            root_dir = config.root_dir,
            STATUS_FILE = config.STATUS_FILE,
            ALL_REQUIRED_FILES = config.ALL_REQUIRED_FILES
        )
        
        return data_validation_config
    
    
    def data_transformation_config(self) -> DataTransformationConfig:
        """
        This function returns the data transformation config
        """
        
        config = self.config.data_transformation
        
        create_directories([config.root_dir])
        
        data_transformation_config = DataTransformationConfig(
            root_dir = config.root_dir,
            data_path = config.data_path,
            result_file_name = config.result_file_name,
            tokenizer_name = config.tokenizer_name
        )
    
        return data_transformation_config


