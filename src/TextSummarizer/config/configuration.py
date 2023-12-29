from TextSummarizer.constants import *
# the asterisk imports everything in the directory

from TextSummarizer.utils.common import read_yaml, create_directories
from TextSummarizer.entity import DataIngestionConfig

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
        # this creates the artifacts_root directory
        # because self.config does the "read_yaml" function which uses ConfigBox, the artifacts_roots can be just accessed by using the dot notation

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        This function returns the data ingestion config
        """
        config = self.config.data_ingestion

        create_directories([config.root_dir])
        # this creates the root_dir, given in the config.yaml
                
        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_URL = config.source_URL,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )
        
        return data_ingestion_config

