from src.constants import CONFIG_PATH
from src.utils.common import read_yaml
from src.entity.data_ingestion_config import DataIngestionConfig
from src.logger import logger


class ConfigurationManager:
    def __init__(self,config_path=CONFIG_PATH):
        self.config=read_yaml(config_path)
    def get_dataingestion_config(self)->DataIngestionConfig:
        config=self.config.dataset
        logger.info(f"Data Ingestion Config Loaded : {config}")
        data_ingestion=DataIngestionConfig(
            raw_dataset=config.raw
        )
        logger.info(f"Successfull data ingestion config details fetched: {data_ingestion}")
        return data_ingestion
        