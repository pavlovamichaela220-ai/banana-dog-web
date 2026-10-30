import streamlit as st
import time
import os
import base64
import random
import string
import streamlit.components.v1 as components

st.set_page_config(pagetitle="BANANADOG & COFFEE", pageicon="🍌", layout="centered")

if "currentpage" not in st.session_state:
    st.session_state.currentpage = "main"
if "cart" not in st.session_state:
    st.session_state.cart = []

def set_page(page_name):
    st.session_state.currentpage = page_name

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
/* Zde ponechej své původní CSS styly */
.gastro-card {
    background-color: #1e1e1e;
    border-radius: 12px;
    padding: 16px;
    margin-bottom: 12px;
    border: 1px solid #333;
}
.gastro-title { font-weight: bold; font-size: 1.2rem; color: #FFE135; }
.gastro-price { font-weight: bold; color: #2ecc71; float: right; }
.gastro-desc { color: #cccccc; font-size: 0.95rem; margin-top: 6px; }
</style>
"""
st.markdown(css_styles, unsafe_allow_html=True)

# 1. HORIZONTÁLNÍ ČÁRA PŘED HLAVNÍM NADPISEM
st.markdown('<hr>', unsafe_allow_html=True)

# ANIMOVANÝ HLAVNÍ NADPIS A PODNADPIS
st.markdown('<h1 style="text-align: center;">BANANADOG</h1>', unsafe_allow_html=True)
st.markdown('<h3 style="text-align: center;">& COFFEE</h3>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; font-weight: bold;">⚡ ZAPOMEŇ NA PÁREK. SLADKÝ POP-UP Z ČB ⚡</p>', unsafe_allow_html=True)

# 2. HORIZONTÁLNÍ ČÁRA ZA PODNADPISU
st.markdown('<hr>', unsafe_allow_html=True)

# PANORAMATICKÝ BANNER
sketch_path = "bananadog.png"
sticker_path = "sticker.png"
sketch_base64 = get_base64_image(sketch_path)
sticker_base64 = get_base64_image(sticker_path)

if sketch_base64 and sticker_base64:
    banner_html = f'''
    <div style="position: relative; text-align: center;">
        <img src="data:image/png;base64,{sketch_base64}" style="width:100%; border-radius:12px;">
        <img src="data:image/png;base64,{sticker_base64}" style="position:absolute; top:10px; right:10px; width:80px;">
    </div>
    '''
    st.markdown(banner_html, unsafe_allow_html=True)
else:
    if os.path.exists(sketch_path):
        st.image(sketch_path, use_container_width=True)
    else:
        st.info("💡 Nahraj soubor 'bananadog.png' do GitHubu.")

# NAVIGAČNÍ PANEL (Rozšířen o tlačítko Šachy)
nav_col1, nav_col2, nav_col3, nav_col4, nav_col5 = st.columns(5)
with nav_col1:
    if st.button("🏠 MAIN"): set_page("main"); st.rerun()
with nav_col2:
    if st.button("📋 NABÍDKA"): set_page("nabidka"); st.rerun()
with nav_col3:
    if st.button("📸 GALLERY"): set_page("gallery"); st.rerun()
with nav_col4:
    if st.button("✨ ORIGIN"): set_page("origin"); st.rerun()
with nav_col5:
    if st.button("♟️ ŠACHY (20%)"): set_page("chess"); st.rerun()

# CELOŠÍŘKOVÝ KOŠÍK POD NAVIGACÍ
cart_count = len(st.session_state.cart)
cart_total = sum([item["price"] for item in st.session_state.cart])
cart_button_text = f"🛒 VIRTUÁLNÍ KOŠÍK ({cart_count} položek) — Celkem: {cart_total} Kč"
if st.button(cart_button_text):
    set_page("cart")
    st.rerun()

st.divider()

# ==========================================
# ROZCESTNÍK PODLE STAVU STRÁNKY
# ==========================================

if st.session_state.currentpage == "main":
    desc_main = "Máslová brioche bulka, grilovaný banán, brutal topingy a výběrové kafe v dravém streetwearovém podání. Přijď ochutnat do našeho budějovického pop-upu!"
    st.write(desc_main)
    st.divider()
    st.markdown("## 🔥 Our Bestsellers", unsafe_allow_html=True)
    st.write("Tohle lidi v ČB milují nejvíc:")

    st.markdown('<div class="gastro-card"><div class="gastro-title">🍫 The OG Classic</div><div class="gastro-desc">Máslová brioška, teplý banán, Nutella, brutal nálož drcených Oreo sušenek a špetka mořské soli. Svatá gastro trojice.</div><div class="gastro-price">115 Kč</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="gastro-card"><div class="gastro-title">🦩 Pink Special</div><div class="gastro-desc">Náš nový estetický drop. Malinový mousse toping, křupavé mini preclíky v domácím slaném karamelu. Totální chic závislost.</div><div class="gastro-price">140 Kč</div></div>', unsafe_allow_html=True)

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

elif st.session_state.currentpage == "nabidka":
    st.markdown("## 📋 Naše Kompletní Nabídka")
    st.write("Kliknutím na tlačítko u produktu si ho hned hodíš do virtuálního košíku.")
    st.markdown("### 🌭 Sladké Bananadogy")

    st.markdown('<div class="gastro-card"><div class="gastro-title">🍫 The OG Classic</div><div class="gastro-desc">Dozlatova opečená máslová brioche bulka, teplý zralý banán, poctivá vrstva husté tekuté Nutelly, bohatě zasypaná drcenými Oreo sušenkami a jemný dotek mořské soli.</div><div class="gastro-price">115 Kč</div></div>', unsafe_allow_html=True)
    if st.button("✨ Přidat The OG Classic do košíku", key="add_og"):
        add_to_cart("The OG Classic", 115); st.rerun()

    st.markdown('<div class="gastro-card"><div class="gastro-title">🦩 Pink Special</div><div class="gastro-desc">Teplý banán v nadýchaném brioche obalu, přelitý nadýchaným malinovým mousse topingem, dozdobený křupavými mini preclíky v domácím slaném karamelu.</div><div class="gastro-price">140 Kč</div></div>', unsafe_allow_html=True)
    if st.button("✨ Přidat Pink Special do košíku", key="add_pink"):
        add_to_cart("Pink Special", 140); st.rerun()

    st.markdown('<div class="gastro-card"><div class="gastro-title">🥜 Lotus & Peanut</div><div class="gastro-desc">Tekuté arašídové máslo, jemný karamelový přeliv, položený na banánu a drcené sušenky Lotus Biscoff.</div><div class="gastro-price">125 Kč</div></div>', unsafe_allow_html=True)
    if st.button("✨ Přidat Lotus & Peanut do košíku", key="add_lotus"):
        add_to_cart("Lotus & Peanut", 125); st.rerun()

elif st.session_state.currentpage == "chess":
    st.markdown("## ♟️ Poraz Stockfish 1200 a získej 20% slevu")
    st.write("Máš neomezeně pokusů! Pokud porazíš náš šachový engine na obtížnosti 1200 ELO, automaticky se ti vygeneruje unikátní slevový kód pro tvou objednávku.")

    # Embed šachové hry přes HTML/JS v rozhraní Streamlit
    chess_game_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/chessboard-js/1.0.0/chessboard-1.0.0.min.css">
        <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/chess.js/0.10.3/chess.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/chessboard-js/1.0.0/chessboard-1.0.0.min.js"></script>
        <style>
            body { font-family: sans-serif; background: #0e1117; color: white; text-align: center; margin: 0; padding: 10px; }
            #board { width: 340px; margin: 15px auto;
