import streamlit as st
import time
import os

# 1. Nastaveni stranky
st.set_page_config(
    page_title="BANANADOG & COFFEE",
    page_icon="🍌",
    layout="centered"
)

# Inicializace stavu stranky pro navigaci na hlavni plose
if "current_page" not in st.session_state:
    st.session_state.current_page = "🏠 MAIN PAGE"

# 2. DESIGN NA MÍRU
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@800;900&family=Space+Grotesk:wght@400;700&display=swap');

    .main .block-container {
        font-family: 'Space Grotesk', sans-serif;
        background: rgba(30, 23, 20, 0.95);
        padding: 40px;
        border-radius: 24px;
        box-shadow: 0px 20px 50px rgba(0,0,0,0.6);
        margin-top: 1.5rem;
        margin-bottom: 2rem;
        border: 2px solid #F3E5AB;
    }

    .stApp {
        background-color: #1a1412;
        color: #f4ece8;
    }

    .profi-title {
        font-family: 'Montserrat', sans-serif;
        font-weight: 900;
        font-size: 4.5rem;
        text-align: center;
        line-height: 0.95;
        letter-spacing: -2px;
        color: #F3E5AB;
        margin-top: 0.5rem;
        margin-bottom: 0.5rem;
    }
    
    .profi-subtitle {
        font-family: 'Space Grotesk', sans-serif;
        text-align: center;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 5px;
        color: #E6D592;
        font-size: 0.95rem;
        margin-bottom: 2.5rem;
    }

    h1, h2, h3 {
        color: #F3E5AB !important;
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 800 !important;
    }

    .gastro-card {
        background: #261d1a;
        border: 1px solid #332723;
        border-radius: 16px;
        padding: 22px;
        margin-bottom: 16px;
        font-family: 'Space Grotesk', sans-serif;
        transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
        cursor: pointer;
    }
    
    .gastro-card:hover {
        transform: translateY(-4px) scale(1.01);
        border-color: #F3E5AB;
        box-shadow: 0px 15px 35px rgba(243, 229, 171, 0.25);
    }
    
    .gastro-title {
        color: #F3E5AB;
        font-size: 1.35rem;
        font-weight: 700;
        margin-bottom: 6px;
    }
    
    .gastro-desc {
        color: #d1c7bd;
        font-size: 0.95rem;
        line-height: 1.4;
    }
    
    .gastro-price {
        color: #E6D592;
        font-weight: 700;
        font-size: 1.1rem;
        margin-top: 12px;
        text-align: right;
    }

    .stButton>button {
        background-color: #F3E5AB !important; 
        color: #1a1412 !important; 
        border: none !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        border-radius: 12px !important;
        padding: 10px 20px !important;
        width: 100% !important;
    }
    
    .stButton>button:hover {
        background-color: #E6D592 !important;
    }

    [data-testid="stSidebar"] { display: none !important; }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- TITUL WEBU ---
st.markdown('<p class="profi-title">BANANADOG<br>& COFFEE</p>', unsafe_allow_html=True)
st.markdown('<p class="profi-subtitle">⚡ ZAPOMEŇ NA PÁREK. SLADKÝ POP-UP Z ČB ⚡</p>', unsafe_allow_html=True)

# --- NAVIGAČNÍ PANEL ---
nav_col1, nav_col2, nav_col3, nav_col4 = st.columns(4)

with nav_col1:
    if st.button("🏠 MAIN PAGE"):
        st.session_state.current_page = "🏠 MAIN PAGE"
with nav_col2:
    if st.button("📋 NABÍDKA"):
        st.session_state.current_page = "📋 NABÍDKA"
with nav_col3:
    if st.button("📸 GALLERY"):
        st.session_state.current_page = "📸 GALLERY"
with nav_col4:
    if st.button("✨ ORIGIN STORY"):
        st.session_state.current_page = "✨ ORIGIN STORY"

st.divider()

# ==========================================
# STRÁNKA 1: MAIN PAGE
# ==========================================
if st.session_state.current_page == "🏠 MAIN PAGE":
    image_path = "bananadog.png"
    if os.path.exists(image_path):
        st.image(image_path, caption="BANANADOG & COFFEE — Náš budějovický pop-up concept.", use_container_width=True)
    else:
        st.image("https://images.unsplash.com/photo-1509722747041-616f39b57569", caption="Obrázek bananadog.png nebyl nalezen v adresáři.", use_container_width=True)
    
    st.write("Máslová brioche bulka, grilovaný banán, brutal topingy a
    
