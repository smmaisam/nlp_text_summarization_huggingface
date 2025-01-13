import os  # Provides functions for interacting with the operating system
from box.exceptions import BoxValueError  # Handles specific exceptions from the `box` library
import yaml  # Used for reading and writing YAML files
from textSummarizer.logging import logger  # Custom logger for the project
from ensure import ensure_annotations  # Ensures type annotations are followed
from box import ConfigBox  # A utility class to work with nested dictionaries as objects
from pathlib import Path  # Provides a convenient way to work with file and directory paths
from typing import Any  # For type hints

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox object.
    
    Args:
        path_to_yaml (Path): Path to the YAML file.
    
    Raises:
        ValueError: If the YAML file is empty.
        Exception: If any other issue occurs during reading.
    
    Returns:
        ConfigBox: YAML content loaded as a ConfigBox (dictionary-like object).
    """
    try:
        with open(path_to_yaml) as yaml_file:  # Open the YAML file
            content = yaml.safe_load(yaml_file)  # Parse the YAML file into a Python dictionary
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")  # Log success
            return ConfigBox(content)  # Convert the dictionary into a ConfigBox object
    except BoxValueError:  # Handle the case where the YAML file is empty
        raise ValueError("yaml file is empty")
    except Exception as e:  # Catch any other exceptions
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates a list of directories if they do not already exist.
    
    Args:
        path_to_directories (list): List of paths to directories to be created.
        verbose (bool, optional): If True, logs the directory creation. Defaults to True.
    """
    for path in path_to_directories:  # Iterate over the list of directory paths
        os.makedirs(path, exist_ok=True)  # Create the directory, ignoring if it already exists
        if verbose:
            logger.info(f"created directory at: {path}")  # Log the creation of each directory

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Gets the size of a file in kilobytes (KB).
    
    Args:
        path (Path): Path to the file.
    
    Returns:
        str: File size in KB, formatted as a string.
    """
    size_in_kb = round(os.path.getsize(path)/1024)  # Get file size in bytes and convert to KB
    return f"~ {size_in_kb} KB"  # Return the size as a string