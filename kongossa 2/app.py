import streamlit as st
from pages.toktok import render_toktok
from pages.feed import render_feed

st.set_page_config(layout="wide")

menu = st.sidebar.radio(
    "Menu",
    ["TokTok","Feed"]
)

if menu == "TokTok":

    render_toktok()

elif menu == "Feed":

    render_feed()
