import streamlit as st
from services.user_service import (
    get_profile,
    update_profile,
    get_user_posts,
)


def render_profile():

    st.title("👤 Profile")

    user = st.session_state["user"]

    profile = get_profile(user.id)

    if not profile:
        st.error("Profile not found")
        return

    st.subheader(profile["username"])

    st.write(profile.get("bio", ""))

    st.write(profile.get("location", ""))

    st.divider()

    st.subheader("Edit profile")

    with st.form("edit_profile"):

        username = st.text_input(
            "Username",
            value=profile["username"]
        )

        bio = st.text_area(
            "Bio",
            value=profile.get("bio", "")
        )

        location = st.text_input(
            "Location",
            value=profile.get("location", "")
        )

        if st.form_submit_button("Update"):

            update_profile(user.id, username, bio, location)

            st.success("Profile updated")

    st.divider()

    st.subheader("Your posts")

    posts = get_user_posts(user.id)

    for post in posts:

        st.write(post["text"])

        if post["media_path"]:

            if post["media_path"].endswith(".mp4"):
                st.video(post["media_path"])
            else:
                st.image(post["media_path"])

        st.write(
            f"❤️ {post['like_count']}   💬 {post['comment_count']}"
        )

        st.divider()
