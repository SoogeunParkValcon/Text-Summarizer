from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.components.data_transformation import DataTransformation

class DataTransformationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()

        data_transformation_config = config.data_transformation_config()

        data_transformation = DataTransformation(config = data_transformation_config)
        # this takes the data_transformation_config, and uses it to create the DataTransformation class

        # now we use the method defined in the data_transformation class

        data_transformation.convert()
            
        
