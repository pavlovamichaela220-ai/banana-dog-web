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

if "cart" not in st.session_state:
    st.session_state.cart = []

def set_page(page_name):
    st.session_state.current_page = page_name

def add_to_cart(item_name, price):
    st.session_state.cart.append({"name": item_name, "price": price})
    st.toast(f"Přihozeno do košíku: {item_name}! 🍌", icon="🛒")

def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode("utf-8")
    return ""

css_styles = "<style>@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@800;900&family=Space+Grotesk:wght@400;700&display=swap'); @keyframes slideFromLeft { 0% { opacity: 0; transform: translateX(-350px); } 100% { opacity: 1; transform: translateX(0); } } @keyframes slideFromRight { 0% { opacity: 0; transform: translateX(350px); } 100% { opacity: 1; transform: translateX(0); } } .main .block-container { font-family: 'Space Grotesk', sans-serif; background: rgba(30, 23, 20, 0.95); padding: 12px; border-radius: 24px; box-shadow: 0px 20px 50px rgba(0,0,0,0.6); margin-top: 1rem; margin-bottom: 2rem; border: 2px solid #F3E5AB; } .stApp { background-color: #1a1412; color: #f4ece8; } .title-left { font-family: 'Montserrat', sans-serif; font-weight: 900; font-size: 5rem !important; text-align: center; line-height: 0.85; letter-spacing: -3px; color: #F3E5AB; margin: 0; text-shadow: 0 10px 30px rgba(0,0,0,0.5); animation: slideFromLeft 1.4s cubic-bezier(0.16, 1, 0.3, 1) forwards; } .title-right { font-family: 'Montserrat', sans-serif; font-weight: 900; font-size: 5rem !important; text-align: center; line-height: 0.85; letter-spacing: -3px; color: #F3E5AB; margin: 0 0 0.2rem 0; text-shadow: 0 10px 30px rgba(0,0,0,0.5); animation: slideFromRight 1.4s cubic-bezier(0.16, 1, 0.3, 1) forwards; } .profi-subtitle { font-family: 'Space Grotesk', sans-serif; text-align: center; font-weight: 700; text-transform: uppercase; letter-spacing: 6px; color: #E6D592; font-size: 1.05rem; margin-bottom: 1.8rem; } h1, h2, h3 { color: #F3E5AB !important; font-family: 'Montserrat', sans-serif !important; font-weight: 800 !important; } .gastro-card { background: #261d1a; border: 1px solid #332723; border-radius: 16px; padding: 22px; margin-bottom: 16px; font-family: 'Space Grotesk', sans-serif; transition: all 0.3s ease-in-out; } .gastro-card:hover { border-color: #F3E5AB !important; transform: translateY(-4px); box-shadow: 0 10px 25px rgba(243, 229, 171, 0.3); } .gastro-title { color: #F3E5AB; font-size: 1.35rem; font-weight: 700; margin-bottom: 6px; } .gastro-desc { color: #d1c7bd; font-size: 0.95rem; line-height: 1.4; } .gastro-price { color: #E6D592; font-weight: 700; font-size: 1.1rem; margin-top: 12px; text-align: right; } .stButton>button { background-color: #F3E5AB !important; color: #1a1412 !important; border: none !important; font-weight: 700 !important; text-transform: uppercase !important; letter-spacing: 1px !important; border-radius: 12px !important; padding: 10px 20px !important; width: 100% !important; transition: all 0.3s ease-in-out !important; } .stButton>button:hover { background-color: #ffffff !important; color: #1a1412 !important; transform: translateY(-3px) scale(1.02) !important; box-shadow: 0px 10px 25px rgba(243, 229, 171, 0.4) !important; } [data-testid=\"stSidebar\"] { display: none !
