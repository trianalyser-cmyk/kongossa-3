from core.supabase_client import supabase


def get_feed(limit=20):

    res = supabase.table("posts").select(

        """
        id,
        text,
        media_path,
        created_at,
        like_count,
        comment_count,
        profiles(username, profile_pic)
        """

    ).order("created_at", desc=True).limit(limit).execute()

    return res.data
