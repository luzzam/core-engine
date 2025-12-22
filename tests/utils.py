import os
import json
from typing import Any, Dict, List, Optional, Union

def read_json_file(file_path: str) -> Dict[str, Any]:
    """Read and parse a JSON file."""
    with open(file_path, 'r') as file:
        return json.load(file)

def write_json_file(file_path: str, data: Dict[str, Any]) -> None:
    """Write data to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def ensure_directory_exists(dir_path: str) -> None:
    """Ensure a directory exists; create it if it doesn't."""
    os.makedirs(dir_path, exist_ok=True)

def get_file_extension(file_path: str) -> str:
    """Get the file extension from a file path."""
    return os.path.splitext(file_path)[1].lower()

def filter_files_by_extension(dir_path: str, extension: str) -> List[str]:
    """Filter files in a directory by their extension."""
    return [
        os.path.join(dir_path, f) 
        for f in os.listdir(dir_path) 
        if f.endswith(extension)
    ]

def merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """Merge two dictionaries recursively."""
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = merge_dicts(result[key], value)
        else:
            result[key] = value
    return result

def validate_file_path(file_path: str) -> bool:
    """Validate if a file path exists and is accessible."""
    return os.path.exists(file_path) and os.access(file_path, os.R_OK)

def get_env_variable(key: str, default: Optional[str] = None) -> Optional[str]:
    """Get an environment variable or return a default value."""
    return os.getenv(key, default)