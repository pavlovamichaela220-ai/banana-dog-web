import streamlit as st
import time
import os
import base64
import streamlit.components.v1 as components

st.set_page_config(
    page_title="BANANADOG & COFFEE", 
    pageicon="🍌", 
    layout="centered"
)

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

# --- 1. HORIZONTÁLNÍ ČÁRA PŘED HLAVNÍM NADPISEM ---
st.markdown('<hr>', unsafe_allow_html=True)

# --- ANIMOVANÝ HLAVNÍ NADPIS A PODNADPIS ---
st.markdown('<h1 style="text-align: center;">BANANADOG</h1>', unsafe_allow_html=True) 
st.markdown('<h3 style="text-align: center;">& COFFEE</h3>', unsafe_allow_html=True) 
st.markdown('<p style="text-align: center; font-weight: bold;">⚡ ZAPOMEŇ NA PÁREK. SLADKÝ POP-UP Z ČB ⚡</p>', unsafe_allow_html=True)

# --- 2. HORIZONTÁLNÍ ČÁRA ZA PODNADISEM (PŘED BANNEREM) ---
st.markdown('<hr>', unsafe_allow_html=True)

# --- PANORAMATICKÝ BANNER ---
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

# --- NAVIGAČNÍ PANEL (Rozšířen o záložku Šachy) ---
navcol1, navcol2, navcol3, navcol4, navcol5 = st.columns(5)
with navcol1: 
    if st.button("🏠 MAIN PAGE"): set_page("main"); st.rerun() 
with navcol2: 
    if st.button("📋 NABÍDKA"): set_page("nabidka"); st.rerun() 
with navcol3: 
    if st.button("📸 GALLERY"): set_page("gallery"); st.rerun() 
with navcol4: 
    if st.button("✨ ORIGIN STORY"): set_page("origin"); st.rerun()
with navcol5: 
    if st.button("♟️ ŠACHY (20%)"): set_page("chess"); st.rerun()

# --- CELOŠÍŘKOVÝ KOŠÍK POD NAVIGACÍ ---
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

elif st.session_state.currentpage == "nabidka": 
    st.markdown("## 📋 Naše Kompletní Nabídka") 
    st.write("Kliknutím na tlačítko u produktu si ho hned hodíš do virtuálního košíku.")
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

