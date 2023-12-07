import streamlit as st
import pydeck as pdk

def create_map(data):
        # Setting the viewport location around Washington
        view_state = pdk.ViewState(
            latitude=47.7511,  # Latitude for Washington's geographic center
            longitude=-120.7401,  # Longitude for Washington's geographic center
            zoom=5,
            pitch=0
        )

        # Creating PyDeck ScatterplotLayer for the map
        layer = pdk.Layer(
            "ScatterplotLayer",
            data=data,
            get_position=["longitude", "latitude"],
            auto_highlight=True,
            get_radius=1000,  # Radius in meters
            get_fill_color=[180, 0, 200, 140],  # RGBA value for fill color
            pickable=True
        )

        # Creating and displaying the PyDeck map
        st.pydeck_chart(pdk.Deck(
            initial_view_state=view_state,
            layers=[layer],
        ))
