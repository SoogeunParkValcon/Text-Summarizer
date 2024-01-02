from dataclasses import dataclass
from pathlib import Path

# decorator frozen = True means:
# that this class "DataIngestionConfig", once created, is immutable. 
# Attempt to modify the attributes will create an error!

@dataclass(frozen = True)
class DataIngestionConfig:
    """
    Configuration for data ingestion
    
    This defines the type of the objects. This matches the config.yaml in the config directory
    """
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen = True)
class DataValidationConfig:
    """
    Providing the format of the data validation config
    """
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list


@dataclass(frozen = True)
class DataTransformationConfig:
    """
    Providing the format of the data transformation config
    """
    root_dir: Path
    data_path: Path
    result_file_name: str
    tokenizer_name: Path
# tokenizer is also a path.. interesting