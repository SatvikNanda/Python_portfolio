import streamlit as st

st.header("Contact me")

with st.form(key = "email_forms"):
    user_email = st.text_input("You email address: ")
    message = st.text_area("Enter your message")

    button = st.form_submit_button("Submit")