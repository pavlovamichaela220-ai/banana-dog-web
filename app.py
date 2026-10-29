import streamlit as st
import time
import os
import base64

st.set_page_config(
    page_title="BANANADOG & COFFEE",
    page_icon="🍌",
    layout="centered"
)

if "current_page" not in st.session_state:
    st.session_state.current_page = "main"

if "cart" not in st.session_state:
    st.session_state.cart = []

def set_page(page_name):
    st.session_state.current_page = page_name

def add_to_cart(item_name, price):
    st.session_state.cart.append({"name": item_name, "price": price})
    st.toast(f"Přihozeno do košíku: {item_name}! 🍌", icon="🛒")

def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode("utf-8")
    return ""

css_styles = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@800;900&family=Space+Grotesk:wght@400;700&display=swap');

@keyframes slideFromLeft {
    0% { opacity: 0; transform: translateX(-350px); }
    100% { opacity: 1; transform: translateX(0); }
}

@keyframes slideFromRight {
    0% { opacity: 0; transform: translateX(350px); }
    100% { opacity: 1; transform: translateX(0); }
}

.main .block-container {
    font-family: 'Space Grotesk', sans-serif;
    background: rgba(30, 23, 20, 0.95);
    padding: 24px !important;
    border-radius: 24px !important;
    border: 3px solid #F3E5AB !important;
    box-shadow: 0px 0px 30px rgba(243, 229, 171, 0.35), 0px 20px 50px rgba(0,0,0,0.8) !important;
    margin-top: 1rem;
    margin-bottom: 2rem;
}

.stApp {
    background-color: #1a1412;
    color: #f4ece8;
}

/* STYLOVÉ ŽLUTÉ HORIZONTÁLNÍ ČÁRY */
.neon-hr {
    border: none;
    height: 3px;
    background: #F3E5AB;
    box-shadow: 0 0 10px #F3E5AB;
    margin: 15px 0;
}

