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

# Funkce pro převod obrázku na base64
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode("utf-8")
    return ""

# 2. DESIGN NA MÍRU (VELKÝ NADPIS, HOVER EFEKTY A PŘETÉKAJÍCÍ SAMOLEPKA)
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
    letter-spacing: 1px !important;
    border-radius: 12px !important;
    padding: 10px 20px !important;
    width: 100% !important;
    transition: all 0.3s ease-in-out !important;
}

.stButton>button:hover {
    background-color: #ffffff !important;
    color: #1a1412 !important;
    transform: translateY(-3px) scale(1.02) !important;
    box-shadow: 0px 10px 25px rgba(243, 229, 171, 0.4) !important;
}

.image-wrapper {
    position: relative;
    width: 100%;
    margin-top: 20px;
    margin-bottom: 40px;
}

.main-sketch {
    width: 100%;
    border-radius: 16px;
    display: block;
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
}

.aesthetic-sticker {
    position: absolute;
    bottom: -35px;
    left: -30px;
    width: 35%;
    transform: rotate(-12deg);
    filter: drop-shadow(0 10px 15px rgba(0,0,0,0.6));
    z-index: 10;
}

[data-testid="stSidebar"] { display: none !important; }
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(css_styles, unsafe_allow_html=True)

# --- TITUL WEBU ---
st.markdown('<p class="profi-title">BANANADOG<br>& COFFEE</p>', unsafe_allow_html=True)
st.markdown('<p class="profi-subtitle">⚡ ZAPOMEŇ NA PÁREK. SLADKÝ POP-UP Z ČB ⚡</p>', unsafe_allow_html=True)

# --- NAVIGAČNÍ PANEL ---
nav_col1, nav_col2, nav_col3, nav_col4 = st.columns(4)

with nav_col1:
    if st.button("🏠 MAIN PAGE"):
        set_page("main")
        st.rerun()
with nav_col2:
    if st.button("📋 NABÍDKA"):
        set_page("nabidka")
        st.rerun()
with nav_col3:
    if st.button("📸 GALLERY"):
        set_page("gallery")
        st.rerun()
with nav_col4:
    if st.button("✨ ORIGIN STORY"):
        set_page("origin")
        st.rerun()

st.divider()

# ==========================================
# STRÁNKA 1: MAIN PAGE
# ==========================================
if st.session_state.current_page == "main":
    sketch_path = "bananadog.png"
    sticker_path = "sticker.png"
    
    sketch_base64 = get_base64_image(sketch_path)
    sticker_base64 = get_base64_image(sticker_path)
    
    if sketch_base64 and sticker_base64:
        html_content = f"""
        <div class="image-wrapper">
            <img src="data:image/png;base64,{sketch_base64}" class="main-sketch" alt="Bananadog Concept">
            <img src="data:image/png;base64,{sticker_base64}" class="aesthetic-sticker" alt="Sticker">
        </div>
        """
        st.markdown(html_content, unsafe_allow_html=True)
    else:
        if os.path.exists(sketch_path):
            st.image(sketch_path, use_container_width=True)
        else:
            st.info("💡 Nahraj soubor 'bananadog.png' do GitHubu.")
        if os.path.exists(sticker_path):
            st.image(sticker_path, width=200)
        else:
            st.warning("💡 Nahraj soubor 'sticker.png' do GitHubu.")

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
    
    jmeno = st.text_input("Jméno:")
    telefon = st.text_input("Telefon:")
    vyber_dog = st.selectbox("Bananadog:", ["Žádný", "The OG Classic", "Pink Special", "Lotus & Peanut", "White Berry", "Maple & Bacon"])
    vyber_kafe = st.selectbox("Kafe:", ["Žádné", "Flat White", "Ice Banana Latte", "Batch Brew"])
    cas = st.time_input("Čas vyzvednutí:")
    
    if st.button("🔥 ODESLAT OBJEDNÁVKU DO KUCHYNĚ 🔥"):
        if jmeno and telefon:
            progress_bar = st.progress(0)
            for percent_complete in range(100):
                time.sleep(0.005)
                progress_bar.progress(percent_complete + 1)
            progress_bar.empty()
            st.success(f"🎉 **Objednávka proklouzla na bar, {jmeno}!**")
            st.balloons()
            cas_str = cas.strftime('%H:%M') if hasattr(cas, 'strftime') else str(cas)
            st.info(f"Chystáme pro tebe: {vyber_dog} a {vyber_kafe} na {cas_str} do Kavárenské 42, ČB.")
        else:
            st.error("Vyplň prosím jméno a telefon!")

# ==========================================
# STRÁNKA 2: NABÍDKA
# ==========================================
elif st.session_state.current_page == "nabidka":
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
elif st.session_state.current_page == "gallery":
    st.markdown("## 📸 Bananadog Gallery")
    st.write("Atmosféra z našeho budějovického pop-upu a happy hour zážitky.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://images.unsplash.com/photo-1555396273-367ea4eb4db5", caption="Vezmi partu ven — skvělá atmosféra a zážitek u našeho pop-upu.")
        st.image("https://images.unsplash.com/photo-1541544741938-0af808871cc0", caption="Happy Hour každý den od 15:00 do 17:00: Dva bananadogy a drink za 299 Kč!")
    with col2:
        st.image("https://images.unsplash.com/photo-1509722747041-616f39b57569", caption="Detailní pohled na naše legendární kousky plné chuti.")
        st.image("https://images.unsplash.com/photo-1495474472287-4d71bcdd2085", caption="Čerstvě namletá výběrová káva k dokonalému sladkému zážitku.")

# ==========================================
# STRÁNKA 4: ORIGIN STORY
# ==========================================
elif st.session_state.current_page == "origin":
    st.markdown("## ✨ Naše Origin Story")
    st.write("Všechno to začalo jedním bláznivým nápadem v Českých Budějovicích: **Proč by měl být hotdog vždycky jenom slaný s párkem?**")
    st.write("Rozhodli jsme se to otočit vzhůru nohama. Vzali jsme nadýchanou máslovou briošku, přidali grilovaný banán a spojili to s těmi nejlepšími surovinami, které máme sami rádi.")
    st.write("Výsledkem je dravý streetwearový pop-up concept **BANANADOG & COFFEE**, který boří mýty o klasickém fastfoodu. Přijď za námi ochutnat kus téhle sladké revoluce! 🔥")
