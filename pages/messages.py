import streamlit as st
from core.supabase_client import supabase
from datetime import datetime


def get_messages(user_id):

    res = supabase.table("messages").select("*").or_(

        f"sender.eq.{user_id},receiver.eq.{user_id}"

    ).order("created_at", desc=True).limit(50).execute()

    return res.data


def send_message(sender, receiver, text):

    supabase.table("messages").insert({

        "sender": sender,
        "receiver": receiver,
        "text": text,
        "created_at": datetime.utcnow().isoformat()

    }).execute()


def render_messages():

    st.title("✉️ Messages")

    user = st.session_state["user"]

    msgs = get_messages(user.id)

    for m in msgs:

        sender = "You" if m["sender"] == user.id else "Them"

        st.write(f"**{sender}:** {m['text']}")

    st.divider()

    st.subheader("Send message")

    with st.form("send_message"):

        receiver = st.text_input("Receiver ID")

        text = st.text_input("Message")

        if st.form_submit_button("Send"):

            send_message(user.id, receiver, text)

            st.success("Message sent")
