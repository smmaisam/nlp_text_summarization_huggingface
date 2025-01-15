from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.conponents.data_transformation import DataTransformation
from src.textSummarizer.logging import logger

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            data_transforamtion_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config = data_transforamtion_config)
            data_transformation.convert()
        except Exception as e:
            raise e