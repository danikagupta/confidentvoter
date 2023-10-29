import streamlit as st
from streamlit.logger import get_logger
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.app_logo import add_logo 

LOGGER = get_logger(__name__)

def set_ui_home_page():
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


def run():
    st.write("# Welcome to Confident Voter! 🗳️")

    st.markdown(
        """
        
        ### Introducing **Confident Voter** - the essential app for individuals seeking to navigate the complexities of ballot propositions with ease. 
        
        * Confident Voter not only simplifies the often convoluted language of ballot measures but also fosters civic awareness and informed decision-making. 
        
        * Rest assured, our app sources information only from reputable sources, steering clear of misinformation, while maintaining a strong commitment to user privacy. 
        
        * This ensures that your voting choices remain confidential, allowing you to stay informed and vote confidently in alignment with your personal values and priorities.
    """
    )

    if st.button("Yes!! I want to learn more."):
            set_defaults()
            switch_page("Locate District")

def set_defaults():
    st.session_state['ballot'] = "Unknown"
    CSV_FILE="https://docs.google.com/spreadsheets/d/e/2PACX-1vTl4Pr6JYmt_2LvSeCrtWrIOwNyqKS5suc6hlKKdx1C82JEEjoJP02Y0dj7H18RMk6xpw7freYJUCLS/pub?gid=0&single=true&output=csv"
    st.session_state['CSV_FILE'] = CSV_FILE
    DEFAULT_LOC={'coords': {'accuracy': 19.812, 'altitude': None, 'altitudeAccuracy': None, 'heading': None, 'latitude': 37.2656344, 'longitude': -122.0261448, 'speed': None}, 'timestamp': 1698549903383}
    st.session_state['loc'] = DEFAULT_LOC


if __name__ == "__main__":
    set_ui_home_page()
    run()
    set_defaults()
