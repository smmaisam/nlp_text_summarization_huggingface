import os
import sys
from src.textSummarizer.logging import logger
from src.textSummarizer.entity import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_files_exist(self) -> bool:
        try:
            validation_status = None
            all_files = os.listdir(os.path.join("artifacts" , "data_ingestion" , "samsum_dataset"))

            for file in all_files:
                if file not in self.config.all_required_files:
                    validation_status = False
                    with open(self.config.status_file, 'w') as file:
                        file.write("Data Validation Failed")
                else:
                    validation_status = True
                    with open(self.config.status_file, 'w') as file:
                        file.write("Data Validation Passed")
            
            return validation_status
        
        except Exception as e:
            logger.error(f"Data Validation Failed: {str(e)}")
            raise e