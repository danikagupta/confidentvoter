import streamlit as st
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

import os
import markdown

def _max_width_():
    max_width_str = "max-width: 1000px;"
    st.markdown(
        f"""
    <style>
    .block-container {{
        {max_width_str}
        }}
    .custom-widget {{
        display: grid;
        border: 1px solid black;
        padding: 12px;
        border-radius: 5%;
        color: #003366;
        margin-bottom: 5px;
        min-height: 251.56px;
        align-items: center;
    }}
    .row-widget.stCheckbox {{
        display: grid;
        justify-content: center;
        align-items: center;
        border: solid 2px black;
        border-radius: 3%;
        height: 50px;
        background-color: #DF1B88;
        color: #FFFFFF;
    }}
    </style>
    """,
        unsafe_allow_html=True,
    )


def set_ui_page_email_me():
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



def send_email(to_emails = 'testEmail@gprof.com',
               subject='Test Email: Please respond',
               message = '<strong>This should work</strong> even without Bolding'):
  #st.write(f"## Sending chat transcript to {to_emails}")
  #print(f"## Sending chat transcript to {to_emails}")
  message = Mail(
      from_email='Confident Voter <counsel@gprof.com>',
      to_emails=to_emails,
      subject=subject,
      html_content=message)
  try:
      sg_key=os.environ['SENDGRID_API_KEY']
      print(f"SendGrid key is: {sg_key}")
      sg = SendGridAPIClient(sg_key)
      response = sg.send(message)
      print(response.status_code)
      print(response.body)
      print(response.headers)
      print("Completed successfully")
  except Exception as e:
      print(e)
      print("Did not succeed")

def get_conversation_summary():
    role_names={"system":"System","assistant":"ConfidentVoter","user":"You"}
    formatted_messages = [f"## {role_names[m['role']]}:\n### {m['content']}\n\n" for m in st.session_state.messages[2:]]
    formatted_string="\n**********\n".join(formatted_messages)
    #print(f"Formatted string is {formatted_string}")
    summary=f"""
## Hi Voter

### Thank you for taking the time to ask the questions at the top of your mind. We are here to help you get savvy about Civics.
    
### -Confident Voter
    
### Here is the transcript: 

{formatted_string}
    """
    #print(f"Summary is {summary}")
    html_summary=markdown.markdown(summary)
    #print(f"HTML summary is {html_summary}")
    return html_summary

def ui_send_email():
    st.markdown("# Get chat transcript by email")
    em=st.text_input("Email address")
    if(st.button("Send Email")):
        g=get_conversation_summary()
        ballot_name=st.session_state['ballot_name']
        send_email(em,f'Transcript of your chat about {ballot_name}',g)
        #with st.sidebar.expander(f"Email message sent to {em}"):
        #    st.markdown(f"To: {em}.\n Body: {g}")
        st.write(f"## Your chat has been sent to {em}\n## No information will be saved.")

if __name__ == "__main__":
    set_ui_page_email_me()
    ui_send_email()