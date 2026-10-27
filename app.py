import streamlit as st
import time

# 1. Konfigurace stránky pro moderní zobrazení
st.set_page_config(
    page_title="BANANADOG & COFFEE",
    page_icon="🍌",
    layout="centered"
)

# 2. BRUTÁLNÍ DESIGN NA MÍRU (CSS Animace, Hover efekty, Sladěné barvy)
st.markdown("""
    <style>
    /* Plynulé načítání celého webu (Animace) */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .main .block-container {
        animation: fadeIn 1.2s ease-out;
    }

    /* Úprava pozadí a písma */
    .stApp {
        background-color: #111111; /* Moderní gastro tmavý režim */
        color: #f5f5f7;
    }

    /* Stylování hlavního nadpisu */
    .profi-title {
        font-family: 'Impact', 'Arial Black', sans-serif;
        font-size: 3.5rem;
        text-align: center;
        background: linear-gradient(45deg, #FFE135, #FFB300);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    
    .profi-subtitle {
        text-align: center;
        font-style: italic;
        color: #A0A0A5;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }

    /* Gastro karty produktů s animací při najetí (Hover) */
    .gastro-card {
        background: #1c1c1e;
        border: 1px solid #2c2c2e;
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 15px;
        transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
        cursor: pointer;
    }
    
    .gastro-card:hover {
        transform: scale(1.03);
        border-color: #FFE135;
        box-shadow: 0px 10px 25px rgba(255, 225, 53, 0.15);
    }
    
    .gastro-title {
        color: #FFE135;
        font-size: 1.4rem;
        font-weight: bold;
        margin-bottom: 5px;
    }
    
    .gastro-desc {
        color: #E5E5EA;
        font-size: 0.95rem;
    }
    
    .gastro-price {
        color: #FFB300;
        font-weight: bold;
        font-size: 1.1rem;
        margin-top: 10px;
        text-align: right;
    }

    /* Skrytí standardních ošklivých Streamlit prvků */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- HLAVNÍ NÁSTUP (ANIMOVANÝ BANNER) ---
st.markdown('<p class="profi-title">BANANADOG & COFFEE</p>', unsafe_allow_html=True)
st.markdown('<p class="profi-subtitle">🔥 Zapomeň na párek. Sladký hotdog pop-up z ČB! 🔥</p>', unsafe_allow_html=True)

st.write(
    "Vezmeme nadýchanou máslovou brioche bulku, opečeme ji, vložíme akorát zralý banán "
    "a zalijeme brutal kombinacemi polev a drcených sušenek. K tomu servírujeme brutal kafe z výběrové pražírny."
)

st.divider()

# --- PREMIÉROVÉ MENU (GASTRO KARTY S HOVER EFEKTEM) ---
st.markdown("## 📋 Naše Na Míru Vytvořené Menu")

kategorie = st.radio("Vyber si sekci:", ["🌭 Bananadogs (Sladké Hotdogy)", "☕ Výběrové Kafe"], horizontal=True)

if "Hotdogy" in kategorie:
    # Zobrazení Bananadogů přes designové karty
    st.markdown("""
        <div class="gastro-card">
            <div class="gastro-title">🍫 The OG Classic</div>
            <div class="gastro-desc">Teplá brioche bulka, čerstvý banán, poctivá dávka tekuté Nutelly, zasypané hromadou drcených Oreo sušenek a špetka mořské soli pro brutal zvýraznění chutí.</div>
            <div class="gastro-price">115 Kč</div>
        </div>
        
        <div class="gastro-card">
            <div class="gastro-title">🥜 Lotus & Peanut</div>
            <div class="gastro-desc">Tekuté krémové arašídové máslo, jemný slaný karamel, zasypané tunou křupavých drcených sušenek Lotus Biscoff. Křupavá závislost!</div>
            <div class="gastro-price">125 Kč</div>
        </div>
        
        <div class="gastro-card">
            <div class="gastro-title">🍓 White Berry</div>
            <div class="gastro-desc">Sametová poleva z bílé belgické čokolády, osvěžující kousky mrazem sušených (lyofilizovaných) jahod a drcené máslové sušenky.</div>
            <div class="gastro-price">120 Kč</div>
        </div>
        
        <div class="gastro-card">
            <div class="gastro-title">🥓 Maple & Bacon (Guilty Pleasure)</div>
            <div class="gastro-desc">Sladko-slaná jízda. Javorový sirup, drcené vlašské ořechy a navrch dokřupava vypečená, sekaná slanina. Totální úlet, který musíš zkusit.</div>
            <div class="gastro-price">135 Kč</div>
        </div>
    """, unsafe_allow_html=True)

else:
    # Zobrazení Kafe přes designové karty
    st.markdown("""
        <div class="gastro-card">
            <div class="gastro-title">☕ Flat White</div>
            <div class="gastro-desc">Dvojité espresso z výběrových zrn, jemně našlehané mikropěna. Silná kávová chuť ideální k sladkému dogu.</div>
            <div class="gastro-price">85 Kč</div>
        </div>
        
        <div class="gastro-card">
            <div class="gastro-title">🍌 Ice Banana Latte</div>
            <div class="gastro-desc">Ledové osvěžení. Naše espresso, vychlazené mléko, led a domácí banánový sirup, který si sami vaříme.</div>
            <div class="gastro-price">95 Kč</div>
        </div>
        
        <div class="gastro-card">
            <div class="gastro-title">🫗 Batch Brew</div>
            <div class="gastro-desc">Filtrovaná káva dne. Lehká, ovocná, skvěle se pije a doplňuje chuť Nutelly.</div>
            <div class="gastro-price">65 Kč</div>
        </div>
    """, unsafe_allow_html=True)

st.divider()

# --- CHYTRÝ OBJEDNÁVKOVÝ SYSTÉM S ANIMACÍ NAČÍTÁNÍ ---
st.markdown("## 🚀 Klikni & Vyzvedni (Click & Collect)")
st.write("Objednej si dopředu, my ti to připravíme horké přesně na čas do ruky.")

with st.form("profi_objednavka"):
    col_jmeno, col_tel = st.columns(2)
    with col_jmeno:
        jmeno = st.text_input("Tvoje jméno:")
    with col_tel:
        telefon = st.text_input("Tvůj telefon:")
        
    vyber_dog = st.selectbox(
        "Který Bananadog ti vyrobíme?",
        ["Žádný", "The OG Classic (Nutella + Oreo)", "Lotus & Peanut", "White Berry", "Maple & Bacon (Slanina)"]
    )
    
    vyber_kafe = st.selectbox(
        "Co k tomu na pití?",
        ["Žádné", "Flat White", "Ice Banana Latte", "Batch Brew"]
    )
    
    cas_vyzvednuti = st.time_input("V kolik hodin se zastavíš?")
    
    st.caption("Příprava trvá cca 7 minut od odeslání.")
    potvrdit = st.st.form_submit_button("🔥 ODESLAT OBJEDNÁVKU DO KUCHYNĚ 🔥")

# Animace zpracování objednávky
if potvrdit:
    if jmeno and telefon and (vyber_dog != "Žádný" or vyber_kafe != "Žádné"):
        # Vlastní barová animace načítání (progress bar)
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
            time.sleep(0.015) # Rychlá plynulá animace
            
        progress_bar.empty()
        status_text.empty()
        
        # Úspěch + Výstřel balónků
        st.success(f"🎉 **Objednávka proletěla až na bar, {jmeno}!**")
        st.balloons()
        
        st.markdown(f"""
            <div style="background: #2c2c2e; padding: 20px; border-radius: 12px; border-left: 5px solid #FFE135;">
                <b>Vezmeš si:</b> {vyber_dog} + {vyber_kafe}<br>
                <b>Čas předání:</b> {cas_vyzvednuti.strftime('%H:%M')}<br>
                <b>Místo:</b> Kavárenská 42, České Budějovice<br>
                <span style="color: #A0A0A5; font-size: 0.85rem;">Jakmile bulky vytáhneme z pece, pošleme ti SMS na {telefon}.</span>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.error("Chybka! Vyplň prosím jméno, telefon a vyber si aspoň jednoho doga nebo kafe.")

# --- SIDEBAR (INFOPANEL) ---
st.sidebar.markdown('<p style="font-size: 1.5rem; font-weight: bold; color: #FFE135;">🍌 Bananadog Pop-Up</p>', unsafe_allow_html=True)
st.sidebar.write("📍 **Kde:** Kavárenská 42, České Budějovice")
st.sidebar.write("🕒 **Dnes makáme:** 8:00 - 20:00")
st.sidebar.divider()
st.sidebar.warning("⚡ **Dnešní drop:** Slaná limitka Maple & Bacon zbývá posledních 15 kusů!")