.title-left {
    font-family: 'Montserrat', sans-serif;
    font-weight: 900;
    font-size: 5rem !important;
    text-align: center;
    line-height: 0.85;
    letter-spacing: -3px;
    color: #F3E5AB;
    margin: 0;
    text-shadow: 0 10px 30px rgba(0,0,0,0.5);
    animation: slideFromLeft 1.4s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

.title-right {
    font-family: 'Montserrat', sans-serif;
    font-weight: 900;
    font-size: 5rem !important;
    text-align: center;
    line-height: 0.85;
    letter-spacing: -3px;
    color: #F3E5AB;
    margin: 0 0 0.2rem 0;
    text-shadow: 0 10px 30px rgba(0,0,0,0.5);
    animation: slideFromRight 1.4s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

.profi-subtitle {
    font-family: 'Space Grotesk', sans-serif;
    text-align: center;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 6px;
    color: #E6D592;
    font-size: 1.05rem;
    margin-bottom: 1.2rem;
}

h1, h2, h3 {
    color: #F3E5AB !important;
    font-family: 'Montserrat', sans-serif !important;
    font-weight: 800 !important;
}

/* GASTRO KARTY SE ŽLUTÝM RÁMEČKEM */
.gastro-card {
    position: relative;
    background: #261d1a;
    border: 2px solid #F3E5AB !important;
    border-radius: 16px;
    padding: 22px;
    margin-bottom: 16px;
    font-family: 'Space Grotesk', sans-serif;
    transition: all 0.3s ease-in-out;
}

.gastro-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 0 25px rgba(243, 229, 171, 0.6) !important;
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

[data-testid="stSidebar"] { display: none !important; }
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header { visibility: hidden; }
</style>
"""
st.markdown(css_styles, unsafe_allow_html=True)

# --- TOP LIŠTA S KOŠÍKEM ---
cart_count = len(st.session_state.cart)
cart_total = sum([item["price"] for item in st.session_state.cart])

top_col1, top_col2 = st.columns([3, 1])
with top_col2:
    if st.button(f"🛒 Košík ({cart_count}) — {cart_total} Kč"):
        set_page("cart")
        st.rerun()

# --- 1. HORIZONTÁLNÍ ČÁRA PŘED HLAVNÍM NADPISEM ---
st.markdown('<hr class="neon-hr">', unsafe_allow_html=True)

# --- ANIMOVANÝ HLAVNÍ NADPIS A PODNADPIS ---
st.markdown('<p class="title-left">BANANADOG</p>', unsafe_allow_html=True)
st.markdown('<p class="title-right">& COFFEE</p>', unsafe_allow_html=True)
st.markdown('<p class="profi-subtitle">⚡ ZAPOMEŇ NA PÁREK. SLADKÝ POP-UP Z ČB ⚡</p>', unsafe_allow_html=True)

# --- 2. HORIZONTÁLNÍ ČÁRA ZA PODNADISEM (PŘED BANNEREM) ---
st.markdown('<hr class="neon-hr">', unsafe_allow_html=True)

# --- PANORAMATICKÝ BANNER ---
sketch_path = "bananadog.png"
sticker_path = "sticker.png"

sketch_base64 = get_base64_image(sketch_path)
sticker_base64 = get_base64_image(sticker_path)

if sketch_base64 and sticker_base64:
    banner_html = f'''
    <div style="position: relative; width: 100%; height: 210px; overflow: hidden; border-radius: 16px; margin-bottom: 25px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); border: 2px solid #F3E5AB;">
        <img src="data:image/png;base64,{sketch_base64}" style="width: 100%; height: 100%; object-fit: cover; display: block;" alt="Bananadog Banner">
        <img src="data:image/png;base64,{sticker_base64}" style="position: absolute; bottom: 10px; right: 15px; width: 22%; transform: rotate(-10deg); filter: drop-shadow(0 8px 12px rgba(0,0,0,0.7)); z-index: 10;" alt="Sticker">
    </div>
    '''
    st.markdown(banner_html, unsafe_allow_html=True)
else:
    if os.path.exists(sketch_path):
        st.image(sketch_path, use_container_width=True)
    else:
        st.info("💡 Nahraj soubor 'bananadog.png' do GitHubu.")

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
# ROZCESTNÍK PODLE STAVU STRÁNKY
# ==========================================

if st.session_state.current_page == "main":
    desc_main = "Máslová brioche bulka, grilovaný banán, brutal topingy a výběrové kafe v dravém streetwearovém podání. Přijď ochutnat do našeho budějovického pop-upu!"
    st.write(desc_main)
    st.divider()
    
    bestsellers_title = "## 🔥 Our Bestsellers"
    st.markdown(bestsellers_title, unsafe_allow_html=True)
    st.write("Tohle lidi v ČB milují nejvíc:")
    
    c_og = '''<div class="gastro-card"><div class="gastro-title">🍫 The OG Classic</div><div class="gastro-desc">Máslová brioška, teplý banán, Nutella, brutal nálož drcených Oreo sušenek a špetka mořské soli. Svatá gastro trojice.</div><div class="gastro-price">115 Kč</div></div>'''
    st.markdown(c_og, unsafe_allow_html=True)
    
    c_pink = '''<div class="gastro-card"><div class="gastro-title">🦩 Pink Special</div><div class="gastro-desc">Náš nový estetický drop. Malinový mousse toping, křupavé mini preclíky v domácím slaném karamelu. Totální chic závislost.</div><div class="gastro-price">140 Kč</div></div>'''
    st.markdown(c_pink, unsafe_allow_html=True)
    
    st.divider()
    st.markdown("## 🚀 Rychlá Objednávka")
    
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

elif st.session_state.current_page == "nabidka":
    st.markdown("## 📋 Naše Kompletní Nabídka")
    st.write("Kliknutím na tlačítko u produktu si ho hned hodíš do virtuálního košíku.")
    
    st.markdown("### 🌭 Sladké Bananadogy")
    
    st.markdown('''<div class="gastro-card"><div class="gastro-title">🍫 The OG Classic</div><div class="gastro-desc">Dozlatova opečená máslová brioche bulka, teplý zralý banán, poctivá vrstva husté tekuté Nutelly, bohatě zasypaná drcenými Oreo sušenkami a jemný dotek mořské soli.</div><div class="gastro-price">115 Kč</div></div>''', unsafe_allow_html=True)
    if st.button("✨ Přidat The OG Classic do košíku", key="add_og"):
        add_to_cart("The OG Classic", 115)
        st.rerun()

    st.markdown('''<div class="gastro-card"><div class="gastro-title">🦩 Pink Special</div><div class="gastro-desc">Teplý banán v nadýchaném brioche obalu, přelitý nadýchaným, lehce kyselkavým malinovým mousse topingem, dozdobený křupavými mini preclíky v domácím slaném karamelu.</div><div class="gastro-price">140 Kč</div></div>''', unsafe_allow_html=True)
    if st.button("✨ Přidat Pink Special do košíku", key="add_pink"):
        add_to_cart("Pink Special", 140)
        st.rerun()

    st.markdown('''<div class="gastro-card"><div class="gastro-title">🥜 Lotus & Peanut</div><div class="gastro-desc">Tekuté arašídové máslo, jemný karamelový přeliv, položený na banánu a drcené sušenky Lotus Biscoff.</div><div class="gastro-price">125 Kč</div></div>''', unsafe_allow_html=True)
    if st.button("✨ Přidat Lotus & Peanut do košíku", key="add_lotus"):
        add_to_cart("Lotus & Peanut", 125)
        st.rerun()

    st.markdown('''<div class="gastro-card"><div class="gastro-title">🍓 White Berry</div><div class="gastro-desc">Poleva z bílé belgické č
