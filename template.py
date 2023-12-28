# this provides a pythonic way of creating a template for a new file

import os
from pathlib import Path
import logging 

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')
# setting up the logging configuration

project_name = "TextSummarizer"

# the ".github" is for the CI/CD deployment
# init file is a constructor file
# in utils/common.py: the utilities are provided
# Dockerfile for the deployment

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "test.py"
]

for filepath in list_of_files:
    # converting the text so that it fits Windows OS (it detects the OS and converts it accordingly)
    filepath = Path(filepath)

    # getting the file directory and the file name (splitting the two)
    filedir, filename = os.path.split(filepath)

    # check whether the file is within a directory or not. If it is within a directory, then I create the directory
    if filedir != "":
        os.makedirs(filedir, exist_ok=True) # exist_ok = True means that if the directory already exists, then it will not throw an error. But also no overwritting.
        logging.info(f"Created directory: {filedir}, and underneath it, the file: {filename}")

    if (not os.path.exists(filepath) or os.path.getsize(filepath) == 0):
        # if the file does not exist, or if the filesize is 0, then I create the file
        
        # "w" = writing mode
        with open(filepath, "w") as f:
            pass
            logging.info(f"Created empty file: {filepath}")

    else: 
        logging.info(f"File already exists: {filepath}")
        



