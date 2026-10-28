import streamlit as st
import time

# 1. Konfigurace stránky pro moderní zobrazení
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

    /* Úprava klasických Streamlit nadpisů (H1, H2, H3) na máslově žlutou */
    h1, h2, h3, [data-testid="stMarkdownContainer"] h2 {
        color: #F3E5AB !important;
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 800 !important;
    }

    /* Gastro karty produktů s jemnou animací */
    .gastro-card {
        background: #261d1a; /* O něco světlejší studená hnědá pro kontrast karet */
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
        color: #F3E5AB; /* Máslově žluté názvy jídel */
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
        background-color: #F3E5AB !important; /* Máslové tlačítko */
        color: #1a1412 !important; /* Tmavě hnědý text uvnitř */
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


# --- CHIC EMBEDDED OBRÁZEK (CHYTRÝ POP-UP CONCEPT) ---
# Použití elegantního, minimalistického uměleckého konceptu bista (espresso tóny s teplým neonem)
header_image = "https://unsplash.com"
st.image(header_image, caption="BANANADOG & COFFEE — Budějovický Pop-Up Concept v minimalistickém stylu.", use_container_width=True)


# --- HLAVNÍ SEKCE STRÁNKY ---
st.markdown('<p class="profi-title">BANANADOG<br>& COFFEE</p>', unsafe_allow_html=True)
st.markdown('<p class="profi-subtitle">⚡ ZAPOMEŇ NA PÁREK. SLADKÝ POP-UP Z ČB ⚡</p>', unsafe_allow_html=True)

st.write(
    "Vezmeme nadýchanou máslovou brioche bulku, opečeme ji na grilu, vložíme čerstvý, "
    "akorát zralý banán a bombíme ho brutal autorskými kombinacemi krémů a posypů. "
    "K tomu ti vykouzlíme bezchybný kofeinový zážitek z výběrových kávových zrn."
)

st.divider()

# --- PREMIÉROVÉ MENU ---
st.markdown("## 📋 Naše Menu")

kategorie = st.radio("Vyber si sekci:", ["🌭 Bananadogs (Sladké Hotdogy)", "☕ Výběrové Kafe"], horizontal=True)

if "Hotdogy" in kategorie:
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
        
        <div class="gastro-card">
            <div class="gastro-title">🫗 Batch Brew</div>
            <div class="gastro-desc">Filtrovaná káva dne s lehkým, čistým a ovocným kávovým profilem. Ideální fresh společník k prolití Nutelly.</div>
            <div class="gastro-price">65 Kč</div>
        </div>
    """, unsafe_allow_html=True)

st.divider()

# --- OBJEDNÁVKOVÝ SYSTÉM ---
st.markdown("## 🚀 Klikni & Vyzvedni (Click & Collect)")
st.write("Objednej si dopředu, my ti to připravíme horké přesně na tvůj čas.")

with st.form("profi_objednavka"):
    col_jmeno, col_tel = st.columns(2)
    with col_jmeno:
        jmeno = st.text_input("Tvoje jméno:")
    with col_tel:
        telefon = st.text_input("Tvůj telefon:")
        
    vyber_dog = st.selectbox(
        "Který Bananadog ti vyrobíme?",
        ["Žádný", "The OG Classic (Nutella + Oreo)", "Pink Special (Malina + Preclíky)", "Lotus & Peanut", "White Berry"]
    )
    
    vyber_kafe = st.selectbox(
        "Co k tomu na pití?",
        ["Žádné", "Flat White", "Ice Banana Latte", "Batch Brew"]
    )
    
    cas_vyzvednuti = st.time_input("V kolik hodin se zastavíš?")
    
    st.caption("Příprava trvá cca 7 minut od odeslání.")
    potvrdit = st.form_submit_button("✨ ODESLAT OBJEDNÁVKU DO KUCHYNĚ ✨")

# Animace zpracování objednávky
if potvrdit:
    if jmeno and telefon and (vyber_dog != "Žádný" or vyber_kafe != "Žádné"):
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i in range(100):
            progress_bar.progress(i + 1)
            if i < 30:
                status_text.text("Connecting to kitchen terminal...")
            elif i < 70:
                status_text.text("Odesílám specifikace kuchaři do ČB... 🍌")
            else:
                status_text.text("Generuji potvrzení a tisk lístku... 🎫")
            time.sleep(0.012)
            
        progress_bar.empty()
        status_text.empty()
        
        st.success(f"🎉 **Objednávka proklouzla na bar, {jmeno}!**")
        st.balloons()
        
        st.markdown(f"""
            <div style="background: #261d1a; padding: 20px; border-radius: 12px; border-left: 5px solid #F3E5AB; font-family: 'Space Grotesk', sans-serif;">
                <b>Vezmeš si:</b> {vyber_dog} + {vyber_kafe}<br>
                <b>Čas předání:</b> {cas_vyzvednuti.strftime('%H:%M')}<br>
                <b>Místo:</b> Kavárenská 42, České Budějovice<br>
