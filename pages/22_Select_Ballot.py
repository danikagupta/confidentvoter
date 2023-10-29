import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page

def set_ui_page_select_ballot():
    st.set_page_config(
        page_title="Select Ballot",
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

def redirect_button(url: str, text: str= None, color="#FD504D"):
    st.markdown(
    f"""
    <a href="{url}" target="_self">
        <div style="
            display: inline-block;
            padding: 0.5em 1em;
            color: #FFFFFF;
            background-color: {color};
            border-radius: 3px;
            text-decoration: none;">
            {text}
        </div>
    </a>
    """,
    unsafe_allow_html=True
    )

def load_csv():
    df=pd.read_csv(st.session_state['CSV_FILE'])
    # st.sidebar.dataframe(df, hide_index=True)
    return df

def show_page_select_ballot(df):
    st.markdown(f"# Select an upcoming ballot for {st.session_state['district_id']}")
    st.divider()
    df=df[df["District"]==st.session_state['district_id']]
    for index, row in df.iterrows():
        with st.container():
            (col1,col2)=st.columns([9,3])
            n=row['Name']
            m=row['Measure']
            p=row['Information']
            col1.markdown(m)
            if col2.button(f"{n}", key=index):
                st.write(f"Button clicked for Issue={n} and index={index}")
                st.session_state['ballot_name']=n
                st.session_state['measure']=m
                st.session_state['ballot_index']=index
                st.session_state['ballot_information']=p
                switch_page("Get Informed")
            st.divider()
#
#
if __name__ == "__main__":
    set_ui_page_select_ballot()
    df=load_csv()
    show_page_select_ballot(df)