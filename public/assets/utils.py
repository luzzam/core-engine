import logging
import os
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)

def load_config(file_path: str) -> Dict[str, Any]:
    try:
        with open(file_path, 'r') as file:
            import json
            return json.load(file)
    except FileNotFoundError:
        logger.error(f"Config file not found at {file_path}")
        return {}
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse config file: {e}")
        return {}

def write_config(config: Dict[str, Any], file_path: str) -> None:
    try:
        with open(file_path, 'w') as file:
            import json
            json.dump(config, file, indent=4)
    except Exception as e:
        logger.error(f"Failed to write config file: {e}")

def get_environment_variable(var_name: str, default: Optional[str] = None) -> Optional[str]:
    return os.environ.get(var_name, default)

def split_string_into_list(input_string: str, separator: str = ',') -> List[str]:
    return [s.strip() for s in input_string.split(separator) if s.strip()]

def merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    result = dict1.copy()
    result.update(dict2)
    return result

def is_file_exists(file_path: str) -> bool:
    return os.path.isfile(file_path)

def create_directory(dir_path: str) -> None:
    try:
        os.makedirs(dir_path, exist_ok=True)
    except Exception as e:
        logger.error(f"Failed to create directory: {e}")