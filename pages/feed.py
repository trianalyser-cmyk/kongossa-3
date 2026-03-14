import streamlit as st
from services.post_service import get_feed_augmented
from core.engine import TTUEngine

def render_feed():
    st.title("🌐 Flux TTU-Augmenté")
    
    # Calcul de l'état du système
    m, c, d = TTUEngine.get_state_vector()
    
    # Barre de monitoring de stabilité (Optionnelle mais recommandée)
    with st.sidebar.expander("📊 Vecteur d'état Φ"):
        st.progress(m, text=f"Mémoire (ΦM): {m:.2f}")
        st.progress(c, text=f"Cohérence (ΦC): {c:.2f}")
        st.progress(d, text=f"Dissipation (ΦD): {d:.2f}")

    # Application de l'Audio-Only si ΦD est trop élevé (Bande passante critique)
    low_bandwidth_mode = d > 0.8 or TTUEngine.compute_flow() < 0.4

    posts = get_feed_augmented()
    
    for post in posts:
        with st.container():
            st.subheader(post["profiles"]["username"])
            
            # Logique de rendu sélectif (Économie d'entropie)
            if not low_bandwidth_mode:
                if post["media_path"]:
                    if post["media_path"].endswith(".mp4"):
                        st.video(post["media_path"])
                    else:
                        st.image(post["media_path"])
            else:
                st.warning("⚠️ Mode basse dissipation : Médias désactivés")
                
            st.write(post["text"])
            # ... reste des interactions (Like/Comment)
