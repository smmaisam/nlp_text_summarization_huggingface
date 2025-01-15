from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.conponents.data_validation import DataValidation
from src.textSummarizer.logging import logger

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config = data_validation_config)
            data_validation.validate_all_files_exist()
        except Exception as e:
            raise e