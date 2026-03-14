import streamlit as st


def render_messages():

    user = st.session_state.user

    st.title("Messages")

    st.write(f"Messages for {user['username']}")

    st.info("Messaging system coming soon")
