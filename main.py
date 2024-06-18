import streamlit as st

st.set_page_config(layout = "wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images(1)/photo.png")

with col2:
    st.title("Satvik Nanda")
    content = """
    Hi, i am satvik.
    """
    st.info(content)

content2 = """
Below you can find some of the apps that i have bbuilt in pythin. Feel free to contact me!
"""

st.write(content2)