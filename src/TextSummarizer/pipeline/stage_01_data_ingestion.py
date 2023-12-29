from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.components.data_ingestion import DataIngestion
from TextSummarizer.logging import logger

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    # This function takes the ConfigurationManager class
    def main(self):
        config = ConfigurationManager()
        
        data_ingestion_config = config.get_data_ingestion_config()
        # this is the data_ingestion_config in the ConfigurationManager class, which is the DataIngestionConfig class

        data_ingestion = DataIngestion(config = data_ingestion_config)
        # this takes the data_ingestion_config, and uses it to create the DataIngestion class

        # and now we can use the methods within the DataIngestion class to download and extract the data
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()