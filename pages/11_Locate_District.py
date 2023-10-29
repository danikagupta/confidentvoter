import streamlit as st
import geocoder
import folium
import requests
import pydeck as pdk
import re 

from geopy.geocoders import Nominatim
from streamlit_js_eval import streamlit_js_eval, copy_to_clipboard, create_share_link, get_geolocation
from streamlit_extras.switch_page_button import switch_page

def set_ui_page_get_location():
    st.set_page_config(
        page_title="Confident Voter",
        page_icon="🗳️"
    )
    st.image("ConfidentVoter.png")

    st.markdown(
        """
        <style>
        button {
            height: 50px;
            width: 200px;
            font-size: 30px;
            padding-top: 10px !important;
            padding-bottom: 10px !important;
            background: #e62143;
            border-radius: 11px;
            box-sizing: border-box;
            color: #fff;
            cursor: pointer;
            display: flex;
            font-family: Mija,-apple-system,BlinkMacSystemFont,Roboto,"Roboto Slab","Droid Serif","Segoe UI",system-ui,Arial,sans-serif;
            font-size: 1.55em;
            font-weight: 700;
            justify-content: center;
            line-height: 33.4929px;
            padding: .8em 1em;
            text-align: center;
            text-decoration: none;
            text-decoration-skip-ink: auto;
            text-shadow: rgba(0, 0, 0, .3) 1px 1px 1px;
            text-underline-offset: 1px;
            transition: all .2s ease-in-out;
            user-select: none;
            -webkit-user-select: none;
            touch-action: manipulation;
            width: 100%;
            word-break: break-word;
            border: 0;
        }
        </style>
        """,
    unsafe_allow_html=True,
    )

def get_loc():
    loc = get_geolocation() or st.session_state['loc']
    # Get latitude and longitude from loc
    lat, lng = loc['coords']['latitude'], loc['coords']['longitude']
    return lat, lng

def get_district(lat,lng):
    geolocator = Nominatim(user_agent="my-app")
    location = geolocator.reverse(f"{lat}, {lng}")
    address = location.address
    #st.write(f"Your address is {address}")
    # Make request to Google Civic Information API
    api_key="AIzaSyD8FnzwnW9TppWWJJEFYo7IPoIIBRbT7yw"
    url = f"https://www.googleapis.com/civicinfo/v2/representatives?address={address}&levels=country&roles=legislatorLowerBody&key={api_key}"
    #url = f"https://www.googleapis.com/civicinfo/v2/elections?address={address}&levels=country&roles=legislatorLowerBody&key={api_key}"
    #print(f"Making request to {url}")
    #st.sidebar.write(f"Making request to {url}")
    response = requests.get(url)


    # Parse response to extract congressional district information
    data = response.json()
    datadivision=data["divisions"]

    #print(f"\nJSON={response.json()}====\n")
    #st.sidebar.write(response.json())
    #print(f"\n Division={datadivision}====\n")
    for k,v in datadivision.items():
        #print(f"\n Key,value:{k}={v}====\n")
        district_info=re.split('[:/]',k)
        #print("district_info=",district_info)
        district_id="-".join([district_info[4].upper(),district_info[6]])
        district_name=v["name"]
    #st.sidebar.write(f"FF district_id={district_id}\n FF district_name={district_name}")

    return district_id,district_name


def show_district(district_id):
    # Display congressional district information using Streamlit
    st.markdown(f"## As per GPS, you are in {district_id}")
    (col1,col2)=st.columns(2)
    with col1:
        if st.button(f"## Yes. This is my district."):
            switch_page("Select_Ballot")
    with col2:
        if st.button(f"## No. I will provide my district."):
            switch_page("Select_Ballot")

def draw_map(lat,lng):
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
#
#
if __name__ == "__main__":
    set_ui_page_get_location()
    (lat,lng)=get_loc()
    (district_id,district_name)=get_district(lat,lng)
    #print(f"district_id={district_id} for congressional_district={district_name}")
    show_district(district_id)
    draw_map(lat,lng)
    st.session_state['district_id']=district_id          
