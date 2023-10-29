import streamlit as st
from streamlit.logger import get_logger
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.app_logo import add_logo 

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Confident Voter",
        page_icon="🗳️",
    )
    st.image("ConfidentVoter.png")
    st.write("# Welcome to Confident Voter! 🗳️")

    st.markdown(
        """
        App Intro text
    """
    )

    if st.button("Next page"):
            switch_page("Locate District")

def set_defaults():
    st.session_state['ballot'] = "Unknown"
    CSV_FILE="https://docs.google.com/spreadsheets/d/e/2PACX-1vTl4Pr6JYmt_2LvSeCrtWrIOwNyqKS5suc6hlKKdx1C82JEEjoJP02Y0dj7H18RMk6xpw7freYJUCLS/pub?gid=0&single=true&output=csv"
    st.session_state['CSV_FILE'] = CSV_FILE
    DEFAULT_LOC={'coords': {'accuracy': 19.812, 'altitude': None, 'altitudeAccuracy': None, 'heading': None, 'latitude': 37.2656344, 'longitude': -122.0261448, 'speed': None}, 'timestamp': 1698549903383}
    st.session_state['loc'] = DEFAULT_LOC


if __name__ == "__main__":
    run()
    set_defaults()
