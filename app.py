import streamlit as st

# Nastavení profesionálního zobrazení
st.set_page_config(
    page_title="Bananadog & Coffee",
    page_icon="🍌",
    layout="centered"
)

# --- STYLING (Kavárenské a banánové barvy) ---
st.markdown("""
    <style>
    .main { background-color: #fdfbf7; }
    h1 { color: #4e3629; font-family: 'Arial Black', sans-serif; }
    h2, h3 { color: #8d5b4c; }
    .stButton>button { background-color: #f4c430; color: #4e3629; font-weight: bold; border-radius: 20px; }
    </style>
""", unsafe_allow_html=True)

# --- HLAVNÍ BANNER ---
st.title("🍌 BANANADOG & COFFEE ☕")
st.markdown("## *Zapomeň na párek. Dej si banán v bulce!*")
st.write(
    "Jsme první **sladký hotdog pop-up** ve městě. Bereme čerstvé, nasládlé "
    "máslové brioche bulky, do nich dáváme akorát zralý banán a bombíme to brutal kombinacemi "
    "polév s drcenými sušenkami. K tomu ti vykouzlíme kafe z výběrových zrn z lokální pražírny."
)

st.divider()

# --- DIGITÁLNÍ MENU (CHUTNÁ SEKCE) ---
st.header("📋 Naše Brutal Menu")

tab_bananadogs, tab_coffee = st.tabs(["🌭 Bananadogs (Sladké hotdogy)", "☕ Výběrové Kafe"])

with tab_bananadogs:
    st.subheader("🔥 Teplé brioche bulky + čerstvý banán")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🍫 **The OG Classic** — 115 Kč")
        st.write("Zalitý tekutou **Nutellou**, zasypaný hromadou drcených **Oreo sušenek** a špetkou mořské soli pro zvýraznění chuti.")
        
        st.markdown("### 🥜 **Lotus & Peanut** — 125 Kč")
        st.write("Tekuté arašídové máslo, karamelový přeliv a zasypané křupavými drcenými sušenkami **Lotus Biscoff**.")
        
    with col2:
        st.markdown("### 🍓 **White Berry** — 120 Kč")
        st.write("Poleva z bílé belgické čokolády, lyofilizované (sušené) jahody a drcené maslové sušenky.")
        
        st.markdown("### 🥞 **Maple & Bacon (Guilty Pleasure)** — 135 Kč")
        st.write("Javorový sirup, sekané vlašské ořechy a navrch křupavá, dozlatova vypečená **slanina**. Sladko-slaná jízda!")

with tab_coffee:
    st.subheader("☕ Kafe, co tě nakopne")
    st.markdown("- **Espresso / Lungo** (100% Arabica, ovocnější profil) — 60 Kč")
    st.markdown("- **Batch Brew** (filtrované kafe, ideální k jídlu) — 65 Kč")
    st.markdown("- **Cappuccino** (sametová pěna z plnotučného mléka) — 75 Kč")
    st.markdown("- **Flat White** (dvojité espresso, méně mléka – silný prožitek) — 85 Kč")
    st.markdown("- **Ice Banana Latte** (ledové latte s domácím banánovým sirupem) — 95 Kč 🧊")

st.divider()

# --- INTERAKTIVNÍ OBJEDNÁVKA S SEBOU (Click & Collect) ---
st.header("🚀 Objednej si dopředu a nečekej frontu")
st.write("Nestíháš? Naklikej si svatou kombinaci teď hned a my ti ji připravíme přesně na čas do krabičky.")

with st.form("objednavka"):
    jmeno = st.text_input("Tvoje jméno:")
    telefon = st.text_input("Telefon (pro SMS o vyzvednutí):")
    
    vyber_dog = st.selectbox(
        "Který Bananadog ti nachystáme?",
        ["Žádný", "The OG Classic (Nutella + Oreo)", "Lotus & Peanut", "White Berry", "Maple & Bacon (Slanina)"]
    )
    
    vyber_kafe = st.selectbox(
        "A co k tomu na pití?",
        ["Žádné", "Espresso", "Batch Brew", "Cappuccino", "Flat White", "Ice Banana Latte"]
    )
    
    cas_vyzvednuti = st.time_input("Na kolik hodin si pro to skočíš?")
    poznamka = st.text_area("Nějaké úpravy? (Např. bez slaniny, ovesné mléko do kafe...)")
    
    potvrdit = st.form_submit_button("Odeslat objednávku do kuchyně")

if potvrdit:
    if jmeno and telefon and (vyber_dog != "Žádný" or vyber_kafe != "Žádné"):
        st.success(f"🎉 **Objednávka přijata, šéfe!**")
        st.balloons()
        st.write(f"Chystáme pro tebe: **{vyber_dog}** a **{vyber_kafe}**.")
        st.info(f"📍 Doraz v **{cas_vyzvednuti.strftime('%H:%M')}** do Kavárenské 42. Jakmile to bude horké v krabičce, pošleme ti SMS.")
    else:
        st.error("Vyplň prosím jméno, telefon a vyber si aspoň jedno jídlo nebo pití!")

# --- SIDEBAR INFO ---
st.sidebar.title("🍌 Bananadog")
st.sidebar.info("🔥 **DNEŠNÍ AKCE:** Při nákupu jakéhokoliv Bananadogu máš Batch Brew kafe jen za bůra (5 Kč)!")
st.sidebar.write("📍 **Adresa:** Kavárenská 42, Praha")
st.sidebar.write("🕒 **Dnes otevřeno:** 8:00 - 20:00")


