from core.supabase_client import supabase


def get_profile(user_id):

    res = supabase.table("profiles").select("*").eq("id", user_id).execute()

    if res.data:
        return res.data[0]

    return None


def update_profile(user_id, username, bio, location):

    supabase.table("profiles").update({

        "username": username,
        "bio": bio,
        "location": location

    }).eq("id", user_id).execute()


def get_user_posts(user_id):

    res = supabase.table("posts").select(

        """
        id,
        text,
        media_path,
        created_at,
        like_count,
        comment_count
        """

    ).eq("user_id", user_id).order("created_at", desc=True).execute()

    return res.data


def get_wallet(user_id):

    res = supabase.table("wallets").select("*").eq("user_id", user_id).execute()

    if res.data:
        return res.data[0]

    return None
