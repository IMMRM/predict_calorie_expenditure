import subprocess
import os
from src.configuration.config import ConfigurationManager
from src.logger import logger
from zipfile import ZipFile



class DataIngestion:
    def __init__(self):
        self.config=ConfigurationManager().get_dataingestion_config()
    def data_ingestion(self):
        logger.info(">>Data Ingestion Started....")
        raw_data_path=self.config.raw_dataset
        try:
            subprocess.run([
                "kaggle", "competitions", "download", "-c", "playground-series-s5e5","-p",raw_data_path
            ])
            logger.info(">> Downloading completed>>")
            logger.info(">> Unzipping started...")
            for file in os.listdir(raw_data_path):
                if(file.endswith(".zip")):
                    file_path=os.path.join(raw_data_path,file)
                    with ZipFile(file_path,'r') as zip_ref:
                        zip_ref.extractall(raw_data_path)
                    os.remove(file_path)
            logger.info(">>Unzip has been completed>>")
        except Exception as e:
            raise e
        
        
