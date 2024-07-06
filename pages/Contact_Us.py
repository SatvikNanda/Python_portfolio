import streamlit as st
from Home import send_email
from smtplib import SMTPResponseException


st.header("Contact me")

with st.form(key = "email_forms"):
    user_email = st.text_input("You email address: ")
    raw_message = st.text_area("Enter your message")

    message = f"""\
Subject: New email in portfolio contact me page from {user_email}

From: {user_email}
{raw_message}
"""

    try:
        button = st.form_submit_button("Submit")

        if button:
            send_email(message)
            st.info("Your email was sent successfully")
    except SMTPResponseException as response_error:
        print("Email sent successfully!")