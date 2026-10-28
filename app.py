import streamlit as st
import time

# 1. Nastaveni stranky
st.set_page_config(
    page_title="BANANADOG & COFFEE",
    page_icon="🍌",
    layout="centered"
)

# Inicializace stavu stranky pro navigaci na hlavni plose
if "current_page" not in st.session_state:
    st.session_state.current_page = "🏠 DOMŮ"

# 2. DESIGN NA MÍRU (Cold Espresso Brown pozadí, Butter Yellow nadpisy a lišty)
st.markdown("""
    <style>
    @import url('https://googleapis.com');

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

    .butter-nav-bar {
        background-color: #F3E5AB;
        color: #1a1412;
        padding: 10px;
        border-radius: 14px;
        text-align: center;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 25px;
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

    /* Skrytí postranního panelu, aby nemátl */
    [data-testid="stSidebar"] { display: none !important; }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- 1. TITUL WEBU ---
st.markdown('<p class="profi-title">BANANADOG<br>& COFFEE</p>', unsafe_allow_html=True)
st.markdown('<p class="profi-subtitle">⚡ ZAPOMEŇ NA PÁREK. SLADKÝ POP-UP Z ČB ⚡</p>', unsafe_allow_html=True)

# --- 2. VIDITELNÝ NAVIGAČNÍ PANEL NA HLAVNÍ PLOŠE ---
st.markdown('<div class="butter-nav-bar">✨ NAVIGACE STRÁNEK ✨</div>', unsafe_allow_html=True)
nav_col1, nav_col2, nav_col3, nav_col4 = st.columns(4)

with nav_col1:
    if st.button("🏠 DOMŮ"):
        st.session_state.current_page = "🏠 DOMŮ"
with nav_col2:
    if st.button("📋 NABÍDKA"):
        st.session_state.current_page = "📋 NABÍDKA"
with nav_col3:
    if st.button("📸 GALLERY"):
        st.session_state.current_page = "📸 GALLERY"
with nav_col4:
    if st.button("✨ O NÁS"):
        st.session_state.current_page = "✨ O NÁS"

st.divider()

# ==========================================
# STRÁNKA 1: ÚVOD & OBJEDNÁVKA
# ==========================================
if st.session_state.current_page == "🏠 DOMŮ":
    st.image("https://streamlit.io", use_container_width=True)
    st.write("Máslová brioche bulka, grilovaný banán, brutal topingy a výběrové kafe v dravém streetwearovém podání. Objednej si dopředu a nečekej frontu!")
    st.divider()
    
    st.markdown("## 🚀 Klikni & Vyzvedni")
    with st.form("objednavka_form"):
        col_jmeno, col_tel = st.columns(2)
        with col_jmeno:
            jmeno = st.text_input("Jméno:")
        with col_tel:
            telefon = st.text_input("Telefon:")
        vyber_dog = st.selectbox("Bananadog:", ["Žádný", "The OG Classic", "Pink Special", "Lotus & Peanut", "White Berry", "Maple & Bacon"])
        vyber_kafe = st.selectbox("Kafe:", ["Žádné", "Flat White", "Ice Banana Latte", "Batch Brew"])
        cas = st.time_input("Čas vyzvednutí:")
        potvrdit = st.form_submit_button("🔥 ODESLAT OBJEDNÁVKU DO KUCHYNĚ 🔥")

    if potvrdit:
        if jmeno and telefon:
            st.success(f"🎉 **Objednávka proklouzla na bar, {jmeno}!**")
            st.balloons()
            st.info(f"Chystáme pro tebe: {vyber_dog} a {vyber_kafe} na {cas.strftime('%H:%M')} do Kavárenské 42, ČB.")
        else:
            st.error("Vyplň prosím jméno a telefon!")

# ==========================================
# STRÁNKA 2: PODROBNÁ NABÍDKA S POPISY A FOTKAMI
# ==========================================
elif st.session_state.current_page == "📋 NABÍDKA":
    st.markdown("## 📋 Naše Kompletní Nabídka")
    
    st.markdown("### 🌭 Sladké Bananadogy")
    
    # 1. OG Classic
    st.image("https://unsplash.com")
    st.markdown("#### 🍫 The OG Classic — 115 Kč")
    st.write("Dozlatova opečená máslová brioche bulka, teplý zralý banán, poctivá vrstva husté tekuté Nutelly, bohatě zasypaná drcenými Oreo sušenkami a jemný dotek mořské soli pro brutal zvýraznění všech tónů.")
    st.divider()
    
    # 2. Pink Special
    st.image("https://unsplash.com")
    st.markdown("#### 🦩 Pink Special — 140 Kč")
    st.write("Teplý banán v nadýchaném brioche obalu, přelitý nadýchaným, lehce kyselkavým malinovým mousse topingem, dozdobený křupavými mini preclíky obalenými v našem domácím slaném karamelu.")
    st.divider()
    
    # Ostatní dogy bez fotek pro přehlednost
    st.markdown("#### 🥜 Lotus & Peanut — 125 Kč")
    st.write("Tekuté arašídové máslo, jemný karamelový přeliv, položený na banánu a drcené sušenky Lotus Biscoff.")
    
    st.markdown("#### 🍓 White Berry — 120 Kč")
    st.write("Poleva z bílé belgické čokolády, mrazem sušené jahody a drcené máslové sušenky.")
    
    st.markdown("#### 🥓 Maple & Bacon — 135 Kč")
    st.write("Javorový sirup, drcené vlašské ořechy a navrch křupavá vypečená sekaná slanina.")
    
    st.divider()
    st.markdown("### ☕ Výběrové Kafe")
    st.write("- **Flat White** (Dvojité espresso, sametová mikropěna) — 85 Kč")
    st.write("- **Ice Banana Latte** (Ledové espresso s naším banánovým sirupem) — 95 Kč")
    st.write("- **Batch Brew** (Filtrovaná káva dne, fresh profil) — 65 Kč")

# ==========================================
# STRÁNKA 3: GALLERY (ATMOSFÉRA POP-UPU)
# ==========================================
elif st.session_state.current_page == "📸 GALLERY":
    st.markdown("## 📸 Bananadog Gallery")
    st.write("Atmosféra z našeho budějovického pop-upu.")
    st.image("https://unsplash.com", caption="Vrtění mlýnků a vůně čerstvých brioche.")
    st.image("https://unsplash.com", caption="Náš minimalistický chic interiér pro tvůj perfect feed.")

# ==========================================
# STRÁNKA 4: O NÁS (PŘÍBĚH)
# ==========================================
elif st.session_state.current_page == "✨ O NÁS":
    st.markdown("## ✨ Náš Příběh")
    st.write("Jak se z divokého snu a domácího nočního experimentu s banánem, brioškou a Nutellou stala opravdová budějovická hotdogárna a pop-up pro komunitu, která miluje streetwear, výběrové kafe a nebojí se zkoušet úletové kombinace.")
    st.image("https://unsplash.com")
    st.write("Dnes pro vás každý den grilujeme ty nejlepší sladké hotdogy v ČB. Děkujeme, že jste součástí našeho snu! 🍌☕️")
