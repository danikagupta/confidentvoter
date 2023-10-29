# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
from streamlit_extras.switch_page_button import switch_page

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Confident Voter",
        page_icon="🗳️",
    )

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
