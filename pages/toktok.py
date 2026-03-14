import streamlit as st
from services.post_service import get_feed
from core.supabase_client import supabase


def get_media_url(path):

    try:

        res = supabase.storage.from_("media").create_signed_url(
            path,
            3600
        )

        return res["signedURL"]

    except:

        return None


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

        url = get_media_url(post["media_path"])

        if url:

            st.video(url)

    col1, col2, col3 = st.columns([1,4,1])

    with col1:

        if st.button("⬆️"):

            if st.session_state.index > 0:

                st.session_state.index -= 1

    with col3:

        if st.button("⬇️"):

            if st.session_state.index < len(posts)-1:

                st.session_state.index += 1
