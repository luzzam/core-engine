import logging
import os
import json
from typing import Dict, List

def load_config(file_path: str) -> Dict:
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error(f"Config file not found: {file_path}")
        return {}
    except json.JSONDecodeError as e:
        logging.error(f"Failed to parse config file: {e}")
        return {}

def write_config(file_path: str, config: Dict) -> None:
    try:
        with open(file_path, 'w') as file:
            json.dump(config, file, indent=4)
    except Exception as e:
        logging.error(f"Failed to write config file: {e}")

def get_environment_variable(var_name: str) -> str:
    return os.environ.get(var_name, "")

def is_environment_variable_set(var_name: str) -> bool:
    return os.environ.get(var_name) is not None

def split_string_into_list(input_string: str, delimiter: str = ",") -> List[str]:
    return [item.strip() for item in input_string.split(delimiter)]

def merge_dicts(dict1: Dict, dict2: Dict) -> Dict:
    return {**dict1, **dict2}