import streamlit as st
import time

# 1. Nastaveni stranky
st.set_page_config(
    page_title="BANANADOG & COFFEE",
    page_icon="🍌",
    layout="centered"
)

# 2. CHIC DESIGN NA MÍRU (Cold Espresso Brown pozadí, Butter Yellow nadpisy)
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
    }

    /* Globální úprava pozadí celé aplikace */
    .stApp {
        background-color: #1a1412; /* Studené hluboké hnědé pozadí */
        color: #f4ece8; /* Soft krémový text pro snadnou čitelnost */
    }

    /* Úprava barvy boční lišty (Sidebar) na studenou kávovou hnědou */
    [data-testid="stSidebar"] {
        background-color: #211917 !important;
        border-right: 1px solid #332723;
    }
    
    [data-testid="stSidebar"] * {
        color: #f4ece8 !important;
        font-family: 'Space Grotesk', sans-serif !important;
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
        margin-top: 1.5rem;
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

    h1, h2, h3, [data-testid="stMarkdownContainer"] h2, [data-testid="stSidebar"] h3 {
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

    /* Prémiové minimalistické tlačítko */
    .stButton>button {
        background-color: #F3E5AB !important; 
        color: #1a1412 !important; 
        border: none !important;
        font-weight: 700 !important;
        font-family: 'Space Grotesk', sans-serif !important;
        text-transform: uppercase !important;
        letter-spacing: 2px !important;
        border-radius: 12px !important;
        padding: 12px 30px !important;
        width: 100% !important;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #E6D592 !important;
        transform: translateY(-1px);
    }

    /* Skrytí standardních prvků Streamlitu */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- BOČNÍ PANEL S NABÍDKOU STRÁNEK (NAVIGATION SIDEBAR) ---
st.sidebar.markdown('### 🧭 NAVIGACE')
stranka = st.sidebar.radio(
    "Přejít na sekci:",
    ["🏠 Domů & Objednávka", "📋 Podrobná Nabídka", "📸 Gallery", "✨ O Nás"]
)

st.sidebar.divider()
st.sidebar.markdown('### 🤎 BANANADOG ČB')
st.sidebar.write("📍 Kavárenská 42, ČB")
st.sidebar.write("🕒 Otevřeno: 8:00 - 20:00")


# ==========================================
# SEKCE 1: DOMŮ & RYCHLÁ OBJEDNÁVKA
# ==========================================
if stranka == "🏠 Domů & Objednávka":
    st.markdown('<p class="profi-title">BANANADOG<br>& COFFEE</p>', unsafe_allow_html=True)
    st.markdown('<p class="profi-subtitle">⚡ ZAPOMEŇ NA PÁREK. SLADKÝ POP-UP Z ČB ⚡</p>', unsafe_allow_html=True)

    st.image("https://streamlit.io", use_container_width=True)

    st.write(
        "Vezmeme nadýchanou máslovou brioche bulku, opečeme ji na grilu, vložíme čerstvý banán "
        "a zasypeme ho brutal autorskými kombinacemi krémů a posypů. "
        "Objednej si dopředu přes formulář níže a nečekej frontu!"
    )

    st.divider()
    st.markdown("## 🚀 Klikni & Vyzvedni (Click & Collect)")
    
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
        potvrdit = st.form_submit_button("✨ ODESLAT OBJEDNÁVKU DO KUCHYNĚ ✨")

    if potvrdit:
        if jmeno and telefon:
            progress_bar = st.progress(0)
            status_text = st.empty()
            for percent_complete in range(100):
                time.sleep(0.005)
                progress_bar.progress(percent_complete + 1)
                status_text.text(f"Odesílám na bar: {percent_complete + 1}%")
            progress_bar.empty()
            status_text.empty()
            
            st.success(f"🎉 **Objednávka proklouzla na bar, {jmeno}!**")
            st.balloons()
            st.info(f"Chystáme: {vyber_dog} & {vyber_kafe}. Vyzvednutí v {cas_vyzvednuti.strftime('%H:%M')} na adrese Kavárenská 42, ČB.")
        else:
            st.error("Chybka! Vyplň prosím jméno a telefon.")


# ==========================================
# SEKCE 2: PODROBNÁ NABÍDKA S FOTKAMI PRODUKTŮ
# ==========================================
elif stranka == "📋 Podrobná Nabídka":
    st.markdown("## 📋 Naše Kompletní Nabídka")
    st.write("Podívej se na detailní složení našich sladkých hotdogů a výběrové kávy.")

    st.markdown("### 🌭 Sladké Bananadogy")

    # 1. OG Classic
    st.markdown('<div class="gastro-card">', unsafe_allow_html=True)
    col_img1, col_txt1 = st.columns()
    with col_img1:
        st.image("https://unsplash.com", caption="🍫 The OG")
    with col_txt1:
        st.markdown('<p class="gastro-title">The OG Classic</p>', unsafe_allow_html=True)
        st.markdown('<p class="gastro-desc">Naše vlajková loď. Dozlatova opečená máslová brioche bulka, teplý zralý banán, poctivá vrstva husté tekuté Nutelly, bohatě zasypaná drcenými Oreo sušenkami a jemný dotek mořské soli pro brutal zvýraznění všech sladkých tónů.</p>', unsafe_allow_html=True)
        st.markdown('<p class="gastro-price">115 Kč</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 2. Pink Special
    st.markdown('<div class="gastro-card">', unsafe_allow_html=True)
    col_img2, col_txt2 = st.columns()
    with col_img2:
        st.image("https://unsplash.com", caption="🦩 Pink Special")
    with col_txt2:
        st.markdown('<p class="gastro-title">Pink Special</p>', unsafe_allow_html=True)
        st.markdown('<p class="gastro-desc">Estetická bomba pro opravdové fajnšmekry. Teplý banán v nadýchaném brioche obalu, přelitý nadýchaným, lehce kyselkavým malinovým mousse topingem, dozdobený křupavými mini preclíky obalenými v našem domácím slaném karamelu.</p>', unsafe_allow_html=True)
        st.markdown('<p class="gastro-price">140 Kč</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 3. Lotus & Peanut
    st.markdown('<div class="gastro-card">', unsafe_allow_html=True)
    st.markdown('<p class="gastro-title">🥜 Lotus & Peanut</p>', unsafe_allow_html=True)
    st.markdown('<p class="gastro-desc">Tekuté krémové arašídové máslo, jemný karamelový přeliv, položený na banánu a zasypaný tunou křupavých drcených sušenek Lotus Biscoff.</p>', unsafe_allow_html=True)
    st.markdown('<p class="gastro-price">125 Kč</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 4. White Berry
    st.markdown('<div class="gastro-card">', unsafe_allow_html=True)
    st.markdown('<p class="gastro-title">🍓 White Berry</p>', unsafe_allow_html=True)
    st.markdown('<p class="gastro-desc">Sametová poleva z bílé belgické čokolády, osvěžující kousky mrazem sušených jahod a jemně drcené máslové sušenky.</p>', unsafe_allow_html=True)
    st.markdown('<p class="gastro-price">120 Kč</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 5. Maple & Bacon
