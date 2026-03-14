from core.supabase_client import supabase
import streamlit as st
from datetime import datetime


def like_post(post_id, user_id):

    try:

        supabase.table("likes").insert({
            "post_id": post_id,
            "user_id": user_id,
            "created_at": datetime.utcnow().isoformat()
        }).execute()

        supabase.rpc("increment_like", {"post_id": post_id}).execute()

        return True

    except Exception:

        return False


def add_comment(post_id, user_id, text):

    if not text.strip():
        return False

    try:

        supabase.table("comments").insert({
            "post_id": post_id,
            "user_id": user_id,
            "text": text,
            "created_at": datetime.utcnow().isoformat()
        }).execute()

        supabase.rpc("increment_comment", {"post_id": post_id}).execute()

        return True

    except Exception:

        return False


def get_comments(post_id):

    res = supabase.table("comments").select(

        """
        id,
        text,
        created_at,
        profiles(username)
        """

    ).eq("post_id", post_id).order("created_at").execute()

    return res.data
