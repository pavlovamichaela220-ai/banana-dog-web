import streamlit as st
import time
import os
import base64

st.set_page_config(
    page_title="BANANADOG & COFFEE",
    page_icon="🍌",
    layout="centered"
)

if "current_page" not in st.session_state:
    st.session_state.current_page = "main"

def set_page(page_name):
    st.session_state.current_page = page_name

def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode("utf-8")
    return ""

css_styles = "<style>@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@800;900&family=Space+Grotesk:wght@400;700&display=swap'); .main .block-container { font-family: 'Space Grotesk', sans-serif; background: rgba(30, 23, 20, 0.95); padding: 40px; border-radius: 24px; box-shadow: 0px 20px 50px rgba(0,0,0,0.6); margin-top: 1.5rem; margin-bottom: 2rem; border: 2px solid #F3E5AB; } .stApp { background-color: #1a1412; color: #f4ece8; } .profi-title { font-family: 'Montserrat', sans-serif; font-weight: 900; font-size: 8.5rem; text-align: center; line-height: 0.85; letter-spacing: -5px; color: #F3E5AB; margin-top: 0rem; margin-bottom: 0.2rem; text-shadow: 0 10px 30px rgba(0,0,0,0.5); } .profi-subtitle { font-family: 'Space Grotesk', sans-serif; text-align: center; font-weight: 700; text-transform: uppercase; letter-spacing: 6px; color: #E6D592; font-size: 1.05rem; margin-bottom: 1.8rem; } h1, h2, h3 { color: #F3E5AB !important; font-family: 'Montserrat', sans-serif !important; font-weight: 800 !important; } .gastro-card { background: #261d1a; border: 1px solid #332723; border-radius: 16px; padding: 22px; margin-bottom: 16px; font-family: 'Space Grotesk', sans-serif; } .gastro-title { color: #F3E5AB; font-size: 1.35rem; font-weight: 700; margin-bottom: 6px; } .gastro-desc { color: #d1c7bd; font-size: 0.95rem; line-height: 1.4; } .gastro-price { color: #E6D592; font-weight: 700; font-size: 1.1rem; margin-top: 12px; text-align: right; } .stButton>button { background-color: #F3E5AB !important; color: #1a1412 !important; border: none !important; font-weight: 700 !important; text-transform: uppercase !important; letter-spacing: 1px !important; border-radius: 12px !important; padding: 10px 20px !important; width: 100% !important; transition: all 0.3s ease-in-out !important; } .stButton>button:hover { background-color: #ffffff !important; color: #1a1412 !important; transform: translateY(-3px) scale(1.02) !important; box-shadow: 0px 10px 25px rgba(243, 229, 171, 0.4) !important; } [data-testid=\"stSidebar\"] { display: none !important; } #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}</style>"
st.markdown(css_styles, unsafe_allow_html=True)

# --- HLAVNÍ NADPIS A PODNADPIS ---
st.markdown('<p class="profi-title">BANANADOG<br>& COFFEE</p>', unsafe_allow_html=True)
st.markdown('<p class="profi-subtitle">⚡ ZAPOMEŇ NA PÁREK. SLADKÝ POP-UP Z ČB ⚡</p>', unsafe_allow_html=True)

# --- PANORAMATICKÝ BANNER HNED ZA NÁPISEM ---
sketch_path = "bananadog.png"
sticker_path = "sticker.png"

sketch_base64 = get_base64_image(sketch_path)
sticker_base64 = get_base64_image(sticker_path)

if sketch_base64 and sticker_base64:
    banner_html = f"""
    <div style="position: relative; width: 100%; height: 210px; overflow: hidden; border-radius: 16px; margin-bottom: 25px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border: 2px solid #332723;">
        <img src="data:image/png;base64,{sketch_base64}" style="width: 1
