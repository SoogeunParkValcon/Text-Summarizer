import os
from TextSummarizer.logging import logger
from TextSummarizer.entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        """
        This class is used to execute data validation
        """
        self.config = config

    # method that downloads the data from the url
    def validate_all_files_exist(self) -> bool:

        try: 
            all_files = os.listdir(os.path.join("artifacts", "data_ingestion", "samsum_dataset"))
            # this provides all of the files in the artifacts/data_ingestion/samsum_dataset,
            # in a list format

            for file in all_files:
                if file not in self.config.ALL_REQUIRED_FILES:
                    logger.info(f"Validation failed for file: {file}")
                else: 
                    logger.info(f"Validation passed for file: {file}")

            validation_status = all(file in all_files for file in self.config.ALL_REQUIRED_FILES)
            
            with open(self.config.STATUS_FILE, "w") as f:
                f.write(f"Validation status: {validation_status}...")

        except Exception as e:
            raise e

        return validation_status
        
                