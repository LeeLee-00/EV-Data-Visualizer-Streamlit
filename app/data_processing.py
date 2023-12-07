import requests
import pandas as pd
import streamlit as st

def fetch_data(url, limit=1000):
    all_data = []
    offset = 0

    placeholder = st.empty()
    placeholder.text("Fetching data... Please wait.")

    while True:
        # Make an API request with the specified limit and offset
        response = requests.get(url, params={'$limit': limit, '$offset': offset})
        response.raise_for_status()  # Raise an exception for HTTP errors

        data = response.json()
        if not data:  # If no data is returned, exit the loop
            break

        all_data.extend(data)  # Add the fetched data to the all_data list
        offset += limit  # Increase the offset for the next request

    # Remove the loading message once data is fetched
    placeholder.empty()

    return all_data

# Function to extract latitude and longitude from a Point object
def extract_lat_lon(Point):
    if isinstance(Point, dict) and 'coordinates' in Point:
        return Point['coordinates'][1], Point['coordinates'][0]
    else:
        return None, None

# URL of the API to fetch data from
api_url = 'https://data.wa.gov/resource/f6w7-q2d2.json'

# Fetching the data and converting it to a DataFrame
data = pd.DataFrame(fetch_data(api_url))

# Extracting latitude and longitude and adding them as new columns
data[['latitude', 'longitude']] = data['geocoded_column'].apply(lambda x: pd.Series(extract_lat_lon(x)))

# Dropping the original 'geocoded_column'
data = data.drop(columns=['geocoded_column'])

# Filtering data to only include rows where the state is WA
dataWA = data.drop(data[data['state'] != 'WA'].index)