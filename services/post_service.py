import uuid
from core.supabase_client import supabase
from datetime import datetime


def upload_video(user_id, file):

    ext = file.name.split(".")[-1]

    filename = f"posts/{user_id}/{uuid.uuid4()}.{ext}"

    supabase.storage.from_("media").upload(
        filename,
        file.getvalue(),
        {"content-type": f"video/{ext}"}
    )

    return filename


def create_post(user_id, text, media_path=None):

    supabase.table("posts").insert({

        "user_id": user_id,
        "text": text,
        "media_path": media_path,
        "created_at": datetime.utcnow().isoformat(),
        "like_count": 0,
        "comment_count": 0

    }).execute()
