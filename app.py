<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BANANADOG & COFFEE | Sladký Pop-Up ČB</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@800;900&family=Space+Grotesk:wght@400;600;700&display=swap" rel="stylesheet">
    <!-- FontAwesome for Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <style>
        /* Base typography & colors */
        body {
            font-family: 'Space Grotesk', sans-serif;
            background-color: #1a1412;
            color: #f4ece8;
            min-height: 100vh;
            overflow-x: hidden;
        }

        h1, h2, h3, .montserrat-font {
            font-family: 'Montserrat', sans-serif;
        }

        /* Slide animations for Title */
        @keyframes slideFromLeft {
            0% {
                opacity: 0;
                transform: translateX(-350px);
            }
            100% {
                opacity: 1;
                transform: translateX(0);
            }
        }

        @keyframes slideFromRight {
            0% {
                opacity: 0;
                transform: translateX(350px);
            }
            100% {
                opacity: 1;
                transform: translateX(0);
            }
        }

        .title-left {
            font-family: 'Montserrat', sans-serif;
            font-weight: 900;
            font-size: clamp(2.8rem, 8vw, 5.5rem);
            line-height: 0.9;
            letter-spacing: -3px;
            color: #F3E5AB;
            text-shadow: 0 10px 30px rgba(0,0,0,0.6);
            animation: slideFromLeft 1.4s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        }

        .title-right {
            font-family: 'Montserrat', sans-serif;
            font-weight: 900;
            font-size: clamp(2.8rem, 8vw, 5.5rem);
            line-height: 0.9;
            letter-spacing: -3px;
            color: #F3E5AB;
            text-shadow: 0 10px 30px rgba(0,0,0,0.6);
            animation: slideFromRight 1.4s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        }

        /* Gastro Card Real-time Smoke Animation */
        @keyframes borderGlowPulse {
            0% {
                box-shadow: 0 0 12px rgba(243, 229, 171, 0.3), inset 0 0 10px rgba(243, 229, 171, 0.15);
            }
            50% {
                box-shadow: 0 -10px 25px rgba(255, 255, 255, 0.3), 0 0 30px rgba(243, 229, 171, 0.6), inset 0 0 20px rgba(243, 229, 171, 0.3);
            }
            100% {
                box-shadow: 0 -16px 35px rgba(255, 255, 255, 0.2), 0 0 22px rgba(243, 229, 171, 0.4), inset 0 0 12px rgba(243, 229, 171, 0.2);
            }
        }

        @keyframes smokeUp {
            0% {
                opacity: 0;
                transform: translateY(0) scale(0.8) rotate(0deg);
            }
            30% {
                opacity: 0.7;
            }
            100% {
                opacity: 0;
                transform: translateY(-45px) scale(2.2) rotate(15deg);
            }
        }

        .gastro-card {
            position: relative;
            background: #261d1a;
            border: 1px solid #332723;
            border-radius: 16px;
            padding: 22px;
            transition: all 0.4s ease-in-out;
            overflow: visible;
        }

        .gastro-card:hover {
            border-color: #F3E5AB !important;
            transform: translateY(-4px);
            animation: borderGlowPulse 1.6s infinite alternate ease-in-out;
        }

        /* Dynamic Smoke Particles on Hover */
        .gastro-card::before,
        .gastro-card::after {
            content: '';
            position: absolute;
            top: -5px;
            width: 30px;
            height: 30px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(255,255,255,0.35) 0%, rgba(243,229,171,0.15) 40%, rgba(0,0,0,0) 80%);
            filter: blur(8px);
            opacity: 0;
            pointer-events: none;
        }

        .gastro-card:hover::before {
            left: 20%;
            animation: smokeUp 1.8s infinite ease-out 0.1s;
        }

        .gastro-card:hover::after {
            right: 25%;
            animation: smokeUp 2.1s infinite ease-out 0.6s;
        }

        /* Buttons styling */
        .btn-yellow {
            background-color: #F3E5AB !important;
            color: #1a1412 !important;
            font-weight: 700 !important;
            text-transform: uppercase !important;
            letter-spacing: 1px !important;
            border-radius: 12px !important;
            transition: all 0.3s ease-in-out !important;
        }

        .btn-yellow:hover {
            background-color: #ffffff !important;
            color: #1a1412 !important;
            transform: translateY(-3px) scale(1.02) !important;
            box-shadow: 0px 10px 25px rgba(243, 229, 171, 0.4) !important;
        }

        .tab-btn {
            background: rgba(38, 29, 26, 0.8);
            border: 1px solid #332723;
            color: #d1c7bd;
            font-weight: 700;
            transition: all 0.2s ease-in-out;
        }

        .tab-btn.active, .tab-btn:hover {
            background: #F3E5AB;
            color: #1a1412;
            border-color: #F3E5AB;
        }

        /* Custom Toast notification */
        #toast {
            visibility: hidden;
            min-width: 280px;
            background-color: #F3E5AB;
            color: #1a1412;
            text-align: center;
            border-radius: 12px;
            padding: 14px 20px;
            position: fixed;
            z-index: 100;
            right: 24px;
            bottom: 30px;
            font-weight: 700;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            opacity: 0;
            transition: opacity 0.3s, bottom 0.3s, visibility 0.3s;
        }

        #toast.show {
            visibility: visible;
            opacity: 1;
            bottom: 40px;
        }
    </style>
