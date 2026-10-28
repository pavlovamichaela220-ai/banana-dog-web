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

# 2. DESIGN NA MÍRU (Včetně gastro karet)
css_styles = """
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
    font-size: 7.2rem;
    text-align: center;
    line-height: 0.88;
    letter-spacing: -4px;
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
