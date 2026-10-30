import streamlit as st import time import os import base64
st.setpageconfig( pagetitle="BANANADOG & COFFEE", pageicon="🍌", layout="centered" )
if "currentpage" not in st.sessionstate: st.sessionstate.currentpage = "main"
if "cart" not in st.sessionstate: st.sessionstate.cart = []
def setpage(pagename): st.sessionstate.currentpage = page_name
def addtocart(itemname, price): st.sessionstate.cart.append({"name": itemname, "price": price}) st.toast(f"Přihozeno do košíku: {itemname}! 🍌", icon="🛒")
def getbase64image(imagepath): if os.path.exists(imagepath): with open(imagepath, "rb") as imgfile: return base64.b64encode(img_file.read()).decode("utf-8") return ""
css_styles = """
""" st.markdown(cssstyles, unsafeallow_html=True)
--- 1. HORIZONTÁLNÍ ČÁRA PŘED HLAVNÍM NADPISEM ---
st.markdown('
', unsafeallowhtml=True)--- ANIMOVANÝ HLAVNÍ NADPIS A PODNADPIS ---
st.markdown('
BANANADOG
', unsafeallowhtml=True) st.markdown('
& COFFEE
', unsafeallowhtml=True) st.markdown('
⚡ ZAPOMEŇ NA PÁREK. SLADKÝ POP-UP Z ČB ⚡
', unsafeallowhtml=True)--- 2. HORIZONTÁLNÍ ČÁRA ZA PODNADISEM (PŘED BANNEREM) ---
st.markdown('
', unsafeallowhtml=True)--- PANORAMATICKÝ BANNER ---
sketchpath = "bananadog.png" stickerpath = "sticker.png"
sketchbase64 = getbase64image(sketchpath) stickerbase64 = getbase64image(stickerpath)
if sketchbase64 and stickerbase64: bannerhtml = f'''

''' st.markdown(bannerhtml, unsafeallowhtml=True) else: if os.path.exists(sketchpath): st.image(sketchpath, usecontainerwidth=True) else: st.info("💡 Nahraj soubor 'bananadog.png' do GitHubu.")--- NAVIGAČNÍ PANEL ---
navcol1, navcol2, navcol3, navcol4 = st.columns(4)
with navcol1: if st.button("🏠 MAIN PAGE"): setpage("main") st.rerun() with navcol2: if st.button("📋 NABÍDKA"): setpage("nabidka") st.rerun() with navcol3: if st.button("📸 GALLERY"): setpage("gallery") st.rerun() with navcol4: if st.button("✨ ORIGIN STORY"): setpage("origin") st.rerun()
--- CELOŠÍŘKOVÝ KOŠÍK POD NAVIGACÍ ---
cartcount = len(st.sessionstate.cart) carttotal = sum([item["price"] for item in st.sessionstate.cart])
cartbuttontext = f"🛒 VIRTUÁLNÍ KOŠÍK ({cartcount} položek) — Celkem: {carttotal} Kč" if st.button(cartbuttontext): set_page("cart") st.rerun()
st.divider()
==========================================
ROZCESTNÍK PODLE STAVU STRÁNKY
==========================================
if st.sessionstate.currentpage == "main": descmain = "Máslová brioche bulka, grilovaný banán, brutal topingy a výběrové kafe v dravém streetwearovém podání. Přijď ochutnat do našeho budějovického pop-upu!" st.write(descmain) st.divider()
bestsellers_title = "## 🔥 Our Bestsellers"
st.markdown(bestsellers_title, unsafe_allow_html=True)
st.write("Tohle lidi v ČB milují nejvíc:")

c_og = (
'<div class="gastro-card">'
'<div class="gastro-title">🍫 The OG Classic</div>'
'<div class="gastro-desc">Máslová brioška, teplý banán, Nutella, brutal nálož drcených Oreo sušenek a špetka mořské soli. Svatá gastro trojice.</div>'
'<div class="gastro-price">115 Kč</div>'
'</div>'
)
st.markdown(c_og, unsafe_allow_html=True)

c_pink = (
'<div class="gastro-card">'
'<div class="gastro-title">🦩 Pink Special</div>'
'<div class="gastro-desc">Náš nový estetický drop. Malinový mousse toping, křupavé mini preclíky v domácím slaném karamelu. Totální chic závislost.</div>'
'<div class="gastro-price">140 Kč</div>'
'</div>'
)
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
elif st.sessionstate.currentpage == "nabidka": st.markdown("## 📋 Naše Kompletní Nabídka") st.write("Kliknutím na tlačítko u produktu si ho hned hodíš do virtuálního košíku.")
st.markdown("### 🌭 Sladké Bananadogy")

card_og = (
'<div class="gastro-card">'
'<div class="gastro-title">🍫 The OG Classic</div>'
'<div class="gastro-desc">Dozlatova opečená máslová brioche bulka, teplý zralý banán, poctivá vrstva husté tekuté Nutelly, bohatě zasypaná drcenými Oreo sušenkami a jemný dotek mořské soli.</div>'
'<div class="gastro-price">115 Kč</div>'
'</div>'
)
st.markdown(card_og, unsafe_allow_html=True)
if st.button("✨ Přidat The OG Classic do košíku", key="add_og"):
add_to_cart("The OG Classic", 115)
st.rerun()

card_pink = (
'<div class="gastro-card">'
'<div class="gastro-title">🦩 Pink Special</div>'
'<div class="gastro-desc">Teplý banán v nadýchaném brioche obalu, přelitý nadýchaným, lehce kyselkavým malinovým mousse topingem, dozdobený křupavými mini preclíky v domácím slaném karamelu.</div>'
'<div class="gastro-price">140 Kč</div>'
'</div>'
)
st.markdown(card_pink, unsafe_allow_html=True)
if st.button("✨ Přidat Pink Special do košíku", key="add_pink"):
add_to_cart("Pink Special", 140)
st.rerun()

card_lotus = (
'<div class="gastro-card">'
'<div class="gastro-title">🥜 Lotus & Peanut</div>'
'<div class="gastro-desc">Tekuté arašídové máslo, jemný karamelový přeliv, položený na banánu a drcené sušenky Lotus Biscoff.</div>'
'<div class="gastro-price">125 Kč</div>'
'</div>'
)
st.markdown(card_lotus, unsafe_allow_html=True)
if st.button("✨ Přidat Lotus & Peanut do košíku", key="add_lotus"):
add_to_cart("Lotus & Peanut", 125)
st.rerun()

card_white = (
'<div class="gastro-card">'
'<div class="gastro-title">🍓 White Berry</div>'
'<div class="gastro-desc">Poleva z bílé belgické čokolády, mrazem sušené jahody a drcené máslové sušenky.</div>'
'<div class="gastro-price">120 Kč</div>'
'</div>'
)
st.markdown(card_white, unsafe_allow_html=True)
if st.button("✨ Přidat White Berry do košíku", key="add_white"):
add_to_cart("White Berry", 120)
st.rerun()

card_maple = (
'<div class="gastro-card">'
'<div class="gastro-title">🥓 Maple & Bacon</div>'
'<div class="gastro-desc">Javorový sirup, drcené vlašské ořechy a navrch dokřupava vypečená, sekaná slanina. Sladko-slaná bomba.</div>'
'<div class="gastro-price">135 Kč</div>'
'</div>'
)
st.markdown(card_maple, unsafe_allow_html=True)
if st.button("✨ Přidat Maple & Bacon do košíku", key="add_maple"):
add_to_cart("Maple & Bacon", 135)
st.rerun()

st.divider()
st.markdown("### ☕ Výběrové Kafe")

card_fw = (
'<div class="gastro-card">'
'<div class="gastro-title">☕ Flat White</div>'
'<div class="gastro-desc">Dvojité espresso, sametová mikropěna.</div>'
'<div class="gastro-price">85 Kč</div>'
'</div>'
)
st.markdown(card_fw, unsafe_allow_html=True)
if st.button("✨ Přidat Flat White do košíku", key="add_fw"):
add_to_cart("Flat White", 85)
st.rerun()

card_ibl = (
'<div class="gastro-card">'
'<div class="gastro-title">🧊 Ice Banana Latte</div>'
'<div class="gastro-desc">Ledové espresso s naším banánovým sirupem.</div>'
'<div class="gastro-price">95 Kč</div>'
'</div>'
)
st.markdown(card_ibl, unsafe_allow_html=True)
if st.button("✨ Přidat Ice Banana Latte do košíku", key="add_ibl"):
add_to_cart("Ice Banana Latte", 95)
st.rerun()

card_bb = (
'<div class="gastro-card">'
'<div class="gastro-title">☕ Batch Brew</div>'
'<div class="gastro-desc">Filtrovaná káva dne, fresh profil.</div>'
'<div class="gastro-price">65 Kč</div>'
'</div>'
)
st.markdown(card_bb, unsafe_allow_html=True)
if st.button("✨ Přidat Batch Brew do košíku", key="add_bb"):
add_to_cart("Batch Brew", 65)
st.rerun()
elif st.sessionstate.currentpage == "cart": st.markdown("## 🛒 Tvůj Virtuální Košík")
if len(st.session_state.cart) == 0:
st.info("Tvůj košík je zatím prázdný. Mrkni do sekce **Nabídka** a něco si vyber! 🍌")
if st.button("← Zpět do nabídky"):
set_page("nabidka")
st.rerun()
else:
st.write("Položky připravené k odeslání:")
for idx, item in enumerate(st.session_state.cart):
col_i1, col_i2, col_i3 = st.columns([3, 1, 1])
col_i1.write(f"• **{item['name']}**")
col_i2.write(f"{item['price']} Kč")
if col_i3.button("🗑️ Smazat", key=f"del_{idx}"):
st.session_state.cart.pop(idx)
st.rerun()

st.divider()
total_price = sum([item["price"] for item in st.session_state.cart])
st.markdown(f"### **Celkem k úhradě: {total_price} Kč**")

st.divider()
st.markdown("### 🚀 Dokončení objednávky")
c_name = st.text_input("Jméno a příjmení:")
c_phone = st.text_input("Telefonní číslo:")
c_time = st.time_input("Čas vyzvednutí:")

if st.button("🔥 ODESLAT KOŠÍK DO KUCHYNĚ 🔥"):
if c_name and c_phone:
progress_bar = st.progress(0)
for percent_complete in range(100):
time.sleep(0.005)
progress_bar.progress(percent_complete + 1)
progress_bar.empty()
st.success(f"🎉 **Hotovo, {c_name}! Objednávka z košíku letí na bar.**")
st.balloons()
st.session_state.cart = []
else:
st.error("Vyplň prosím jméno a telefon!")
elif st.sessionstate.currentpage == "gallery": st.markdown("## 📸 Bananadog Gallery") st.write("Atmosféra z našeho budějovického pop-upu a detaily našich produktů.")
grid_path = "gallery_grid.png"
if os.path.exists(grid_path):
gallery_caption = "⚡ Bananadogs Vibe Grid: Street food atmosféra, detailní topingy a Happy Hour (299 Kč)"
st.image(grid_path, use_container_width=True, caption=gallery_caption)
else:
st.warning("💡 Nahraj soubor s touto fotkou a pojmenuj ho 'gallery_grid.png' do GitHubu, aby se zobrazil.")
elif st.sessionstate.currentpage == "origin": st.markdown("## ✨ Naše Origin Story") p1 = "Všechno to začalo jedním bláznivým nápadem v Českých Budějovicích: Proč by měl být hotdog vždycky jenom slaný s párkem?" st.write(p1)
p2 = "Rozhodli jsme se to otočit vzhůru nohama. Vzali jsme nadýchanou máslovou briošku, přidali grilovaný banán a spojili to s těmi nejlepšími surovinami, které máme sami rádi."
st.write(p2)

p3 = "Výsledkem je dravý streetwearový pop-up concept BANANADOG & COFFEE, který boří mýty o klasickém fastfoodu. Přijď za námi ochutnat kus téhle sladké revoluce! 🔥"
st.write(p3) 
