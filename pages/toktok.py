import streamlit as st
from services.post_service import get_feed

def render_toktok():

    st.title("TokTok")

    if "index" not in st.session_state:

        st.session_state.index = 0

    posts = get_feed(20)

    if not posts:
        st.info("No videos")
        return

    post = posts[st.session_state.index]

    st.subheader(post["profiles"]["username"])

    if post["media_path"]:
        st.video(post["media_path"])

    col1, col2, col3 = st.columns([1,4,1])

    with col1:

        if st.button("⬆️"):

            if st.session_state.index > 0:

                st.session_state.index -= 1

    with col3:

        if st.button("⬇️"):

            if st.session_state.index < len(posts)-1:

                st.session_state.index += 1
