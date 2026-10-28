import streamlit as st
import time
import os
import base64

# 1. Nastaveni stranky
st.set_page_config(
    page_title="BANANADOG & COFFEE",
    page_icon="🍌",
    layout="centered"
)

# Inicializace stavu stranky pro navigaci
if "current_page" not in st.session_state:
    st.session_state.current_page = "main"

def set_page(page_name):
    st.session_state.current_page = page_name

def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode("utf-8")
    return ""

# 2. DESIGN NA MÍRU
css_styles = "<style>@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@800;900&family=Space+Grotesk:wght@400;700&display=swap'); .main .block-container { font-family: 'Space Grotesk', sans-serif; background: rgba(30, 23, 20, 0.95); padding: 40px; border-radius: 24px; box-shadow: 0px 20px 50px rgba(0,0,0,0.6); margin-top: 1.5rem; margin-bottom: 2rem; border: 2px solid #F3E5AB; } .stApp { background-color: #1a1412; color: #f4ece8; } .profi-title { font-family: 'Montserrat', sans-serif; font-weight: 900; font-size: 7.2rem; text-align: center; line-height: 0.88; letter-spacing: -4px; color: #F3E5AB; margin-top: 0.5rem; margin-bottom: 0.5rem; } .profi-subtitle { font-family: 'Space Grotesk', sans-serif; text-align: center; font-weight: 700; text-transform: uppercase; letter-spacing: 5px; color: #E6D592; font-size: 0.95rem; margin-bottom: 2.5rem; } h1, h2, h3 { color: #F3E5AB !important; font-family: 'Montserrat', sans-serif !important; font-weight: 800 !important; } .gastro-card { background: #261d1a; border: 1px solid #332723; border-radius: 16px; padding: 22px; margin-bottom: 16px; font-family: 'Space Grotesk', sans-serif; } .gastro-title { color: #F3E5AB; font-size: 1.35rem; font-weight: 700; margin-bottom: 6px; } .gastro-desc { color: #d1c7bd; font-size: 0.95rem; line-height: 1.4; } .gastro-price { color: #E6D592; font-weight: 700; font-size: 1.1rem; margin-top: 12px; text-align: right; } .stButton>button { background-color: #F3E5AB !important; color: #1a1412 !important; border: none !important; font-weight: 700 !important; text-transform: uppercase !important; letter-spacing: 1px !important; border-radius: 12px !important; padding: 10px 20px !important; width: 100% !important; transition: all 0.3s ease-in-out !important; } .stButton>button:hover { background-color: #ffffff !important; color: #1a1412 !important; transform: translateY(-3px) scale(1.02) !important; box-shadow: 0px 10px 25px rgba(243, 229, 171, 0.4) !important; } [data-testid=\"stSidebar\"] { display: none !important; } #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}</style>"
st.markdown(css_styles, unsafe_allow_html=True)

# --- TITUL WEBU ---
st.markdown('<p class="profi-title">BANANADOG<br>& COFFEE</p>', unsafe_allow_html=True)
st.markdown('<p class="profi-subtitle">⚡ ZAPOMEŇ NA PÁREK. SLADKÝ POP-UP Z ČB ⚡</p>', unsafe_allow_html=True)

# --- NAVIGAČNÍ PANEL ---
nav_col1, nav_col2, nav_col3, nav_col4 = st.columns(4)

with nav_col1:
    if st.button("🏠 MAIN PAGE"):
        set_page("main")
        st.rerun()
with nav_col2:
    if st.button("📋 NABÍDKA"):
        set_page("nabidka")
        st.rerun()
with nav_col3:
    if st.button("📸 GALLERY"):
        set_page("gallery")
        st.rerun()
with nav_col4:
    if st.button("✨ ORIGIN STORY"):
        set_page("origin")
        st.rerun()

st.divider()

# ==========================================
# ROZCESTNÍK PODLE STAVU STRÁNKY
# ==========================================

if st.session_state.current_page == "main":
    sketch_path = "bananadog.png"
    sticker_path = "sticker.png"
    
    sketch_base64 = get_base64_image(sketch_path)
    sticker_base64 = get_base64_image(sticker_path)
    
    if sketch_base64 and sticker_base64:
        html_content = f"""
        <div style="position: relative; width: 100%; margin-top: 20px; margin-bottom: 40px;">
            <img src="data:image/png;base64,{sketch_base64}" style="width: 100%; border-radius: 16px; display: block; box-shadow: 0 10px 30px rgba(0,0,0,0.5);" alt="Bananadog Concept">
            <img src="data:image/png;base64,{sticker_base64}" style="position: absolute; bottom: -35px; left: -30px; width: 35%; transform: rotate(-12deg); filter: drop-shadow(0 10px 15px rgba(0,0,0,0.6)); z-index: 10;" alt="Sticker">
        </div>
        """
        st.markdown(html_content, unsafe_allow_html=True)
    else:
        if os.path.exists(sketch_path):
            st.image(sketch_path, use_container_width=True)
        else:
            st.info("💡 Nahraj soubor 'bananadog.png' do GitHubu.")
        if os.path.exists(sticker_path):
            st.image(sticker_path, width=200)
        else:
            st.warning("💡 Nahraj soubor 'sticker.png' do GitHubu.")

    t1 = "Máslová brioche bulka, grilovaný banán, brutal topingy a výběrové kafe "
    t2 = "v dravém streetwearovém podání. Přijď ochutnat do našeho budějovického pop-upu!"
    st.write(t1 + t2)
    st.divider()
    
    st.markdown("## 🔥 Our Bestsellers
