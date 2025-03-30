import csv
import json
from utils.configutils import get_csv_folder_name, get_json_folder_name

# ====================================================================
# Define CSV and JSON Folder Paths based on environment configuration
# ====================================================================
csv_file_name = 'test_csv_data/' + get_csv_folder_name() + '/'
json_file_name = 'testdata/' + get_json_folder_name() + '/'


# ======================================================
# Function to write data to a CSV file
# Parameters:
# - file_name (str): Name of the CSV file
# - row_data_1 (str): First column value
# - row_data_2 (str): Second column value
# ======================================================
def write_csv_data(file_name, row_data_1, row_data_2):
    with open(csv_file_name + file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([row_data_1, row_data_2])


# ======================================================
# Function to write JSON data to a file
# Parameters:
# - file_name (str): Name of the JSON file
# - data (dict): Data to be written in JSON format
# ======================================================
def write_json_data(file_name, data):
    with open(json_file_name + file_name, 'w') as json_file:
        json.dump(data, json_file, indent=4)


# ======================================================
# Function to append JSON data to a file (without indentation)
# Parameters:
# - file_name (str): Name of the JSON file
# - data (dict): Data to be appended in JSON format
# ======================================================
def write_json_data_append(file_name, data):
    with open(json_file_name + file_name, 'w') as json_file:
        json.dump(data, json_file)


# ======================================================
# Function to read JSON data from a file
# Parameters:
# - file_name (str): Name of the JSON file
# Returns:
# - dict: JSON data loaded from the file
# ======================================================
def read_json_data(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data


# ======================================================
# Function to read JSON data from the environment-specific folder
# Parameters:
# - file_name (str): Name of the JSON file
# Returns:
# - dict: JSON data loaded from the file
# ======================================================
def read_json_data_env(file_name):
    with open(json_file_name + file_name, 'r') as file:
        data = json.load(file)
    return data


# ======================================================
# Function to create a CSV file and write column headers
# Parameters:
# - file_name (str): Name of the CSV file
# - column_name_1 (str): First column header
# - column_name_2 (str): Second column header
# ======================================================
def csv_file_write_column_name(file_name, column_name_1, column_name_2):
    with open(csv_file_name + file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([column_name_1, column_name_2])
