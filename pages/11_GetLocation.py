import streamlit as st
import geocoder
import folium
import requests
import pydeck as pdk

from geopy.geocoders import Nominatim
from streamlit_js_eval import streamlit_js_eval, copy_to_clipboard, create_share_link, get_geolocation
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
        page_title="Confident Voter",
        page_icon="🗳️",
)

loc = get_geolocation()
#st.write(f"Your coordinates are {loc}")
# Get latitude and longitude from loc
lat, lng = loc['coords']['latitude'], loc['coords']['longitude']
geolocator = Nominatim(user_agent="my-app")
location = geolocator.reverse(f"{lat}, {lng}")
address = location.address
#st.write(f"Your address is {address}")

# Make request to Google Civic Information API
api_key="AIzaSyD8FnzwnW9TppWWJJEFYo7IPoIIBRbT7yw"
url = f"https://www.googleapis.com/civicinfo/v2/representatives?address={address}&levels=country&roles=legislatorLowerBody&key={api_key}"
#url = f"https://www.googleapis.com/civicinfo/v2/elections?address={address}&levels=country&roles=legislatorLowerBody&key={api_key}"
print(f"Making request to {url}")
#st.sidebar.write(f"Making request to {url}")
response = requests.get(url)


# Parse response to extract congressional district information
data = response.json()
datadivision=data["divisions"]

print(f"\nJSON={response.json()}====\n")
#st.sidebar.write(response.json())
print(f"\n Division={datadivision}====\n")
for k,v in datadivision.items():
    print(f"\n Key,value:{k}={v}====\n")
    district_id=k
    district_name=v["name"]
#st.sidebar.write(f"FF district_id={district_id}\n FF district_name={district_name}")

congressional_district = district_name

# Display congressional district information using Streamlit
st.markdown(f"## It looks like you are in {congressional_district}")
(col1,col2)=st.columns(2)
with col1:
    if st.button(f"## Yes. This is my district."):
        switch_page("DataFrame_Demo")

with col2:
    if st.button(f"## No. I will enter my district manually."):
        switch_page("DataFrame_Demo")
layers=[
        # Create a marker layer at the specified location
        pdk.Layer(
            "ScatterplotLayer",
            data=[{"position": [lng,lat]}],
            get_position="position",
            get_radius=300,  # Marker size in pixels
            get_fill_color=[0, 0, 255],  # Marker color (red in RGB)
            get_icon="marker",
        ),
    ]

chart=pdk.Deck(map_style="mapbox://styles/mapbox/streets-v11",
               initial_view_state={"latitude": lat,"longitude": lng,"zoom": 11,"pitch": 5,},
               layers=layers)
st.pydeck_chart(chart)            
