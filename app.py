import streamlit as st
import time

# 1. Nastaveni stranky
st.set_page_config(
    page_title="BANANADOG & COFFEE",
    page_icon="🍌",
    layout="centered"
)

# Inicializace stavu stranky (aby fungovalo spolehlive prepinani na hlavni plose)
if "current_page" not in st.session_state:
    st.session_state.current_page = "🏠 DOMŮ"

# 2. CHIC DESIGN NA MÍRU (Cold Espresso Brown pozadí, Butter Yellow nadpisy a lišty)
st.markdown("""
    <style>
    /* Import čistých minimalistických fontů */
    @import url('https://googleapis.com');

    /* Plynulé načítání celého webu */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(15px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .main .block-container {
        animation: fadeIn 1s ease-out;
        font-family: 'Space Grotesk', sans-serif;
        background: rgba(30, 23, 20, 0.95); /* Chladné tmavě hnědé tělo (Espresso Brown) */
        padding: 40px;
        border-radius: 24px;
        box-shadow: 0px 20px 50px rgba(0,0,0,0.6);
        margin-top: 1.5rem;
        margin-bottom: 2rem;
        border: 2px solid #F3E5AB; /* Esteticke maslove ohraniceni celeho webu */
    }

    /* Globální úprava pozadí celé aplikace */
    .stApp {
        background-color: #1a1412; /* Studené hluboké hnědé pozadí */
        color: #f4ece8; /* Soft krémový text pro snadnou čitelnost */
    }

    /* ESTETICKÉ LOGO A NADPISY V BUTTER YELLOW */
    .profi-title {
        font-family: 'Montserrat', sans-serif;
        font-weight: 900;
        font-size: 4.5rem;
        text-align: center;
        line-height: 0.95;
        letter-spacing: -2px;
        color: #F3E5AB; /* Pastelová Butter Yellow */
        margin-top: 0.5rem;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 0px #1a1412;
    }
    
    .profi-subtitle {
        font-family: 'Space Grotesk', sans-serif;
        text-align: center;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 5px;
        color: #E6D592; /* Tlumenější máslová žlutá */
        font-size: 0.95rem;
        margin-bottom: 2.5rem;
    }

    h1, h2, h3, [data-testid="stMarkdownContainer"] h2 {
        color: #F3E5AB !important;
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 800 !important;
    }

    /* Gastro karty produktů s jemnou animací */
    .gastro-card {
        background: #261d1a; 
        border: 1px solid #332723;
        border-radius: 16px;
        padding: 22px;
        margin-bottom: 16px;
        transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
        font-family: 'Space Grotesk', sans-serif;
    }
    
    .gastro-card:hover {
        transform: translateY(-3px);
        border-color: #F3E5AB;
        box-shadow: 0px 12px 30px rgba(243, 229, 171, 0.08);
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

    /* MÁSLOVÝ NAVIGAČNÍ PANEL NA HLAVNÍ PLOŠE */
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

    /* Prémiová minimalistická tlačítka */
    .stButton>button {
        background-color: #F3E5AB !important; 
        color: #1a1412 !important; 
        border: none !important;
        font-weight: 700 !important;
        font-family: 'Space Grotesk', sans-serif !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        border-radius: 12px !important;
        padding: 10px 20px !important;
        width: 100% !important;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #E6D592 !important;
    }

    /* Skrytí standardních prvků Streamlitu a otravného sidebaru */
    [data-testid="stSidebar"] { display: none !important; }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)


# --- 1. LOGO A TITUL NAHOŘE ---
st.markdown('<p class="profi-title">BANANADOG<br>& COFFEE</p>', unsafe_allow_html=True)
st.markdown('<p class="profi-subtitle">⚡ ZAPOMEŇ NA PÁREK. SLADKÝ POP-UP Z ČB ⚡</p>', unsafe_allow_html=True)


# --- 2. NOVÁ NEPŘEHLÉDNUTELNÁ MÁSLOVÁ LIŠTA S NAVIGACÍ ---
st.markdown('<div class="butter-nav-bar">✨ MENU STRÁNEK ✨</div>', unsafe_allow_html=True)

# Tlačítka vedle sebe pro okamžité přepínání
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
# REAKCE NA KLIKNUTÍ: ZOBRAZENÍ STRÁNEK
# ==========================================

# STRÁNKA: DOMŮ
if st.session_state.current_page == "🏠 DOMŮ":
    st.image("https://streamlit.io", use_container_width=True)
    st.write(
        "Vezmeme nadýchanou máslovou brioche bulku, opečeme ji na grilu, vložíme čerstvý banán "
        "a zasypeme ho brutal autorskými kombinacemi krémů a posypů. "
        "Naklikej si svou brutal kombinaci dopředu a vyzvedni si ji horkou na baru!"
    )
    st.divider()
    
    st.markdown("## 🚀 Rychlá objednávka (Click & Collect)")
    with st.form("rychla_objednavka"):
        col_jmeno, col_tel = st.columns(2)
        with col_jmeno:
            jmeno = st.text_input("Tvoje jméno:")
        with col_tel:
            telefon = st.text_input("Tvůj telefon:")
            
        vyber_dog = st.selectbox(
            "Vyber si svůj Bananadog:",
            ["Žádný", "The OG Classic (Nutella + Oreo)", "Pink Special (Malina + Preclíky)", "Lotus & Peanut", "White Berry", "Maple & Bacon"]
        )
        vyber_kafe = st.selectbox(
            "Co k tomu na pití?",
            ["Žádné", "Flat White", "Ice Banana Latte", "Batch Brew"]
        )
        cas_vyzvednuti = st.time_input("V kolik hodin se zastavíš?")
        potvrdit = st.form_submit_button("🔥 ODESLAT OBJEDNÁVKU DO KUCHYNĚ 🔥")

    if potvrdit:
        if jmeno and telefon:
            progress_bar = st.progress(0)
            for percent_complete in range(100):
                time.sleep(0.005)
                progress_bar.progress(percent_complete + 1)
            progress_bar.empty()
            
            st.success(f"🎉 **Objednávka proklouzla na bar, {jmeno}!**")
            st.balloons()
            st.info(f"Chystáme: {vyber_dog} & {vyber_kafe}. Vyzvednutí v {cas_vyzvednuti.strftime('%H:%M')} na adrese Kavárenská 42, ČB.")
        else:
            st.error("Chybka! Vyplň prosím jméno a telefon.")

# STRÁNKA: NABÍDKA
elif st.session_state.current_page == "📋 NABÍDKA":
    st.markdown("## 📋 Naše Kompletní Nabídka")
    st.write("Detailní složení našich sladkých hotdogů a výběrové kávy.")

    st.markdown("### 🌭 Sladké Bananadogy")

    # 1. OG Classic
    st.markdown('<div class="gastro-card">', unsafe_allow_html=True)
    col_img1, col_txt1 = st.columns([1, 2])
    with col_img1:
        st.image("https://unsplash.com")
    with col_txt1:
        st.markdown('<p class="gastro-title">🍫 The OG Classic</p>', unsafe_allow_html=True)
        st.markdown('<p class="gastro-desc">Naše vlajková loď. Dozlatova opečená máslová brioche bulka, teplý zralý banán, poctivá vrstva husté tekuté Nutelly, bohatě zasypaná drcenými Oreo sušenkami a jemný dotek mořské soli pro brutal zvýraznění všech sladkých tónů.</p>', unsafe_allow_html=True)
        st.markdown('<p class="gastro-price">115 Kč</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 2. Pink Special
    st.markdown('<div class="gastro-card">', unsafe_allow_html=True)
    col_img2, col_txt2 = st.columns([1, 2])
    with col_img2:
        st.image("https://unsplash.com")
    with col_txt2:
        st.markdown('<p class="gastro-title">🦩 Pink Special</p>', unsafe_allow_html=True)
        st.markdown('<p class="gastro-desc">Estetická bomba pro opravdové fajnšmekry. Teplý banán v nadýchaném brioche obalu, přelitý nadýchaným, lehce kyselkavým malinovým mousse topingem, dozdobený křupavými mini preclíky obalenými v našem domácím slaném karamelu.</p>', unsafe_allow_html=True)
        st.markdown('<p class="gastro-price">140 Kč</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 3. Lotus & Peanut
    st.markdown("""
        <div class="gastro-card">
            <div class="gastro-title">🥜 Lotus & Peanut</div>
            <div class="gastro-desc">Tekuté krémové arašídové máslo, jemný karamelový přeliv, položený na banánu a zasypaný tunou křupavých drcených sušenek Lotus Biscoff.</div>
            <div class="gastro-price">125 Kč</div>
        </div>
        <div class="gastro-card">
            <div class="gastro-title">🍓 White Berry</div>
            <div class="gastro-desc">Sametová poleva z bílé belgické čokolády, osvěžující kousky mrazem sušených jahod a jemně drcené máslové sušenky.</div>
            <div class="gastro-price">120 Kč</div>
        </div>

