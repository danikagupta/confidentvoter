import streamlit as st

def set_ui_page_get_informed():
    for k in st.session_state:
        st.sidebar.write(f"session_state key={k} value={st.session_state[k]}")

def show_page_get_informed(ballot_index,ballot_information):
    st.markdown(f"# Get Informed about {ballot_information} at {ballot_index}")
#
#
if __name__ == "__main__":
    set_ui_page_get_informed()
    show_page_get_informed(st.session_state['ballot_index'],st.session_state['ballot_information'])