</head>
<body class="py-6 px-3 sm:px-6">

    <!-- Toast Notification -->
    <div id="toast"><i class="fa-solid fa-cart-shopping mr-2"></i> <span id="toast-msg">Přihozeno do košíku!</span></div>

    <!-- MAIN APP CONTAINER -->
    <div class="max-w-4xl mx-auto bg-[rgba(30,23,20,0.95)] p-3 sm:p-8 rounded-3xl shadow-2xl border-2 border-[#F3E5AB] my-2">

        <!-- HEADER TOP BAR WITH CART BUTTON -->
        <div class="flex justify-between items-center mb-6 border-b border-[#332723] pb-4">
            <div class="text-xs uppercase tracking-widest text-[#E6D592] font-semibold flex items-center gap-2">
                <span class="inline-block w-2.5 h-2.5 rounded-full bg-emerald-500 animate-ping"></span>
                POP-UP ČESKÉ BUDĚJOVICE OPEN
            </div>
            <!-- Floating Cart Trigger -->
            <button onclick="switchTab('cart')" class="btn-yellow px-4 py-2 text-sm flex items-center gap-2 relative shadow-lg">
                <i class="fa-solid fa-basket-shopping text-base"></i>
                <span class="hidden sm:inline">Košík</span>
                <span id="cart-badge" class="bg-[#1a1412] color-[#F3E5AB] text-[#F3E5AB] text-xs px-2 py-0.5 rounded-full font-bold">0</span>
                <span id="cart-total-header" class="text-xs border-l border-[#1a1412]/30 pl-2 font-bold">0 Kč</span>
            </button>
        </div>

        <!-- ANIMATED HEADER -->
        <div class="text-center my-4 overflow-hidden py-2">
            <h1 class="title-left">BANANADOG</h1>
            <h1 class="title-right">& COFFEE</h1>
            <p class="text-center font-bold uppercase tracking-[4px] sm:tracking-[6px] text-[#E6D592] text-xs sm:text-base mt-4 mb-6">
                ⚡ ZAPOMEŇ NA PÁREK. SLADKÝ POP-UP Z ČB ⚡
            </p>
        </div>

        <!-- PANORAMIC BANNER -->
        <div class="relative w-full h-48 sm:h-60 overflow-hidden rounded-2xl mb-8 shadow-2xl border-2 border-[#332723]">
            <img src="https://images.unsplash.com/photo-1551024709-8f23befc6f87?auto=format&fit=crop&w=1200&q=80" alt="Bananadog Banner" class="w-full h-full object-cover">
            <div class="absolute inset-0 bg-gradient-to-t from-[#1a1412] via-transparent to-transparent opacity-80"></div>
            <!-- Sticker Overlay -->
            <div class="absolute bottom-3 right-4 bg-[#F3E5AB] text-[#1a1412] px-4 py-2 rounded-xl font-extrabold text-xs sm:text-sm transform -rotate-6 shadow-2xl border-2 border-[#1a1412] uppercase tracking-wider flex items-center gap-2">
                <i class="fa-solid fa-fire text-amber-600"></i> FRESH & HOT DAILY
            </div>
        </div>

        <!-- TAB NAVIGATION -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 mb-8">
            <button onclick="switchTab('main')" id="tab-main" class="tab-btn py-3 px-2 rounded-xl text-center text-xs sm:text-sm uppercase tracking-wider">
                🏠 MAIN PAGE
            </button>
            <button onclick="switchTab('menu')" id="tab-menu" class="tab-btn py-3 px-2 rounded-xl text-center text-xs sm:text-sm uppercase tracking-wider">
                📋 NABÍDKA
            </button>
            <button onclick="switchTab('gallery')" id="tab-gallery" class="tab-btn py-3 px-2 rounded-xl text-center text-xs sm:text-sm uppercase tracking-wider">
                📸 GALLERY
            </button>
            <button onclick="switchTab('origin')" id="tab-origin" class="tab-btn py-3 px-2 rounded-xl text-center text-xs sm:text-sm uppercase tracking-wider">
                ✨ ORIGIN STORY
            </button>
        </div>

        <hr class="border-[#332723] mb-8">

        <!-- ==================== TAB 1: MAIN PAGE ==================== -->
        <div id="page-main" class="tab-content space-y-8">
            <div class="text-base sm:text-lg text-[#d1c7bd] leading-relaxed bg-[#261d1a]/50 p-4 sm:p-6 rounded-2xl border border-[#332723]">
                Máslová brioche bulka, grilovaný banán, brutal topingy a výběrové kafe v dravém streetwearovém podání. Přijď ochutnat do našeho budějovického pop-upu!
            </div>

            <div>
                <h2 class="text-2xl font-extrabold text-[#F3E5AB] mb-4 flex items-center gap-2">
                    🔥 Our Bestsellers
                </h2>
                <p class="text-sm text-[#d1c7bd] mb-6">Tohle lidi v ČB milují nejvíc:</p>

                <!-- Bestseller Card 1 -->
                <div class="gastro-card mb-4">
                    <div class="flex justify-between items-start">
                        <div class="text-xl font-bold text-[#F3E5AB]">🍫 The OG Classic</div>
                        <div class="text-[#E6D592] font-bold text-lg">115 Kč</div>
                    </div>
                    <p class="text-[#d1c7bd] text-sm mt-2 leading-relaxed">
                        Máslová brioška, teplý banán, Nutella, brutal nálož drcených Oreo sušenek a špetka mořské soli. Svatá gastro trojice.
                    </p>
                    <button onclick="addToCart('The OG Classic', 115)" class="btn-yellow w-full py-2 mt-4 text-xs">
                        ✨ Přidat Bestseller do košíku
                    </button>
                </div>

                <!-- Bestseller Card 2 -->
                <div class="gastro-card">
                    <div class="flex justify-between items-start">
                        <div class="text-xl font-bold text-[#F3E5AB]">🦩 Pink Special</div>
                        <div class="text-[#E6D592] font-bold text-lg">140 Kč</div>
                    </div>
                    <p class="text-[#d1c7bd] text-sm mt-2 leading-relaxed">
                        Náš nový estetický drop. Malinový mousse toping, křupavé mini preclíky v domácím slaném karamelu. Totální chic závislost.
                    </p>
                    <button onclick="addToCart('Pink Special', 140)" class="btn-yellow w-full py-2 mt-4 text-xs">
                        ✨ Přidat Bestseller do košíku
                    </button>
                </div>
            </div>

            <!-- Fast Quick Order -->
            <div class="bg-[#261d1a] p-6 rounded-2xl border border-[#332723] space-y-4">
                <h2 class="text-xl font-extrabold text-[#F3E5AB] flex items-center gap-2">
                    🚀 Rychlá Objednávka Na Bar (Click & Collect)
                </h2>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div>
                        <label class="block text-xs font-bold text-[#E6D592] mb-1">Jméno:</label>
                        <input type="text" id="quick-name" placeholder="Tvoje jméno" class="w-full bg-[#1a1412] border border-[#332723] rounded-xl p-3 text-sm text-white focus:outline-none focus:border-[#F3E5AB]">
                    </div>
                    <div>
                        <label class="block text-xs font-bold text-[#E6D592] mb-1">Telefon:</label>
                        <input type="tel" id="quick-phone" placeholder="+420 777 000 111" class="w-full bg-[#1a1412] border border-[#332723] rounded-xl p-3 text-sm text-white focus:outline-none focus:border-[#F3E5AB]">
                    </div>
                </div>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div>
                        <label class="block text-xs font-bold text-[#E6D592] mb-1">Vyber Bananadog:</label>
                        <select id="quick-dog" class="w-full bg-[#1a1412] border border-[#332723] rounded-xl p-3 text-sm text-white focus:outline-none focus:border-[#F3E5AB]">
                            <option value="none">Žádný</option>
                            <option value="The OG Classic" data-price="115">The OG Classic (115 Kč)</option>
                            <option value="Pink Special" data-price="140">Pink Special (140 Kč)</option>
                            <option value="Lotus & Peanut" data-price="125">Lotus & Peanut (125 Kč)</option>
                            <option value="White Berry" data-price="120">White Berry (120 Kč)</option>
                            <option value="Maple & Bacon" data-price="135">Maple & Bacon (135 Kč)</option>
                        </select>
                    </div>
                    <div>
                        <label class="block text-xs font-bold text-[#E6D592] mb-1">Vyber Kafe:</label>
                        <select id="quick-coffee" class="w-full bg-[#1a1412] border border-[#332723] rounded-xl p-3 text-sm text-white focus:outline-none focus:border-[#F3E5AB]">
                            <option value="none">Žádné</option>
                            <option value="Flat White" data-price="85">Flat White (85 Kč)</option>
                            <option value="Ice Banana Latte" data-price="95">Ice Banana Latte (95 Kč)</option>
                            <option value="Batch Brew" data-price="65">Batch Brew (65 Kč)</option>
                        </select>
                    </div>
                </div>
                <button onclick="submitQuickOrder()" class="btn-yellow w-full py-4 font-bold mt-2">
                    🔥 ODESLAT RYCHLOU OBJEDNÁVKU DO KUCHYNĚ 🔥
                </button>
            </div>
        </div>

        <!-- ==================== TAB 2: MENU ==================== -->
        <div id="page-menu" class="tab-content hidden space-y-6">
            <div>
                <h2 class="text-2xl font-extrabold text-[#F3E5AB] mb-1">📋 Naše Kompletní Nabídka</h2>
                <p class="text-sm text-[#d1c7bd]">Kliknutím na tlačítko si položku hodíš do virtuálního košíku.</p>
            </div>

            <h3 class="text-lg font-bold text-[#E6D592] uppercase tracking-wider pt-2">🌭 Sladké Bananadogy</h3>

            <!-- Item 1 -->
            <div class="gastro-card">
                <div class="flex justify-between items-start">
                    <div class="text-xl font-bold text-[#F3E5AB]">🍫 The OG Classic</div>
                    <div class="text-[#E6D592] font-bold text-lg">115 Kč</div>
                </div>
                <p class="text-[#d1c7bd] text-sm mt-2 leading-relaxed">
                    Dozlatova opečená máslová brioche bulka, teplý zralý banán, poctivá vrstva husté tekuté Nutelly, bohatě zasypaná drcenými Oreo sušenkami a jemný dotek mořské soli.
                </p>
                <button onclick="addToCart('The OG Classic', 115)" class="btn-yellow w-full py-2.5 mt-4 text-xs">
                    ✨ Přidat The OG Classic do košíku
                </button>
            </div>

            <!-- Item 2 -->
            <div class="gastro-card">
                <div class="flex justify-between items-start">
                    <div class="text-xl font-bold text-[#F3E5AB]">🦩 Pink Special</div>
                    <div class="text-[#E6D592] font-bold text-lg">140 Kč</div>
                </div>
                <p class="text-[#d1c7bd] text-sm mt-2 leading-relaxed">
                    Teplý banán v nadýchaném brioche obalu, přelitý nadýchaným, lehce kyselkavým malinovým mousse topingem, dozdobený křupavými mini preclíky v domácím slaném karamelu.
                </p>
                <button onclick="addToCart('Pink Special', 140)" class="btn-yellow w-full py-2.5 mt-4 text-xs">
                    ✨ Přidat Pink Special do košíku
                </button>
            </div>

            <!-- Item 3 -->
            <div class="gastro-card">
                <div class="flex justify-between items-start">
                    <div class="text-xl font-bold text-[#F3E5AB]">🥜 Lotus & Peanut</div>
                    <div class="text-[#E6D592] font-bold text-lg">125 Kč</div>
                </div>
                <p class="text-[#d1c7bd] text-sm mt-2 leading-relaxed">
                    Tekuté arašídové máslo, jemný karamelový přeliv, položený na banánu a drcené sušenky Lotus Biscoff.
                </p>
                <button onclick="addToCart('Lotus & Peanut', 125)" class="btn-yellow w-full py-2.5 mt-4 text-xs">
                    ✨ Přidat Lotus & Peanut do košíku
                </button>
            </div>

            <!-- Item 4 -->
            <div class="gastro-card">
                <div class="flex justify-between items-start">
                    <div class="text-xl font-bold text-[#F3E5AB]">🍓 White Berry</div>
                    <div class="text-[#E6D592] font-bold text-lg">120 Kč</div>
                </div>
                <p class="text-[#d1c7bd] text-sm mt-2 leading-relaxed">
                    Poleva z bílé belgické čokolády, mrazem sušené jahody a drcené máslové sušenky.
                </p>
                <button onclick="addToCart('White Berry', 120)" class="btn-yellow w-full py-2.5 mt-4 text-xs">
                    ✨ Přidat White Berry do košíku
                </button>
            </div>

            <!-- Item 5 -->
            <div class="gastro-card">
                <div class="flex justify-between items-start">
                    <div class="text-xl font-bold text-[#F3E5AB]">🥓 Maple & Bacon</div>
                    <div class="text-[#E6D592] font-bold text-lg">135 Kč</div>
                </div>
                <p class="text-[#d1c7bd] text-sm mt-2 leading-relaxed">
                    Javorový sirup, drcené vlašské ořechy a navrch dokřupava vypečená, sekaná slanina. Sladko-slaná bomba.
                </p>
                <button onclick="addToCart('Maple & Bacon', 135)" class="btn-yellow w-full py-2.5 mt-4 text-xs">
                    ✨ Přidat Maple & Bacon do košíku
                </button>
            </div>

            <h3 class="text-lg font-bold text-[#E6D592] uppercase tracking-wider pt-6">☕ Výběrové Kafe</h3>

            <!-- Coffee 1 -->
            <div class="gastro-card">
                <div class="flex justify-between items-start">
                    <div class="text-xl font-bold text-[#F3E5AB]">☕ Flat White</div>
                    <div class="text-[#E6D592] font-bold text-lg">85 Kč</div>
                </div>
                <p class="text-[#d1c7bd] text-sm mt-2">Dvojité espresso, sametová mikropěna.</p>
                <button onclick="addToCart('Flat White', 85)" class="btn-yellow w-full py-2.5 mt-4 text-xs">
                    ✨ Přidat Flat White do košíku
                </button>
            </div>

            <!-- Coffee 2 -->
            <div class="gastro-card">
                <div class="flex justify-between items-start">
                    <div class="text-xl font-bold text-[#F3E5AB]">🧊 Ice Banana Latte</div>
                    <div class="text-[#E6D592] font-bold text-lg">95 Kč</div>
                </div>
                <p class="text-[#d1c7bd] text-sm mt-2">Ledové espresso s naším banánovým sirupem.</p>
                <button onclick="addToCart('Ice Banana Latte', 95)" class="btn-yellow w-full py-2.5 mt-4 text-xs">
                    ✨ Přidat Ice Banana Latte do košíku
                </button>
            </div>

            <!-- Coffee 3 -->
            <div class="gastro-card">
                <div class="flex justify-between items-start">
                    <div class="text-xl font-bold text-[#F3E5AB]">☕ Batch Brew</div>
                    <div class="text-[#E6D592] font-bold text-lg">65 Kč</div>
                </div>
                <p class="text-[#d1c7bd] text-sm mt-2">Filtrovaná káva dne, fresh profil.</p>
                <button onclick="addToCart('Batch Brew', 65)" class="btn-yellow w-full py-2.5 mt-4 text-xs">
                    ✨ Přidat Batch Brew do košíku
                </button>
            </div>
        </div>

        <!-- ==================== TAB 3: GALLERY ==================== -->
        <div id="page-gallery" class="tab-content hidden space-y-6">
            <div>
                <h2 class="text-2xl font-extrabold text-[#F3E5AB] mb-1">📸 Bananadog Gallery</h2>
                <p class="text-sm text-[#d1c7bd]">Atmosféra z našeho budějovického pop-upu a detaily našich produktů.</p>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div class="bg-[#261d1a] border border-[#332723] rounded-2xl overflow-hidden group">
                    <div class="h-56 overflow-hidden">
                        <img src="https://images.unsplash.com/photo-1551024709-8f23befc6f87?auto=format&fit=crop&w=600&q=80" alt="Street Food Vibe" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                    </div>
                    <div class="p-4">
                        <p class="text-xs text-[#E6D592] font-bold uppercase tracking-wider">Street Food Pop-Up</p>
                        <p class="text-sm text-[#d1c7bd] mt-1">České Budějovice center energy.</p>
                    </div>
                </div>

                <div class="bg-[#261d1a] border border-[#332723] rounded-2xl overflow-hidden group">
                    <div class="h-56 overflow-hidden">
                        <img src="https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?auto=format&fit=crop&w=600&q=80" alt="Specialty Coffee" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                    </div>
                    <div class="p-4">
                        <p class="text-xs text-[#E6D592] font-bold uppercase tracking-wider">Výběrová Káva</p>
                        <p class="text-sm text-[#d1c7bd] mt-1">Čerstvě pražená zrna & sametová mikropěna.</p>
                    </div>
                </div>

                <div class="bg-[#261d1a] border border-[#332723] rounded-2xl overflow-hidden group sm:col-span-2">
                    <div class="h-64 overflow-hidden">
                        <img src="https://images.unsplash.com/photo-1587314168485-3236d6710814?auto=format&fit=crop&w=1000&q=80" alt="Sweet Dog Preparation" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
                    </div>
                    <div class="p-4">
                        <p class="text-xs text-[#E6D592] font-bold uppercase tracking-wider">Fresh Toppings Drop</p>
                        <p class="text-sm text-[#d1c7bd] mt-1">Nutella, Oreo & mořská sůl v plné parádě.</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- ==================== TAB 4: ORIGIN STORY ==================== -->
        <div id="page-origin" class="tab-content hidden space-y-6">
            <div>
                <h2 class="text-2xl font-extrabold text-[#F3E5AB] mb-1">✨ Naše Origin Story</h2>
            </div>

            <div class="bg-[#261d1a] p-6 sm:p-8 rounded-2xl border border-[#332723] space-y-4 text-[#d1c7bd] leading-relaxed">
                <p>
                    Všechno to začalo jedním bláznivým nápadem v Českých Budějovicích: <strong class="text-[#F3E5AB]">Proč by měl být hotdog vždycky jenom slaný s párkem?</strong>
                </p>
                <p>
                    Rozhodli jsme se to otočit vzhůru nohama. Vzali jsme nadýchanou máslovou briošku, přidali grilovaný banán a spojili to s těmi nejlepšími surovinami, které máme sami rádi.
                </p>
                <p>
                    Výsledkem je dravý streetwearový pop-up concept <strong class="text-[#F3E5AB]">BANANADOG & COFFEE</strong>, který boří mýty o klasickém fastfoodu. Přijď za námi ochutnat kus téhle sladké revoluce! 🔥
                </p>
            </div>
        </div>

        <!-- ==================== TAB 5: CART VIEW ==================== -->
        <div id="page-cart" class="tab-content hidden space-y-6">
            <div>
                <h2 class="text-2xl font-extrabold text-[#F3E5AB] mb-1">🛒 Tvůj Virtuální Košík</h2>
                <p class="text-sm text-[#d1c7bd]">Zkontrolovat a odeslat objednávku do kuchyně.</p>
            </div>

            <div id="cart-empty-msg" class="bg-[#261d1a] p-8 rounded-2xl border border-[#332723] text-center space-y-4">
                <i class="fa-solid fa-basket-shopping text-4xl text-[#E6D592]/40"></i>
                <p class="text-[#d1c7bd]">Tvůj košík je zatím prázdný. Mrkni do sekce **Nabídka** a něco si vyber! 🍌</p>
                <button onclick="switchTab('menu')" class="btn-yellow px-6 py-3 text-xs">
                    ← Zpět do nabídky
                </button>
            </div>

            <div id="cart-content-wrapper" class="hidden space-y-6">
                <!-- Cart Items List -->
                <div id="cart-items-list" class="space-y-3">
                    <!-- Populated by JS -->
                </div>

                <div class="bg-[#261d1a] p-4 rounded-xl border border-[#332723] flex justify-between items-center text-lg font-bold">
                    <span class="text-[#d1c7bd]">Celkem k úhradě:</span>
                    <span id="cart-total-sum" class="text-[#F3E5AB] text-xl">0 Kč</span>
                </div>

                <!-- Order Form -->
                <div class="bg-[#261d1a] p-6 rounded-2xl border border-[#332723] space-y-4">
                    <h3 class="text-lg font-extrabold text-[#F3E5AB] flex items-center gap-2">
                        🚀 Dokončení Objednávky
                    </h3>
                    
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                        <div>
                            <label class="block text-xs font-bold text-[#E6D592] mb-1">Jméno a příjmení:</label>
                            <input type="text" id="cart-name" placeholder="Jan Novák" class="w-full bg-[#1a1412] border border-[#332723] rounded-xl p-3 text-sm text-white focus:outline-none focus:border-[#F3E5AB]">
                        </div>
                        <div>
                            <label class="block text-xs font-bold text-[#E6D592] mb-1">Telefonní číslo:</label>
                            <input type="tel" id="cart-phone" placeholder="+420 777 123 456" class="w-full bg-[#1a1412] border border-[#332723] rounded-xl p-3 text-sm text-white focus:outline-none focus:border-[#F3E5AB]">
                        </div>
                    </div>

                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                        <div>
                            <label class="block text-xs font-bold text-[#E6D592] mb-1">Čas vyzvednutí na baru:</label>
                            <input type="time" id="cart-time" value="15:30" class="w-full bg-[#1a1412] border border-[#332723] rounded-xl p-3 text-sm text-white focus:outline-none focus:border-[#F3E5AB]">
                        </div>
                        <div>
                            <label class="block text-xs font-bold text-[#E6D592] mb-1">Způsob platby:</label>
                            <select id="cart-payment" class="w-full bg-[#1a1412] border border-[#332723] rounded-xl p-3 text-sm text-white focus:outline-none focus:border-[#F3E5AB]">
                                <option value="Karta na baru">💳 Platba kartou u výdeje</option>
                                <option value="Hotově">💵 Hotově u výdeje</option>
                            </select>
                        </div>
                    </div>

                    <!-- Order Progress Bar Indicator -->
                    <div id="order-progress-container" class="hidden space-y-2 pt-2">
                        <div class="flex justify-between text-xs text-[#E6D592] font-bold">
                            <span>Odesílám do kuchyně...</span>
                            <span id="progress-percent">0%</span>
                        </div>
                        <div class="w-full bg-[#1a1412] h-3 rounded-full overflow-hidden border border-[#332723]">
                            <div id="progress-bar-fill" class="bg-[#F3E5AB] h-full w-0 transition-all duration-100"></div>
                        </div>
                    </div>

                    <button onclick="submitCartOrder()" id="cart-submit-btn" class="btn-yellow w-full py-4 font-bold text-sm">
                        🔥 ODESLAT KOŠÍK DO KUCHYNĚ 🔥
                    </button>
                </div>
            </div>
        </div>

    </div>

    <!-- JAVASCRIPT LOGIC -->
    <script>
        // Shopping Cart State
        let cart = [];

        // Tab Switching
        function switchTab(tabName) {
            document.querySelectorAll('.tab-content').forEach(el => el.classList.add('hidden'));
            document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));

            const targetPage = document.getElementById(`page-${tabName}`);
            if (targetPage) {
                targetPage.classList.remove('hidden');
            }

            const targetBtn = document.getElementById(`tab-${tabName}`);
            if (targetBtn) {
                targetBtn.classList.add('active');
            }

            // Render Cart if opened
            if (tabName === 'cart') {
                renderCart();
            }

            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        // Add item to cart
        function addToCart(itemName, price) {
            cart.push({ id: Date.now(), name: itemName, price: price });
            updateCartHeader();
            showToast(`Přihozeno do košíku: ${itemName}! 🍌`);
        }

        // Remove item from cart
        function removeFromCart(itemId) {
            cart = cart.filter(item => item.id !== itemId);
            updateCartHeader();
            renderCart();
        }

        // Update Header Badge and Total
        function updateCartHeader() {
            const count = cart.length;
            const total = cart.reduce((sum, item) => sum + item.price, 0);

            document.getElementById('cart-badge').innerText = count;
            document.getElementById('cart-total-header').innerText = `${total} Kč`;
        }

        // Render Cart UI
        function renderCart() {
            const emptyMsg = document.getElementById('cart-empty-msg');
            const wrapper = document.getElementById('cart-content-wrapper');
            const itemsList = document.getElementById('cart-items-list');
            const totalSum = document.getElementById('cart-total-sum');

            if (cart.length === 0) {
                emptyMsg.classList.remove('hidden');
                wrapper.classList.add('hidden');
                return;
            }

            emptyMsg.classList.add('hidden');
            wrapper.classList.remove('hidden');

            itemsList.innerHTML = '';
            let total = 0;

            cart.forEach(item => {
                total += item.price;
                const itemEl = document.createElement('div');
                itemEl.className = 'bg-[#261d1a] border border-[#332723] p-4 rounded-xl flex justify-between items-center';
                itemEl.innerHTML = `
                    <div>
                        <div class="font-bold text-[#F3E5AB] text-base">• ${item.name}</div>
                        <div class="text-xs text-[#d1c7bd]">${item.price} Kč</div>
                    </div>
                    <button onclick="removeFromCart(${item.id})" class="text-rose-400 hover:text-rose-300 text-xs uppercase font-bold tracking-wider px-3 py-1.5 rounded-lg border border-rose-900/50 hover:border-rose-500/50 bg-rose-950/30">
                        <i class="fa-solid fa-trash mr-1"></i> Smazat
                    </button>
                `;
                itemsList.appendChild(itemEl);
            });

            totalSum.innerText = `${total} Kč`;
        }

        // Toast Notification
        function showToast(message) {
            const toast = document.getElementById('toast');
            document.getElementById('toast-msg').innerText = message;
            toast.classList.add('show');
            setTimeout(() => {
                toast.classList.remove('show');
            }, 2500);
        }

        // Submit Quick Order Form from Main Tab
        function submitQuickOrder() {
            const name = document.getElementById('quick-name').value.trim();
            const phone = document.getElementById('quick-phone').value.trim();
            const dogSelect = document.getElementById('quick-dog');
            const coffeeSelect = document.getElementById('quick-coffee');

            if (!name || !phone) {
                alert('⚠️ Vyplň prosím jméno a telefon!');
                return;
            }

            if (dogSelect.value === 'none' && coffeeSelect.value === 'none') {
                alert('⚠️ Vyber prosím alespoň jeden Bananadog nebo kafe!');
                return;
            }

            if (dogSelect.value !== 'none') {
                const dogOption = dogSelect.options[dogSelect.selectedIndex];
                addToCart(dogSelect.value, parseInt(dogOption.getAttribute('data-price') || 0));
            }

            if (coffeeSelect.value !== 'none') {
                const coffeeOption = coffeeSelect.options[coffeeSelect.selectedIndex];
                addToCart(coffeeSelect.value, parseInt(coffeeOption.getAttribute('data-price') || 0));
            }

            switchTab('cart');
        }

        // Submit Full Cart Order with Progress Bar
        function submitCartOrder() {
            const name = document.getElementById('cart-name').value.trim();
            const phone = document.getElementById('cart-phone').value.trim();
            const timeVal = document.getElementById('cart-time').value;

            if (!name || !phone) {
                alert('⚠️ Vyplň prosím jméno a telefonní číslo!');
                return;
            }

            const progressContainer = document.getElementById('order-progress-container');
            const progressBarFill = document.getElementById('progress-bar-fill');
            const progressPercent = document.getElementById('progress-percent');
            const submitBtn = document.getElementById('cart-submit-btn');

            progressContainer.classList.remove('hidden');
            submitBtn.disabled = true;
            submitBtn.classList.add('opacity-50');

            let progress = 0;
            const interval = setInterval(() => {
                progress += 5;
                progressBarFill.style.width = `${progress}%`;
                progressPercent.innerText = `${progress}%`;

                if (progress >= 100) {
                    clearInterval(interval);
                    setTimeout(() => {
                        alert(`🎉 Objednávka proklouzla na bar, ${name}!\nChystáme pro tebe ${cart.length} položek na ${timeVal} do Kavárenské 42, ČB.`);
                        cart = [];
                        updateCartHeader();
                        renderCart();
                        progressContainer.classList.add('hidden');
                        submitBtn.disabled = false;
                        submitBtn.classList.remove('opacity-50');
                        switchTab('main');
                    }, 300);
                }
            }, 30);
        }

        // Set Main Tab default
        window.addEventListener('DOMContentLoaded', () => {
            switchTab('main');
        });
    </script>
</body>
</html>
