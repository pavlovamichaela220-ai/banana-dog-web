import streamlit as st
import time

# 1. Nastaveni stranky
st.set_page_config(
    page_title="BANANADOG & COFFEE",
    page_icon="🍌",
    layout="centered"
)

# 2. CSS Design (Cold Espresso & Butter Yellow)
st.markdown("""
    <style>
    @import url('https://googleapis.com');

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(15px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .main .block-container {
        animation: fadeIn 1s ease-out;
        font-family: 'Space Grotesk', sans-serif;
        background: rgba(30, 23, 20, 0.95);
        padding: 40px;
        border-radius: 24px;
        box-shadow: 0px 20px 50px rgba(0,0,0,0.6);
        margin-top: 1.5rem;
        margin-bottom: 2rem;
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
        margin-top: 1.5rem;
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
        letter-spacing: 2px !important;
        border-radius: 12px !important;
        padding: 12px 30px !important;
        width: 100% !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- PORADÍ PRVKŮ: NEJPRVE LOGO A SUBTITLE ---
st.markdown('<p class="profi-title">BANANADOG<br>& COFFEE</p>', unsafe_allow_html=True)
st.markdown('<p class="profi-subtitle">⚡ ZAPOMEŇ NA PÁREK. SLADKÝ POP-UP Z ČB ⚡</p>', unsafe_allow_html=True)

# --- SESTŘÍHANÝ NOVÝ ESTETICKÝ OBRÁZEK POD LOGEM ---
# Nový stabilní odkaz na minimalistický gastro-design
st.image("https://unsplash.com", caption="BANANADOG & COFFEE — Budějovický Pop-Up Concept v chic espresso stylu.", use_container_width=True)

st.write("Brioche bulka, grilovaný banán, brutal topingy a výběrové kafe v dravém streetwearovém podání.")
st.divider()

# --- NAŠE MENU ---
st.markdown("## 📋 Naše Menu")
kategorie = st.radio("Sekce:", ["🌭 Bananadogs", "☕ Výběrové Kafe"], horizontal=True)

if "Bananadogs" in kategorie:
    st.markdown("""
        <div class="gastro-card">
            <div class="gastro-title">🍫 The OG Classic</div>
            <div class="gastro-desc">Naše vlajková loď. Dozlatova opečená máslová brioche bulka, teplý zralý banán, poctivá vrstva husté tekuté Nutelly, bohatě zasypaná drcenými Oreo sušenkami a jemný dotek mořské soli pro brutal zvýraznění všech sladkých tónů.</div>
            <div class="gastro-price">115 Kč</div>
        </div>
        <div class="gastro-card">
            <div class="gastro-title">🦩 Pink Special</div>
            <div class="gastro-desc">Estetická bomba pro opravdové fajnšmekry. Teplý banán v nadýchaném brioche obalu, přelitý nadýchaným, lehce kyselkavým malinovým mousse topingem, dozdobený křupavými mini preclíky obalenými v našem domácím slaném karamelu.</div>
            <div class="gastro-price">140 Kč</div>
        </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <div class="gastro-card">
            <div class="gastro-title">☕ Flat White</div>
            <div class="gastro-desc">Dvojité espresso z výběrových zrn z lokální pražírny spojené s dokonale našlehanou mikropěnou. Dokonalý balanc síly a jemnosti k našim dogům.</div>
            <div class="gastro-price">85 Kč</div>
        </div>
        <div class="gastro-card">
            <div class="gastro-title">🍌 Ice Banana Latte</div>
            <div class="gastro-desc">Ledové osvěžení. Výběrové espresso, vychlazené plnotučné mléko, kostky ledu a náš řemeslný banánový sirup, který si sami vaříme.</div>
            <div class="gastro-price">95 Kč</div>
        </div>
    """, unsafe_allow_html=True)

st.divider()

# --- FORMULÁR ---
st.markdown("## 🚀 Rychlá objednávka")
with st.form("objednavka_form"):
    col_jmeno, col_tel = st.columns(2)
    with col_jmeno:
        jmeno = st.text_input("Jméno:")
    with col_tel:
        telefon = st.text_input("Telefon:")
    vyber_dog = st.selectbox("Bananadog:", ["Žádný", "The OG Classic", "Pink Special"])
    potvrdit = st.form_submit_button("🔥 ODESLAT OBJEDNÁVKU DO KUCHYNĚ 🔥")

if potvrdit:
    if jmeno and telefon:
        st.success(f"🎉 **Díky {jmeno}! Objednávka proletěla na bar.**")
        st.balloons()
        st.info(f"Chystáme pro tebe: {vyber_dog}. Místo vyzvednutí: Kavárenská 42, České Budějovice. Jakmile bulky vytáhneme z pece, pošleme ti SMS na {telefon}.")
    else:
        st.error("Chybka! Vyplň prosím jméno a telefon.")

# --- SIDEBAR ---
st.sidebar.markdown('### 🤎 BANANADOG')
st.sidebar.write("📍 Kavárenská 42, ČB")
st.sidebar.write("🕒 Dnes makáme: 8:00 - 20:00")
