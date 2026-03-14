import streamlit as st
from services.post_service import upload_video, create_post


def create_post_ui():

    user = st.session_state.user

    st.subheader("Create post")

    with st.form("post_form"):

        text = st.text_area("Caption")

        video = st.file_uploader(
            "Upload video",
            type=["mp4","mov"]
        )

        if st.form_submit_button("Post"):

            media_path = None

            if video:

                if video.size > 100 * 1024 * 1024:

                    st.error("Max 100MB")

                    return

                media_path = upload_video(user.id, video)

            create_post(user.id, text, media_path)

            st.success("Post created")
