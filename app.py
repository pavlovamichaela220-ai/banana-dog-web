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

# 2. DESIGN NA MÍRU + STYL PRO SAMOLEPKU
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
    letter-spacing: 1px !important;
    border-radius: 12px !important;
    padding: 10px 20px !important;
    width: 100% !important;
}

.stButton>button:hover {
    background-color: #E6D592 !important;
}

/* Stylování pro aesthetic samolepku na kraji fotky */
.image-container {
    position: relative;
    width: 100%;
    margin-bottom: 20px;
}

.main-sketch-image {
    width: 100%;
    border-radius: 12px;
    display: block;
}

.aesthetic-sticker {
    position: absolute;
    bottom: -30px;
    left: -25px;
    width: 35%;
    transform: rotate(-12deg);
    filter: drop-shadow(0px 10px 15px rgba(0,0,0,0.5));
    z-index: 10;
    transition: transform 0.3s ease;
}

.aesthetic-sticker:hover {
    transform: rotate(-5deg) scale(1.05);
}

[data-testid="stSidebar"] { display: none !important; }
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# --- TITUL WEBU ---
st.markdown('<p class="profi-title">BANANADOG<br>& COFFEE</p>', unsafe_allow_html=True)
st.markdown('<p class="profi-subtitle">⚡ ZAPOMEŇ NA PÁREK. SLADKÝ POP-UP Z ČB ⚡</p>', unsafe_allow_html=True)

# --- NAVIGAČNÍ PANEL ---
nav_col1, nav_col2, nav_col3, nav_col4 = st.columns(4)

with nav_col1:
    st.button("🏠 MAIN PAGE", on_click=set_page, args=("🏠 MAIN PAGE",))
with nav_col2:
    st.button("📋 NABÍDKA", on_click=set_page, args=("📋 NABÍDKA",))
with nav_col3:
    st.button("📸 GALLERY", on_click=set_page, args=("📸 GALLERY",))
with nav_col4:
    st.button("✨ ORIGIN STORY", on_click=set_page, args=("✨ ORIGIN STORY",))

st.divider()

