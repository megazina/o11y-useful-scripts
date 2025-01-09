import requests
import configparser
import time
import sys

# Read configuration from config.conf
config = configparser.ConfigParser()
config.read('config.conf')

auth_token = config.get('DEFAULT', 'auth_token')
realm = config.get('DEFAULT', 'realm')
dimension_name = config.get('DEFAULT', 'dimension_name')
limit_num = config.getint('DEFAULT', 'limit_num')
property_name = config.get('DEFAULT', 'property_name')
description = config.get('DEFAULT', 'description')

# Function to retrieve dimension values
def get_dimension_values():
    url = f"https://api.{realm}.signalfx.com/v2/dimension/?query=key%3A{dimension_name}&limit={limit_num}"
    headers = {
        'Content-Type': 'application/json',
        'X-SF-Token': auth_token
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Check for request errors
    return response.json()

# Function to update dimension with custom properties
def update_dimension(key, value):
    url = f"https://api.{realm}.signalfx.com/v2/dimension/{key}/{value}"
    headers = {
        'Content-Type': 'application/json',
        'X-SF-Token': auth_token
    }
    data = {
        "customProperties": {
            property_name: value  # Use the value as the property_value
        },
        "description": description,
        "key": key,
        "value": value
    }
    response = requests.put(url, headers=headers, json=data)
    response.raise_for_status()  # Check for request errors

# Main execution
def main():
    dimension_data = get_dimension_values()
    total_items = len(dimension_data.get('results', []))
    for index, item in enumerate(dimension_data.get('results', []), start=1):
        key = item.get('key')
        value = item.get('value')
        if key and value:
            update_dimension(key, value)
            print(f"Updated {index}/{total_items}", end='\r', flush=True)  # Progress message on one line
            time.sleep(0.1)  # Small delay to prevent hitting API rate limits
    
    print()  # Print newline after last update
    print(f"Congrats! You have successfully copied the values from {dimension_name} to {property_name}!")

if __name__ == "__main__":
    main()
