import streamlit as st
from services.post_service import get_feed
from core.supabase_client import supabase

# cache feed
@st.cache_data(ttl=30)
def load_videos():
    return get_feed(20)


def get_video_url(path):

    try:

        res = supabase.storage.from_("media").create_signed_url(
            path,
            3600
        )

        return res["signedURL"]

    except:

        return None


def render_toktok():

    st.title("🎵 TokTok")

    if "toktok_index" not in st.session_state:
        st.session_state.toktok_index = 0

    videos = load_videos()

    if not videos:
        st.info("No videos yet")
        return

    index = st.session_state.toktok_index

    video = videos[index]

    st.subheader(video["profiles"]["username"])

    if video["media_path"]:

        url = get_video_url(video["media_path"])

        if url:

            st.video(url)

    st.write(video["text"])

    col1, col2, col3 = st.columns([1,3,1])

    with col1:
        if st.button("⬆️ Prev"):
            if index > 0:
                st.session_state.toktok_index -= 1
                st.rerun()

    with col3:
        if st.button("⬇️ Next"):
            if index < len(videos) - 1:
                st.session_state.toktok_index += 1
                st.rerun()
