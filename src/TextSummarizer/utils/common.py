# what is utils?
# We're creating a module to store all the utilities that we need for the project.
# these utility functions are just used very commonly in the project.

import os
from box.exceptions import BoxValueError # we will be using box exceptions (what are those?)
from TextSummarizer.logging import logger 
import yaml
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

# read_yaml method:
# responsible for reading yaml file, return all the content present in the yaml file.


@ensure_annotations # this is a "decorator" (a function that takes another function as an argument)
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns the content of the YAML file as a ConfigBox object.
    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        e: empty file

    Returns:
        ConfigBox: Content of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)    
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)

    except BoxValueError:
        raise ValueError("yaml file is empty")
    
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"