import streamlit as st
import pandas as pd

import smtplib, ssl
import os


st.set_page_config(layout = "wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images(1)/Screenshot_20240705_160315.jpg", width=400)

with col2:
    st.title("Satvik Nanda")
    content = """
    Hello! I'm Satvik Nanda, currently entering my final year of my Computer Science degree at the Vellore Institute of Technology, Vellore. When I'm not deciphering complex algorithms or debugging my code (or my life), you’ll find me scratching my head around Python.

I picked up a keen interest for Python during the last six months which has encouraged me to manuever my way around projects, helping me improve my ability on every step. This website is a testament to my passion, showcasing the projects I've crafted.

From automating mundane tasks to developing intricate web applications, Python has been my go-to tool. I firmly believe in the mantra: “Code, Debug, Coffee, Repeat,” and I live by it every day.

    """
    st.info(content)

content2 = """
Below you can find some of the apps that i have built in python. Feel free to contact me!
"""

st.write(content2)

col3, empty_col, col4 = st.columns([3,1,3])

df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images(1)/" + row["image"])
        st.write(f"[Source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images(1)/" + row["image"])
        st.write(f"[Source code]({row['url']})")

#configuring email
def send_email(message):
    host = "smtp.gmail.com"
    port = 465


    username = "satvik.nanda@gmail.com"
    password = os.getenv("PASSWORD")
    receiver = "satvik.nanda@gmail.com"


    context  = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context = context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
