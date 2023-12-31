from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.components.data_validation import DataValidation


class DataValidationPipeline:

    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        
        data_validation_config = config.data_validation_config()

        data_validation = DataValidation(config = data_validation_config)
        # this takes the data_validation_config, and uses it to create the DataValidation class

        # now we use the method defined in the dtaa_validation class
        
        data_validation.validate_all_files_exist()
