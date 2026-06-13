import requests
import pandas as pd
import pymysql
import sqlalchemy # import the sqlalchemy module into the current session
from sqlalchemy import text# Import the text object
import time

# Define API URL phpmyadmin
url = "https://jogaan.fashol.com/api/get-table-data"

headers = {
    "X-API-KEY": "SonTzHgCApsbHPZttt7a21UoPGKlqqhm"
}

def get_table(table_name):
  # Send POST request with form-data directly
  response = requests.post(url, headers=headers, data={"table": table_name})

  # Convert to DataFrame if successful
  if response.status_code == 200:
    data = response.json()  # Parse JSON response
    df = pd.DataFrame(data["payload"])
    return df
  else:
    print(f"Error: {response.status_code}, {response.text}")



def get_table_with_query(table_name, query=None):
    payload = {"table": table_name}
    if query:
        payload["query"] = query  # Add the query to the payload if it exists

    response = requests.post(url, headers=headers, data=payload)

    # Convert to DataFrame if successful
    if response.status_code == 200:
        data = response.json()  # Parse JSON response
        if "payload" in data:
            df = pd.DataFrame(data["payload"])
            return df
        else:
            print("Error: 'payload' key not found in response.")
            print(f"Full response: {data}") # Print full response for debugging
            return None
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

def get_arots():
    return get_table_with_query('arots', "select * from arots")

def get_products():
    return get_table_with_query('products', "select * from products")

def get_units():
    return get_table_with_query('units', "select * from units")

if __name__ == '__main__':
    arots = get_arots()
    if arots is not None:
        print("Arots preview:")
        print(arots.head())


