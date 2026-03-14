import streamlit as st
from services.post_service import get_feed
from services.reaction_service import like_post, add_comment, get_comments


@st.cache_data(ttl=30)
def load_posts():

    return get_feed()


def render_feed():

    st.title("🌐 Feed")

    posts = load_posts()

    user = st.session_state["user"]

    if not posts:

        st.info("No posts yet")
        return

    for post in posts:

        with st.container():

            st.subheader(post["profiles"]["username"])

            st.write(post["text"])

            if post["media_path"]:

                if post["media_path"].endswith(".mp4"):
                    st.video(post["media_path"])
                else:
                    st.image(post["media_path"])

            st.write(
                f"❤️ {post['like_count']}   💬 {post['comment_count']}"
            )

            col1, col2 = st.columns(2)

            with col1:

                if st.button("❤️ Like", key=f"like_{post['id']}"):

                    if like_post(post["id"], user.id):
                        st.success("Liked")

            with col2:

                with st.expander("Comments"):

                    comments = get_comments(post["id"])

                    for c in comments:

                        st.write(
                            f"**{c['profiles']['username']}**: {c['text']}"
                        )

                    with st.form(f"comment_{post['id']}"):

                        text = st.text_input("Write comment")

                        if st.form_submit_button("Send"):

                            add_comment(post["id"], user.id, text)