# ==========================================
# STRÁNKA 1: MAIN PAGE
# ==========================================
if st.session_state.current_page == "🏠 MAIN PAGE":
    sketch_path = "bananadog.png"
    sticker_path = "sticker.png"
    
    # Zobrazení fotky se samolepkou přes HTML/CSS overlay
    if os.path.exists(sketch_path):
        import base64
        
        def get_base64_image(image_path):
            if os.path.exists(image_path):
                with open(image_path, "rb") as img_file:
                    return base64.b64encode(img_file.read()).decode("utf-8")
            return ""

        sketch_base64 = get_base64_image(sketch_path)
        sticker_base64 = get_base64_image(sticker_path)
        
        # HTML struktura pro překrytí samolepky přes fotografii
        html_code = f"""
        <div class="image-container">
            <img src="data:image/png;base64,{sketch_base64}" class="main-sketch-image" alt="BANANADOG & COFFEE Concept">
        """
        
        if sticker_base64:
            html_code += f"""
            <img src="data:image/png;base64,{sticker_base64}" class="aesthetic-sticker" alt="Bananadog Sticker">
            """
            
        html_code += "</div>"
        st.markdown(html_code, unsafe_allow_html=True)
    else:
        st.info("💡 Nahraj prosím soubory 'bananadog.png' a 'sticker.png' do kořenové složky na GitHubu.")
    
    st.write("Máslová brioche bulka, grilovaný banán, brutal topingy a výběrové kafe v dravém streetwearovém podání. Přijď ochutnat do našeho budějovického pop-upu!")
    st.divider()
    
    st.markdown("## 🔥 Our Bestsellers")
    st.write("Tohle lidi v ČB milují nejvíc. Najjeď na kartu myší a zažij ten glow!")
    
    st.markdown("""
    <div class="gastro-card">
        <div class="gastro-title">🍫 The OG Classic</div>
        <div class="gastro-desc">Máslová brioška, teplý banán, Nutella, brutal nálož drcených Oreo sušenek a špetka mořské soli. Svatá gastro trojice.</div>
        <div class="gastro-price">115 Kč</div>
    </div>
    <div class="gastro-card">
        <div class="gastro-title">🦩 Pink Special</div>
        <div class="gastro-desc">Náš nový estetický drop. Malinový mousse toping, křupavé mini preclíky v domácím slaném karamelu. Totální chic závislost.</div>
        <div class="gastro-price">140 Kč</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    st.markdown("## 🚀 Klikni & Vyzvedni (Click & Collect)")
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
            progress_bar = st.progress(0)
            for percent_complete in range(100):
                time.sleep(0.005)
                progress_bar.progress(percent_complete + 1)
            progress_bar.empty()
            st.success(f"🎉 **Objednávka proklouzla na bar, {jmeno}!**")
            st.balloons()
            st.info(f"Chystáme pro tebe: {vyber_dog} a {vyber_kafe} na {cas.strftime('%H:%M')} do Kavárenské 42, ČB.")
        else:
            st.error("Vyplň prosím jméno a telefon!")

# ==========================================
# STRÁNKA 2: NABÍDKA
# ==========================================
elif st.session_state.current_page == "📋 NABÍDKA":
    st.markdown("## 📋 Naše Kompletní Nabídka")
    st.write("Detailní složení našich sladkých hotdogů a výběrové kávy.")
    
    st.markdown("### 🌭 Sladké Bananadogy")
    st.markdown("""
    <div class="gastro-card">
        <div class="gastro-title">🍫 The OG Classic — 115 Kč</div>
        <div class="gastro-desc">Dozlatova opečená máslová brioche bulka, teplý zralý banán, poctivá vrstva husté tekuté Nutelly, bohatě zasypaná drcenými Oreo sušenkami a jemný dotek mořské soli.</div>
    </div>
    <div class="gastro-card">
        <div class="gastro-title">🦩 Pink Special — 140 Kč</div>
        <div class="gastro-desc">Teplý banán v nadýchaném brioche obalu, přelitý nadýchaným, lehce kyselkavým malinovým mousse topingem, dozdobený křupavými mini preclíky v domácím slaném karamelu.</div>
    </div>
    <div class="gastro-card">
        <div class="gastro-title">🥜 Lotus & Peanut — 125 Kč</div>
        <div class="gastro-desc">Tekuté arašídové máslo, jemný karamelový přeliv, položený na banánu a drcené sušenky Lotus Biscoff.</div>
    </div>
    <div class="gastro-card">
        <div class="gastro-title">🍓 White Berry — 120 Kč</div>
        <div class="gastro-desc">Poleva z bílé belgické čokolády, mrazem sušené jahody a drcené máslové sušenky.</div>
    </div>
    <div class="gastro-card">
        <div class="gastro-title">🥓 Maple & Bacon — 135 Kč</div>
        <div class="gastro-desc">Javorový sirup, drcené vlašské ořechy a navrch dokřupava vypečená, sekaná slanina. Sladko-slaná bomba.</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    st.markdown("### ☕ Výběrové Kafe")
    st.write("- **Flat White** (Dvojité espresso, sametová mikropěna) — 85 Kč")
    st.write("- **Ice Banana Latte** (Ledové espresso s naším banánovým sirupem) — 95 Kč")
    st.write("- **Batch Brew** (Filtrovaná káva dne, fresh profil) — 65 Kč")

# ==========================================
# STRÁNKA 3: GALLERY
# ==========================================
elif st.session_state.current_page == "📸 GALLERY":
    st.markdown("## 📸 Bananadog Gallery")
    st.write("Atmosféra z našeho budějovického pop-upu a happy hour zážitky.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://images.unsplash.com/photo-1555396273-367ea4eb4db5", caption="Vezmi partu ven — sk
                 
