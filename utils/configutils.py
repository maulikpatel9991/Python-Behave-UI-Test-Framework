import os
import yaml

# Global variable to store configuration (to prevent multiple file reads)
CONFIG = None

def load_config() -> dict:
    """
    Loads configuration settings based on the environment.

    Returns:
    - dict: A dictionary containing configuration settings for the current environment.
    """
    global CONFIG
    if CONFIG is None:
        env = os.environ.get('ENV', 'qa')  # Default to 'qa' if ENV is not set
        with open('settings/config.yaml', 'r') as file:
            all_configs = yaml.safe_load(file)
            CONFIG = all_configs.get(env, {})
    return CONFIG


def get_config_value(key: str, default: str = '') -> str:
    """
    Retrieves a specific configuration value based on the current environment.

    Parameters:
    - key (str): The configuration key to retrieve.
    - default (str): The default value if the key is not found.

    Returns:
    - str: The configuration value, or the default value if not found.
    """
    return load_config().get(key, default)


def get_apiurl() -> str:
    """Retrieves the API URL for the current environment."""
    return get_config_value('apiurl')


def get_url() -> str:
    """Retrieves the Base URL for the current environment."""
    return get_config_value('base_url')


def get_csv_folder_name() -> str:
    """Retrieves the CSV folder path for the current environment."""
    return get_config_value('CsvFolder')


def get_allure_folder_name() -> str:
    """Retrieves the Allure reports output directory."""
    return get_config_value('output_dir')


def get_json_folder_name() -> str:
    """Retrieves the JSON folder path for the current environment."""
    return get_config_value('jsonFolder')
