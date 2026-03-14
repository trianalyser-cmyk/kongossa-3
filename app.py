import streamlit as st

from pages.toktok import render_toktok
from pages.feed import render_feed
from pages.profile import render_profile
from pages.messages import render_messages

st.set_page_config(layout="wide")


# INITIALISATION SESSION
if "user" not in st.session_state:

    st.session_state.user = None


# PAGE LOGIN SIMPLE
def login():

    st.title("Login")

    with st.form("login_form"):

        username = st.text_input("Username")

        if st.form_submit_button("Enter"):

            st.session_state.user = {
                "id": username,
                "username": username
            }

            st.rerun()


# SI PAS CONNECTÉ
if st.session_state.user is None:

    login()
    st.stop()


# MENU PRINCIPAL
menu = st.sidebar.radio(
    "Menu",
    ["TokTok", "Feed", "Profile", "Messages"]
)


if menu == "TokTok":

    render_toktok()

elif menu == "Feed":

    render_feed()

elif menu == "Profile":

    render_profile()

elif menu == "Messages":

    render_messages()
