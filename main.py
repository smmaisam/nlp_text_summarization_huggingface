from src.textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.textSummarizer.logging import logger

STAGE_NAME = "Data Ingestion Training Pipeline"
try:
    logger.info(f"Starting {STAGE_NAME}")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"Finished {STAGE_NAME}")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Training Pipeline"
try:
    logger.info(f"Starting {STAGE_NAME}")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"Finished {STAGE_NAME}")
except Exception as e:
    logger.exception(e)
    raise e