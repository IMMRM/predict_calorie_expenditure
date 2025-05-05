from ensure import ensure_annotations
from box import ConfigBox
import yaml
from pathlib import Path
from src.logger import logger
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml:Path)->ConfigBox:
    try:
        with open(path_to_yaml,'r') as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(">>Yaml file {path_to_yaml} loaded successfully!!")
            return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError("Yaml file is empty")
    except Exception as e:
        raise e
        