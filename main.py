from TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from TextSummarizer.pipeline.stage_02_data_validation import DataValidationPipeline
from TextSummarizer.logging import logger


STAGE_NAME = "Data Ingestion Stage"

# This just takes from the DataIngestionTrainingPipeline class and runs the main method
try:
    logger.info(f"Running stage: {STAGE_NAME}")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.main()
    logger.info(f"Stage: {STAGE_NAME} completed successfully")

except Exception as e:
    logger.exception(e)
    raise e    


STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f"Running stage: {STAGE_NAME}")
    data_validation_pipeline = DataValidationPipeline()
    data_validation_pipeline.main()
    logger.info(f"Stage: {STAGE_NAME} completed successfully")

except Exception as e:
    logger.exception(e)
    raise e    