elif st.session_state.currentpage == "chess":
    st.markdown("## ♟️ Stockfish 1200 Chess Challenge")
    st.write("Poraz bota na obtížnosti 1200 ELO a získej **20% slevový kód** na své objednávky. Zkoušet to můžeš neomezeně, ale každý vygenerovaný kód platí pouze jednou!")

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
            #board { width: 340px; margin: 15px auto; }
            .status { font-weight: bold; margin: 10px; font-size: 1.1rem; color: #FFE135; }
            .voucher-box { background: #1e293b; border: 2px dashed #10b981; padding: 15px; border-radius: 8px; margin-top: 15px; display: none; }
            .voucher-code { font-size: 1.5rem; font-weight: bold; color: #10b981; letter-spacing: 2px; margin: 10px 0; }
            button { background: #FFE135; color: #000; border: none; padding: 10px 20px; font-weight: bold; border-radius: 6px; cursor: pointer; }
            button:hover { background: #ffd700; }
        </style>
    </head>
    <body>
        <div class="status" id="status">Jsi na tahu (Bílý)</div>
        <div id="board"></div>
        <button id="restartBtn">🔄 Nová Hra</button>
        
        <div class="voucher-box" id="voucherBox">
            <h3>🎉 GRATULUJEME! PORAZIL JSI STOCKFISH!</h3>
            <p>Zde je tvůj unikátní 20% slevový kód (použitelný 1x):</p>
            <div class="voucher-code" id="voucherCode">BANANA20-XXXX</div>
            <p><small>*Zkopíruj si ho a vlož v košíku v aplikaci.</small></p>
        </div>

        <script>
            var board = null;
            var game = new Chess();
            var $status =$('#status');
            var $voucherBox =$('#voucherBox');
            var $voucherCode =$('#voucherCode');

            var pieceValues = { p: 10, n: 30, b: 32, r: 50, q: 90, k: 900 };

            function evaluateBoard(boardState) {
                var totalEvaluation = 0;
                for (var i = 0; i < 8; i++) {
                    for (var j = 0; j < 8; j++) {
                        var piece = boardState[i][j];
                        if (piece) {
                            var val = pieceValues[piece.type] + (Math.random() * 0.3);
                            totalEvaluation += (piece.color === 'b' ? val : -val);
                        }
                    }
                }
                return totalEvaluation;
            }

            function makeStockfishMove() {
                var moves = game.moves({ verbose: true });
                if (moves.length === 0) return;

                moves.sort(function(a, b) {
                    game.move(a);
                    var scoreA = evaluateBoard(game.board());
                    game.undo();
                    game.move(b);
                    var scoreB = evaluateBoard(game.board());
                    game.undo();
                    return scoreB - scoreA;
                });

                var chosenIndex = (moves.length > 1 && Math.random() < 0.25) ? 1 : 0;
                game.move(moves[chosenIndex]);
                board.position(game.fen());
                updateStatus();
            }

            function onDragStart (source, piece) {
                if (game.game_over()) return false;
                if (piece.search(/^b/) !== -1) return false;
            }

            function onDrop (source, target) {
                var move = game.move({
                    from: source,
                    to: target,
                    promotion: 'q'
                });

                if (move === null) return 'snapback';
                updateStatus();

                if (!game.game_over()) {
                    window.setTimeout(makeStockfishMove, 300);
                }
            }

            function onSnapEnd () {
                board.position(game.fen());
            }

            function generateVoucher() {
                var chars = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789';
                var res = '';
                for (var i = 0; i < 6; i++) {
                    res += chars.charAt(Math.floor(Math.random() * chars.length));
                }
                return 'BANANA20-' + res;
            }

            function updateStatus () {
                var status = '';
                var moveColor = game.turn() === 'b' ? 'Stockfish (Černý)' : 'Ty (Bílý)';

                if (game.in_checkmate()) {
                    if (game.turn() === 'b') {
                        status = '🏆 VÍTĚZSTVÍ! Porazil jsi Stockfish!';
                        var code = generateVoucher();
                        $voucherCode.text(code);$voucherBox.show();
                    } else {
                        status = '❌ Mat! Stockfish vyhrál. Zkus to znovu!';
                    }
                } else if (game.in_draw()) {
                    status = '🤝 Remíza! Zkus to znovu pro získání voucheru.';
                } else {
                    status = moveColor + ' je na tahu';
                    if (game.in_check()) status += ', ŠACH!';
                }
                $status.html(status);
            }

            var config = {
                draggable: true,
                position: 'start',
                onDragStart: onDragStart,
                onDrop: onDrop,
                onSnapEnd: onSnapEnd
            };
            board = Chessboard('board', config);
            updateStatus();

            $('#restartBtn').on('click', function() {
                game.reset();
                board.position('start');
                $voucherBox.hide();
                updateStatus();
            });
        </script>
    </body>
    </html>
    """
    components.html(chess_game_html, height=650, scrolling=False)

elif st.session_state.currentpage == "cart": 
    st.markdown("## 🛒 Tvůj Virtuální Košík")
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
        st.markdown("### 🎁 Slevový kód")
        voucher_input = st.text_input("Vlož svůj slevový kód z šachů:")
        if voucher_input:
            if voucher_input.startswith("BANANA20-"):
                total_price = int(total_price * 0.8)
                st.success(f"🎉 Slevový kód úspěšně uplatněn! Nová cena: **{total_price} Kč**")
            else:
                st.error("Tento slevový kód neexistuje nebo je neplatný.")

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

elif st.session_state.currentpage == "gallery": 
    st.markdown("## 📸 Bananadog Gallery") 
    st.write("Atmosféra z našeho budějovického pop-upu a detaily našich produktů.")
    grid_path = "gallery_grid.png"
    if os.path.exists(grid_path):
        gallery_caption = "⚡ Bananadogs Vibe Grid: Street food atmosféra, detailní topingy a Happy Hour (299 Kč)"
        st.image(grid_path, use_container_width=True, caption=gallery_caption)
    else:
        st.warning("💡 Nahraj soubor s touto fotkou a pojmenuj ho 'gallery_grid.png' do GitHubu, aby se zobrazil.")

elif st.session_state.currentpage == "origin": 
    st.markdown("## ✨ Naše Origin Story") 
    p1 = "Všechno to začalo jedním bláznivým nápadem v Českých Budějovicích: Proč by měl být hotdog vždycky jenom slaný s párkem?" 
    st.write(p1)
    p2 = "Rozhodli jsme se to otočit vzhůru nohama. Vzali jsme nadýchanou máslovou briošku, přidali grilovaný banán a spojili to s těmi nejlepšími surovinami, které máme sami rádi."
    st.write(p2)
    p3 = "Výsledkem je dravý streetwearový pop-up concept BANANADOG & COFFEE, který boří mýty o klasickém fastfoodu. Přijď za námi ochutnat kus téhle sladké revoluce! 🔥"
    st.write(p3)
    
