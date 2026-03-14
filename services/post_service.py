from core.supabase_client import supabase
from core.engine import TTUEngine

def get_feed_augmented(limit=20):
    # On ajuste la limite selon le flux informationnel calculé
    flow = TTUEngine.compute_flow()
    adjusted_limit = int(limit * flow)
    
    # On ne requête que si le système n'est pas en surchauffe dissipative
    if flow < 0.2:
        return [] # Protection contre le crash (Loi de Dissipation)

    res = supabase.table("posts").select(
        "id, text, media_path, created_at, like_count, comment_count, profiles(username, profile_pic)"
    ).order("created_at", desc=True).limit(adjusted_limit).execute()
    
    return res.data
