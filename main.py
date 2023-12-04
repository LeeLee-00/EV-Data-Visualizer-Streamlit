import requests
import streamlit as st
import pandas as pd
import pydeck as pdk

# Function to fetch data
@st.cache_data
def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # This will raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        st.error(f"HTTP error occurred: {http_err}")
    except Exception as err:
        st.error(f"An error occurred: {err}")

# URL for the API
api_url = 'https://data.wa.gov/resource/f6w7-q2d2.json'

# Fetching the data
data = fetch_data(api_url)

# Check if data is fetched
if data:
    # Extracting latitudes and longitudes
    locations = []
    for item in data:
        if 'geocoded_column' in item and 'coordinates' in item['geocoded_column']:
            lat = item["geocoded_column"]["coordinates"][1]
            lon = item["geocoded_column"]["coordinates"][0]
            locations.append({'latitude': lat, 'longitude': lon})

    # Convert to DataFrame
    locations_df = pd.DataFrame(locations)

    # Streamlit UI layout
    st.title("Welcome to EV car data visualizer streamlit app")
    st.text('In this project, I will be presenting data from...')

    # Setting the viewport location (soley around washington)
    view_state = pdk.ViewState(
        latitude=47.7511, #Lat for Washington's geogrpahic center
        longitude=-120.7401, #Lon for Washington's geogrpahic center
        zoom=5,
        pitch=0
    )

    # Creating PyDeck layer
    layer = pdk.Layer(
        'ScatterplotLayer',     # Type of layer to use
        data=locations_df,           # locations DataFrame
        get_position=['longitude', 'latitude']
    )

    with st.container():
        st.header('EV Car Dataset')
        st.dataframe(data)
        st.dataframe(locations_df)

    with st.container():
        st.header('Dataset Description')
        # Your model training code here

    with st.container():
        st.header('Mapped Locations')
    # Assuming locations_df is correctly set up
    if not locations_df.empty:
        # Setting the viewport location around Washington
        view_state = pdk.ViewState(
            latitude=47.7511,  # Latitude for Washington's geographic center
            longitude=-120.7401,  # Longitude for Washington's geographic center
            zoom=5,
            pitch=0
        )

        # Creating PyDeck ScatterplotLayer
        layer = pdk.Layer(
            "ScatterplotLayer",
            data=locations_df,
            get_position=["longitude", "latitude"],
            get_color=[255, 0, 0, 200],  # Optional: set point color (RGBA)
            get_radius=1500,            # Optional: set point radius
        )

        # Creating the PyDeck map
        st.pydeck_chart(pdk.Deck(
            initial_view_state=view_state,
            layers=[layer],
        ))

    with st.container():
        st.header('Analysis')
        # Your model training code here