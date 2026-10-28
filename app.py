import streamlit as st
import time
import os

# 1. Nastaveni stranky
st.set_page_config(
    page_title="BANANADOG & COFFEE",
    page_icon="🍌",
    layout="centered"
)

# Inicializace stavu stranky pro navigaci
if "current_page" not in st.session_state:
    st.session_state.current_page = "🏠 MAIN PAGE"

# Funkce pro bezpecnou zmenu stranky
def set_page(page_name):
    st.session_state.current_page = page_name

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
