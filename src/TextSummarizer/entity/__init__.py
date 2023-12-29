from dataclasses import dataclass
from pathlib import Path

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