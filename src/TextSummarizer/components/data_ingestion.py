import os
import urllib.request as request
import zipfile
from TextSummarizer.logging import logger
from TextSummarizer.utils.common import get_size
from TextSummarizer.entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        """
        This class is used to ingest data
        """
        self.config = config

    # method that downloads the data from the url
    def download_file(self):

        # first, we check whether the data exists already. If it is not the case, we proceed and download the data
        if not os.path.exists(self.config.local_data_file) or get_size(Path(self.config.local_data_file)) == '~ 0 KB':
            filename, headers = request.urlretrieve(
                url = self.config.source_URL, 
                filename = self.config.local_data_file
                )
            logger.info(f"Downloaded file from {self.config.source_URL} \n to {self.config.local_data_file}. \nInfo: \n{headers}")

        else:
            logger.info(f"File already present at {self.config.local_data_file}. File size = {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        """
        This function extracts the zip file
        """
        # first defining the directory for unzipping
        # this is defined already in the config.yaml
        unzip_path = self.config.unzip_dir

        os.makedirs(unzip_path, exist_ok = True)

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)
        