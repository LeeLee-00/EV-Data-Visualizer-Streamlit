import streamlit as st
import data_processing as Dprocessing
import visualizatons as visuals

# Streamlit UI layout
st.title("Welcome to the EV Car Data Visualizer Streamlit App")
st.subheader('This dataset shows the Battery Electric Vehicles (BEVs) and Plug-in Hybrid Electric Vehicles (PHEVs) that are currently registered through Washington State Department of Licensing (DOL).')


with st.container():
        st.header('EV Car Dataset')
        st.dataframe(Dprocessing.dataWA)
        st.subheader('Dataset Description')
   # Write the description using markdown for formatted display
st.markdown("""
        | Column Name | Description |
        | ----------- | ----------- |
        | VIN (1-10) | The 1st 10 characters of each vehicle's Vehicle Identification Number (VIN). |
        | County | The geographic region of a state that a vehicle's owner is listed to reside within. Vehicles registered in Washington state may be located in other states. |
        | City | The city in which the registered owner resides. |
        | State | The geographic region of the country associated with the record. These addresses may be located in other states. |
        | zip Code | The 5 digit zip code in which the registered owner resides. |
        | Model Year | The model year of the vehicle, determined by decoding the Vehicle Identification Number (VIN). |
        | Make | The manufacturer of the vehicle, determined by decoding the Vehicle Identification Number (VIN). |
        | model | The model of the vehicle, determined by decoding the Vehicle Identification Number (VIN). |
        | ev_type | This distinguishes the vehicle as all electric or a plug-in hybrid. |
        | cafv_type | This categorizes vehicle as Clean Alternative Fuel Vehicles (CAFVs) based on the fuel requirement and electric-only range requirement in House Bill 2042 as passed in the 2019 legislative session. |
        | electric_range | Describes how far a vehicle can travel purely on its electric charge. |
        | base_msrp | This is the lowest Manufacturer's Suggested Retail Price (MSRP) for any trim level of the model in question. |
        | legislastive_district | The specific section of Washington State that the vehicle's owner resides in, as represented in the state legislature. |
        | dol_vehicle_id | Unique number assigned to each vehicle by Department of Licensing for identification purposes. |  
        | electric_utility | This is the electric power retail service territories serving the address of the registered vehicle. All ownership types for areas in Washington are included: federal, investor owned, municipal, political subdivision, and cooperative. If the address for the registered vehicle falls into an area with overlapping electric power retail service territories then a single pipe | delimits utilities of same TYPE and a double pipe || delimits utilities of different types. We combined vehicle address and Homeland Infrastructure Foundation Level Database (HIFLD) (https://gii.dhs.gov/HIFLD) RetailServiceTerritories feature layer using a geographic information system to assign values for this field. Blanks occur for vehicles with addresses outside of Washington or for addresses falling into areas in Washington not containing a mapped electric power retail service territory in the source data. |         
        | _2020_census_tract | The census tract identifier is a combination of the state, county, and census tract codes as assigned by the United States Census Bureau in the 2020 census, also known as Geographic Identifier (GEOID). More information can be found here: https://www.census.gov/programs-surveys/geography/about/glossary.html#partextimage13 https://www.census.gov/programs-surveys/geography/guidance/geo-identifiers.html |            
    """, unsafe_allow_html=True)
    

with st.container():
        st.header('Mapped Locations')
        visuals.create_map(Dprocessing.dataWA)
