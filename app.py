import streamlit as st
import requests

BASE_URL = "https://api.alquran.cloud/v1"

# Bookmark Storage
if "bookmarks" not in st.session_state:
    st.session_state.bookmarks = []

# Fetch Surah List
def fetch_surahs():
    response = requests.get(f"{BASE_URL}/surah")
    if response.status_code == 200:
        return response.json()["data"]
    return []

# Fetch Surah Verses
def fetch_surah_verses(surah_number):
    response = requests.get(f"{BASE_URL}/surah/{surah_number}/editions/quran-uthmani,en.asad")
    if response.status_code == 200:
        return response.json()["data"]
    return None

# --------------- Config & Assets ---------------
st.set_page_config(
    page_title="JannahWay - Islamic Growth",
    page_icon="🕌",
    layout="wide" 
)
# Sidebar Navigation
st.sidebar.title("🌟 JannahWay Portal")
dark_mode = st.sidebar.toggle("🌙 Dark Mode")

menu = st.sidebar.radio(
    "📜 Select a Section",
    ["🏠 Home", "📖 Quran", "📿 Tasbeeh", "🤲 Duas & Wazaif", "🕌 Ramadan"]
)
# --------------- Dark Mode Styling ---------------
if dark_mode:
    st.markdown("""
        <style>
        body {background-color: #1E1E1E; color: #E5E5E5;}
        .stApp {background-color: #1E1E1E !important;}
        .stSidebar {background: #252525 !important; color: white !important;}
        h1, h2, h3, h4, h5, h6 { color: #FFD700 !important; }
        p, label { color: #E5E5E5 !important; }
  
        /* Force Button Background & Text Color */
        div.stButton > button {
            color: black !important;  /* Ensure text is black */
            background-color: #1E1E1E !important;
            border-radius: 10px !important;
            border: 2px solid #FFD700 !important;
            padding: 8px 16px !important;
            font-weight: bold !important;
            transition: 0.3s ease-in-out !important;
        }

    /* Arabic Text Styling */
    div.arabic-text {
        color: white !important;  /* Arabic text in white */
        font-size: 22px;
        text-align: right;
        margin: 10px 0;
    }

        /* Button Hover Effect */
        div.stButton > button:hover {
            background-color:rgb(97, 72, 7) !important;
            color: black !important;
            border-color: #FFC700 !important;
        }

        </style>
    """, unsafe_allow_html=True)

def home_section():
    # Custom CSS styling
    st.markdown("""
    <style>
        # h3 { color: #FFD700 !important; }
        h6 { color: #E5E5E5 !important; }
        .stButton>button {
            margin-top: 10px;
            background-color: #000000;
            color: white;
            border-radius: 15px;
            border: 2px solid #FFD700;
            padding: 8px 20px;
            width: 100%;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {            
            background-color: #000000;
            transform: scale(1.05);
        }
        .asma-card {
            background: #1a1a1a;
            padding: 20px;
            border-radius: 15px;
            margin-top: 20px;
            text-align: center;
            min-height: 300px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .arabic-text {
            font-size: 32px;
            min-height: 60px;
            color: #E5E5E5;
        }   
        .english-text {
            font-size: 18px;
            margin: 15px 0;
            color: #E5E5E5;
        }
        .qibla-card {
            background: #1a1a1a;
            padding: 20px;
            border-radius: 15px;
            margin-top: 20px;
            text-align: center;
            min-height: 300px;
        }
    </style>
    """, unsafe_allow_html=True)

    # Header Section
    st.markdown("""
    <div style="background:#000000;color:white;padding:30px;border-radius:20px;text-align:center">
        <h1>🌙 Welcome to JannahWay</h1>
        <p>Your Smart Companion for Islamic Growth & Spirituality</p>
    </div>
    """, unsafe_allow_html=True)

    # Initialize session state for Asma ul Husna
    if 'next_asma_nabi_index' not in st.session_state:
        st.session_state.next_asma_nabi_index = 0

    if 'asma_index' not in st.session_state:
        st.session_state.asma_index = 0

    prophet_names_list = [
    ("مُحَمَّدٌ", "The Praised One"),
    ("أَحْمَدُ", "The Most Praiseworthy"),
    ("طَهَ", "Pure, Clean"),
    ("يٰسٓ", "O Human Being"),
    ("الْمُصْطَفَى", "The Chosen One"),
    ("الْمُرْتَضَى", "The One Pleasing to Allah"),
    ("الْحَبِيبُ", "The Beloved"),
    ("السَّاجِدُ", "The One Who Prostrates"),
    ("الرَّاكِعُ", "The One Who Bows"),
    ("النَّبِيُّ", "The Prophet"),
    ("الرَّسُولُ", "The Messenger"),
    ("الصِّدِّيقُ", "The Truthful"),
    ("الأَمِينُ", "The Trustworthy"),
    ("الشَّافِعُ", "The Intercessor"),
    ("المُبَشِّرُ", "The Bringer of Good News"),
    ("النَّذِيرُ", "The Warner"),
    ("السِّرَاجُ الْمُنِيرُ", "The Illuminating Lamp"),
    ("الرَّحْمَةُ", "The Mercy"),
    ("الخَاتَمُ", "The Seal (of Prophets)"),
    ("المُزَمِّلُ", "The Enshrouded One"),
    ("المُدَّثِّرُ", "The Cloaked One"),
    ("الْمُؤَيَّدُ", "The Supported One"),
    ("الْمَاحِي", "The Eraser (of disbelief)"),
    ("الْحَاشِرُ", "The Gatherer"),
    ("الْعَاقِبُ", "The Successor"),
    ("الفَاتِحُ", "The Conqueror"),
    ("النَّاصِرُ", "The Helper"),
    ("الرَّحِيمُ", "The Compassionate"),
    ("التَّوَّابُ", "The Most Repentant"),
    ("الشَّهِيدُ", "The Witness"),
    ("الصَّادِقُ", "The Honest"),
    ("المَشْفُوعُ", "The One with Intercession"),
    ("الْمُقْتَدِي", "The Role Model"),
    ("الْمُجْتَبَى", "The Selected One"),
    ("الْمُحْسِنُ", "The Benevolent"),
    ("الْمُعَلِّمُ", "The Teacher"),
    ("السَّيِّدُ", "The Master"),
    ("الْمُبَارَكُ", "The Blessed One"),
    ("الْأُمِّيُّ", "The Unlettered Prophet"),
    ("الْمُنْجِي", "The Rescuer"),
    ("الرَّئُوفُ", "The Kind"),
    ("الْمُجَاهِدُ", "The Struggler (in Allah’s cause)"),
    ("الْمُتَوَاضِعُ", "The Humble One"),
    ("الْمُتَوَكِّلُ", "The One Who Relies on Allah"),
    ("الْكَافِي", "The Sufficient One"),
    ("النَّبِيُّ الأَكْرَمُ", "The Most Honored Prophet"),
    ("الصَّفِيُّ", "The Pure One"),
    ("الشَّاكِرُ", "The Grateful One"),
    ("الْحَلِيمُ", "The Forbearing One"),
    ("الْمُحْتَسِبُ", "The One Who Seeks Reward from Allah"),
    ("الْمُطْمَئِنُّ", "The Tranquil One"),
    ("الْمُنِيرُ", "The Radiant One"),
    ("الْمُبِينُ", "The Clear Expositor"),
    ("الْمُعْجِزُ", "The Miraculous"),
    ("الْمَأْمُونُ", "The Secured One"),
    ("الْمُجْزِي", "The One Who Recompenses"),
    ("الْمُتَضَرِّعُ", "The Supplicating One"),
    ("الْمُحْتَرَمُ", "The Honored One"),
    ("الْمَكْرُمُ", "The Noble One"),
    ("الصَّبُورُ", "The Patient One"),
    ("الْوَفِيُّ", "The Faithful One"),
    ("الْمُوَقَّرُ", "The Revered One"),
    ("المُحِبُّ", "The Loving One"),
    ("الْمُبَارَكُ", "The Blessed One"),
    ("السَّابِقُ", "The Forerunner"),
    ("الْخَيِّرُ", "The Good One"),
    ("الْهَادِي", "The Guide"),
    ("الْمُبِينُ", "The Manifest One"),
    ("الْمُخْتَارُ", "The Chosen One"),
    ("الْمُتَفَكِّرُ", "The Thoughtful One"),
    ("الْمُقَدَّمُ", "The One Who is Given Precedence"),
    ("الْمُؤْمِنُ", "The Faithful One"),
    ("الْمُعَظَّمُ", "The Highly Honored One"),
    ("الْمُهْتَدِي", "The Rightly Guided One"),
    ("السَّامِعُ", "The Listener"),
    ("الْمُرَبِّي", "The One Who Nurtures"),
    ("الْمُنِيبُ", "The One Who Turns to Allah"),
    ("الْمُشَفَّعُ", "The One Whose Intercession is Accepted"),
    ("المُجْتَهِدُ", "The Hardworking One"),
    ("الْمُحِبُّ", "The Loving One"),
    ("السَّالِمُ", "The Peaceful One"),
    ("النُّورُ", "The Light"),
    ("الْمُؤَيَّدُ", "The Supported One"),
    ("الْمُسَدَّدُ", "The One Guided to Success"),
    ("الْمُسْتَقِيمُ", "The Upright One")
]

    # Complete list of Asma ul Husna (first 5 for demo)
    asma_list = [
    ("ٱلْرَّحْمَـٰنُ", "The Most Merciful"),
    ("ٱلْرَّحِيمُ", "The Especially Merciful"),
    ("ٱلْمَلِكُ", "The King and Owner of Dominion"),
    ("ٱلْقُدُّوسُ", "The Absolutely Pure"),
    ("ٱلْسَّلَامُ", "The Source of Peace and Safety"),
    ("ٱلْمُؤْمِنُ", "The Giver of Faith and Security"),
    ("ٱلْمُهَيْمِنُ", "The Guardian"),
    ("ٱلْعَزِيزُ", "The Almighty"),
    ("ٱلْجَبَّارُ", "The Compeller"),
    ("ٱلْمُتَكَبِّر", "The Supreme"),
    ("ٱلْخَالِقُ", "The Creator"),
    ("ٱلْبَارِئُ", "The Evolver"),
    ("ٱلْمُصَوِّرُ", "The Fashioner"),
    ("ٱلْغَفَّارُ", "The Constant Forgiver"),
    ("ٱلْقَهَّارُ", "The All-Prevailing One"),
    ("ٱلْوَهَّابُ", "The Supreme Bestower"),
    ("ٱلْرَّزَّاقُ", "The Provider"),
    ("ٱلْفَتَّاحُ", "The Supreme Solver"),
    ("ٱلْعَلِيمُ", "The All-Knowing"),
    ("ٱلْقَابِضُ", "The Withholder"),
    ("ٱلْبَاسِطُ", "The Extender"),
    ("ٱلْخَافِضُ", "The Reducer"),
    ("ٱلْرَّافِعُ", "The Exalter"),
    ("ٱلْمُعِزُّ", "The Honourer-Bestower"),
    ("ٱلْمُذِلُّ", "The Dishonourer"),
    ("ٱلْسَّمِيعُ", "The All-Hearing"),
    ("ٱلْبَصِيرُ", "The All-Seeing"),
    ("ٱلْحَكَمُ", "The Impartial Judge"),
    ("ٱلْعَدْلُ", "The Just One"),
    ("ٱلْلَّطِيفُ", "The Subtle One"),
    ("ٱلْخَبِيرُ", "The All-Aware"),
    ("ٱلْحَلِيمُ", "The Most Forbearing"),
    ("ٱلْعَظِيمُ", "The Magnificent One"),
    ("ٱلْغَفُورُ", "The Great Forgiver"),
    ("ٱلْشَّكُورُ", "The Most Appreciative"),
    ("ٱلْعَلِيُّ", "The Most High, The Exalted"),
    ("ٱلْكَبِيرُ", "The Most Great"),
    ("ٱلْحَفِيظُ", "The Preserver"),
    ("ٱلْمُقِيتُ", "The Sustainer"),
    ("ٱلْحسِيبُ", "The Reckoner"),
    ("ٱلْجَلِيلُ", "The Majestic"),
    ("ٱلْكَرِيمُ", "The Most Generous, the Most Esteemed"),
    ("ٱلْرَّقِيبُ", "The Watchful"),
    ("ٱلْمُجِيبُ", "The Responsive One"),
    ("ٱلْوَاسِعُ", "The All-Encompassing, the Boundless"),
    ("ٱلْحَكِيمُ", "The All-Wise"),
    ("ٱلْوَدُودُ", "The Most Loving"),
    ("ٱلْمَجِيدُ", "The Glorious, Most Honorable"),
    ("ٱلْبَاعِثُ", "The Infuser of New Life"),
    ("ٱلْشَّهِيدُ", "The All-and-Ever Witnessing"),
    ("ٱلْحَقُ", "The Absolute Truth"),
    ("ٱلْوَكِيلُ", "The Trustee"),
    ("ٱلْقَوِيُ", "The All-Strong"),
    ("ٱلْمَتِينُ", "The Firm One"),
    ("ٱلْوَلِيُ", "The Solely Loyal"),
    ("ٱلْحَمِيدُ", "The Most Praiseworthy"),
    ("ٱلْمُحْصِيُ", "The All-Enumerating, the Counter"),
    ("ٱلْمُبْدِئُ", "The Originator, the Initiator"),
    ("ٱلْمُعِيدُ", "The Restorer, the Reinstater"),
    ("ٱلْمُحْيِى", "The Giver of Life"),
    ("ٱلْمُمِيتُ", "The Creator of Death"),
    ("ٱلْحَيُ", "The Ever-Living"),
    ("ٱلْقَيُّومُ", "The Sustainer, The Self-Subsisting"),
    ("ٱلْوَاجِدُ", "The Perceiver"),
    ("ٱلْمَاجِدُ", "The Glorious, Most Honorable"),
    ("ٱلْوَاحِدُ", "The Only One"),
    ("ٱلْأَحَدُ", "The Indivisible, The One"),
    ("ٱلْصَّمَدُ", "The Self-Sufficient, The Impregnable"),
    ("ٱلْقَادِرُ", "The Omnipotent"),
    ("ٱلْمُقْتَدِرُ", "The Creator of All Power"),
    ("ٱلْمُقَدِّمُ", "The Expediter"),
    ("ٱلْمُؤَخِّرُ", "The Delayer"),
    ("ٱلأوَّلُ", "The First"),
    ("ٱلْآخِرُ", "The Last"),
    ("ٱلْظَّاهِرُ", "The Manifest"),
    ("ٱلْبَاطِنُ", "The Hidden One, Knower of the Hidden"),
    ("ٱلْوَالِي", "The Sole Governor"),
    ("ٱلْمُتَعَالِي", "The Self Exalted"),
    ("ٱلْبَرُ", "The Source of All Goodness"),
    ("ٱلْتَّوَابُ", "The Ever-Pardoning"),
    ("ٱلْمُنْتَقِمُ", "The Just Requitor"),
    ("ٱلْعَفُوُ", "The Supreme Pardoner"),
    ("ٱلْرَّؤُفُ", "The Most Kind"),
    ("مَالِكُ ٱلْمُلْكِ", "Master of the Kingdom, Owner of the Dominion"),
    ("ذُوالْجَلَالِ وَالإكْرَامِ", "Possessor of Glory and Honor"),
    ("ٱلْمُقْسِطُ", "The Just One"),
    ("ٱلْجَامِعُ", "The Gatherer, the Uniter"),
    ("ٱلْغَنيُ", "The Self-Sufficient, the Wealthy"),
    ("ٱلْمُغْنِيُ", "The Enricher"),
    ("ٱلْمَانِعُ", "The Withholder"),
    ("ٱلْضَّارَ", "The Distresser"),
    ("ٱلْنَّافِعُ", "The Propitious, the Benefactor"),
    ("ٱلْنُّورُ", "The Light"),
    ("ٱلْهَادِي", "The Guide"),
    ("ٱلْبَدِيعُ", "Incomparable Originator"),
    ("ٱلْبَاقِي", "The Ever-Surviving"),
    ("ٱلْوَارِثُ", "The Inheritor"),
    ("ٱلْرَّشِيدُ", "The Guide, Infallible Teacher, and Knower"),
    ("ٱلْصَّبُورُ", "The Forbearing")
]

    # Navigation functions
    def next_asma():
        st.session_state.asma_index = (st.session_state.asma_index + 1) % len(asma_list)
    
    def prev_asma():
        st.session_state.asma_index = (st.session_state.asma_index - 1) % len(asma_list)

    def next_asma_nabi():
        st.session_state.next_asma_nabi_index = (st.session_state.next_asma_nabi_index + 1) % len(prophet_names_list)
    
    def prev_asma_nabi():
        st.session_state.next_asma_nabi_index = (st.session_state.next_asma_nabi_index - 1) % len(prophet_names_list)

    # Main columns layout
    col1, col2 = st.columns([1, 1], gap="medium")

 
    with col1:
        # Asma ul Husna Card
        st.markdown(f"""
        <div class="asma-card">
            <h3 style="color: #E5E5E5;">🕋 Asma ul Husna جَلَّ جَلَالُهُ</h3>
            <div style="margin:20px 0">
                <div class="arabic-text" style="font-size:32px; min-height: 60px; text-align: center;">
                    <p>
                    {asma_list[st.session_state.asma_index][0]}
                    </p>
                </div>
                <p class="english-text" style="margin:15px 0; font-size:18px">
                    {asma_list[st.session_state.asma_index][1]}
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Button controls
        btn_col1, btn_col2 = st.columns(2)
        with btn_col1:
            if st.button("← Previous", key="prev_btn"):
                prev_asma()
        with btn_col2:
            if st.button("Next →", key="next_btn"):
                next_asma()
 
    with col2:
        # Asma ul Husna Card
        st.markdown(f"""
        <div class="asma-card">
            <h3 style="color: #E5E5E5;">🕌 Asma un Nabi ﷺ</h3>
            <div style="margin:20px 0">
                <div class="arabic-text" style="font-size:32px; min-height: 60px; text-align: center;">
                    <p>
                    {prophet_names_list[st.session_state.next_asma_nabi_index][0]}
                    </p>
                </div>
                <p class="english-text" style="margin:15px 0; font-size:18px">
                    {prophet_names_list[st.session_state.next_asma_nabi_index][1]}
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Button controls
        btn_col1, btn_col2 = st.columns(2)
 
        with btn_col1:
            if st.button("← Previous", key="prev_button"):
                prev_asma_nabi()
        with btn_col2:
            if st.button("Next →", key="next_button"):
                next_asma_nabi()
                
                
                
# --------------- Quran Section 📖 ---------------
def quran_section():
    st.markdown("<h1>📖 Quran Section</h1>", unsafe_allow_html=True)
    
    if 'current_view' not in st.session_state:
        st.session_state.current_view = "surah"

    # Navigation Buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📜 Surah"):
            st.session_state.current_view = "surah"
    with col2:
        if st.button("📑 Bookmark"):
            st.session_state.current_view = "bookmark"

    # Handle Surah View
    if st.session_state.current_view == "surah":
        surahs = fetch_surahs()
        if surahs:
            surah_names = [f"{s['number']}. {s['englishName']} ({s['name']})" for s in surahs]
            selected_surah = st.selectbox("Choose Surah:", surah_names)
            surah_number = int(selected_surah.split(".")[0])
            
            with st.spinner("Loading surah..."):
                surah_data = fetch_surah_verses(surah_number)
            
            if surah_data:
                st.markdown(f"### 📖 {surah_data[0]['englishName']} ({surah_data[0]['name']})")
                st.markdown(f"**Number of Verses:** {len(surah_data[0]['ayahs'])}")
                st.markdown(f"**Revelation Type:** {surah_data[0]['revelationType'].capitalize()}")
                
                if surah_number != 9 and surah_number != 1:
                    st.markdown("<div dir='rtl' style='font-size:28px; text-align:center; margin:20px 0;'>بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ</div>", unsafe_allow_html=True)
                
                for i, verse in enumerate(surah_data[0]["ayahs"]):
                    eng_verse = surah_data[1]["ayahs"][i]
                    
                    st.markdown(f"""
                    <div style='background-color: {"#333" if dark_mode else "#f8f9fa"}; 
                               padding: 15px; 
                               border-radius: 10px; 
                               margin-bottom: 15px;'>
                        <p style='font-weight: bold; margin-bottom: 5px; color: {"#FFD700" if dark_mode else "#0066cc"};'>
                            Verse {verse['numberInSurah']}
                        </p>
                        <div dir='rtl' style='font-size: 24px; margin-bottom: 10px;'>
                            {verse['text']}
                        </div>
                        <div style='font-size: 16px; margin-top: 10px; color: {"#E5E5E5" if dark_mode else "#333"};'>
                            {eng_verse['text']}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button(f"🔊 Listen to {surah_data[0]['englishName']}"):
                        audio_url = f"https://server8.mp3quran.net/afs/{str(surah_number).zfill(3)}.mp3"
                        st.audio(audio_url)
                with col2:
                    bookmark_name = f"Surah {surah_data[0]['englishName']}"
                    if st.button(f"📑 Bookmark {bookmark_name}"):
                        if bookmark_name not in st.session_state.bookmarks:
                            st.session_state.bookmarks.append(bookmark_name)
                            st.success("Bookmarked!")
                        else:
                            st.warning("Already bookmarked!")

    # Handle Bookmarks View
    elif st.session_state.current_view == "bookmark":
        st.markdown("### 📑 Your Bookmarks")
        if st.session_state.bookmarks:
            for bm in st.session_state.bookmarks:
                col1, col2 = st.columns([4, 1])
                with col1:
                    st.write(f"✅ {bm}")
                with col2:
                    if st.button("🗑️ Remove", key=f"remove_{bm}"):
                        st.session_state.bookmarks.remove(bm)
                        st.experimental_rerun()
            
            if st.button("Clear All Bookmarks"):
                st.session_state.bookmarks = []
                st.success("Bookmarks cleared!")
        else:
            st.warning("No bookmarks yet. Start exploring to save some!")
# --------------- Tasbeeh Section 📿 ---------------
def tasbeeh_section():
    st.markdown("<h1>📿 Dhikr Counter</h1>", unsafe_allow_html=True)
    st.write("🔢 Click the buttons to count your dhikr.")

    # List of 50 Adhkar
    adhkar_list = [
        "SubhanAllah (سبحان الله)", "Alhamdulillah (الحمد لله)", "Allahu Akbar (الله أكبر)", "La ilaha illallah (لا إله إلا الله)",
        "Astaghfirullah (أستغفر الله)", "La hawla wa la quwwata illa billah (لا حول ولاقوة إلا بالله)", "Bismillah (بسم الله)",
        "Hasbunallahu wa ni'mal wakeel (حسبنا الله ونعم الوكيل)", "Rabbi zidni ilma (ربي زدني علما)", "Allahumma inni as'aluka al-jannah (اللهم إني أسألك الجنة)",
        "Allahumma ajirni min an-naar (اللهم أجرني من النار)", "Ya Hayyu Ya Qayyum (يا حي يا قيوم)", "Allahumma barik lana (اللهم بارك لنا)",
        "Rabbighfir li (رب اغفر لي)", "Allahumma laka alhamd (اللهم لك الحمد)", "Allahumma anta as-salam (اللهم أنت السلام)",
        "SubhanAllahi wa bihamdihi (سبحان الله وبحمده)", "SubhanAllahil azeem (سبحان الله العظيم)", "Ya Rahman, Ya Raheem (يا رحمن يا رحيم)",
        "Rabbi la tadharni fardan (ربي لا تذرني فردا)", "Rabbi habli minas-salihin (رب هب لي من الصالحين)", "Allahumma rahmataka arju (اللهم رحمتك أرجو)",
        "Rabbana atina fid-dunya hasanah (ربنا آتنا في الدنيا حسنة)", "Rabbi yassir wa la tu'assir (ربي يسر ولا تعسر)", "Allahumma inni dhalamtu nafsi (اللهم إني ظلمت نفسي)",
        "Rabbi innee lima anzalta ilayya min khayrin faqir (ربي إني لما أنزلت إلي من خير فقير)", "Allahumma inni a'udhu bika min fitnatil qabri (اللهم إني أعوذ بك من فتنة القبر)",
        "Allahumma ahdina siratal mustaqeem (اللهم اهدنا الصراط المستقيم)", "Rabbi jalni muqimas-salah (ربي اجعلني مقيم الصلاة)", "Rabbi inni maghloobun fantasir (ربي إني مغلوب فانتصر)",
        "Rabbi awzi'ni an ashkura (ربي أوزعني أن أشكر)", "Rabbi la taj'alni ma'al qawmi dhalimeen (ربي لا تجعلني مع القوم الظالمين)", "Rabbi faghfir wa irham wa anta khayrur rahimeen (ربي اغفر وارحم وأنت خير الراحمين)",
        "Ya Dhal-Jalali wal-Ikram (يا ذا الجلال والإكرام)", "Allahumma salli ala Muhammadin wa ala aali Muhammad (اللهم صل على محمد وعلى آل محمد)",
        "Rabbi inni zalamtu nafsi faghfir li (ربي إني ظلمت نفسي فاغفر لي)", "Rabbi inni massaniyadh-dhurru wa anta arhamur-rahimeen (ربي إني مسني الضر وأنت أرحم الراحمين)",
        "Rabbi adkhilni mudkhala sidqin wa akhrijni mukhraja sidqin (ربي أدخلني مدخل صدق وأخرجني مخرج صدق)", "Allahumma anta rabbi la ilaha illa anta (اللهم أنت ربي لا إله إلا أنت)",
        "Rabbi a'udhu bika min hamazatish-shayateen (ربي أعوذ بك من همزات الشياطين)", "Rabbi la tuhammilni ma la taqata li bihi (ربي لا تحملني ما لا طاقة لي به)",
        "Rabbi la tukhzini yawmal qiyamah (ربي لا تخزني يوم القيامة)", "Rabbi yassir lana umoorana (ربي يسر لنا أمورنا)", "Rabbi a'udhu bika min athabil qabr (ربي أعوذ بك من عذاب القبر)",
        "Rabbi habli hukman wa alhiqni bis-salihin (ربي هب لي حكما وألحقني بالصالحين)", "Rabbi la tu'akhidhni bima nasitu (ربي لا تؤاخذني بما نسيت)", "Rabbi waqini adhab an-naar (ربي وقني عذاب النار)"
    ]

    # Store tasbeeh counts in session state
    if "tasbeeh_counts" not in st.session_state:
        st.session_state.tasbeeh_counts = {dhikr: 0 for dhikr in adhkar_list}

    # Display Tasbeehs  
    for tasbeeh, count in st.session_state.tasbeeh_counts.items():
        st.write(f"📿 **{tasbeeh}**: {count}")
        col1, col2 = st.columns(2)
        with col1:
            if st.button(f"➕ {tasbeeh}", key=f"inc_{tasbeeh}"):
                st.session_state.tasbeeh_counts[tasbeeh] += 1
        with col2:
            if st.button(f"🔄 Reset {tasbeeh}", key=f"reset_{tasbeeh}"):
                st.session_state.tasbeeh_counts[tasbeeh] = 0

    # Custom Tasbeeh input
    new_tasbeeh = st.text_input("➕ Add Custom Tasbeeh:")
    if st.button("Add Tasbeeh"):
        if new_tasbeeh and new_tasbeeh not in st.session_state.tasbeeh_counts:
            st.session_state.tasbeeh_counts[new_tasbeeh] = 0

# --------------- Duas & Wazaif Section 🤲 ---------------
def duas_wazaif_section():
    st.markdown("<h1>🤲 Islamic Duas & Wazaif</h1>", unsafe_allow_html=True)

    # Dua Categories
    categories = [
        "🌅 Daily Life Duas",
        "🛡️ Protection Duas",
        "🕌 Ramadan Duas",
        "🤲 Forgiveness & Mercy Duas",
        "📖 Quranic & Special Duas"
    ]

    # Default: Show all duas
    selected_category = st.selectbox("📜 Select a Dua Category", ["📜 Show All"] + categories)

    # **DUAS COLLECTION**
    duas_collection = {
        "🌅 Daily Life Duas": [
            ("Morning Dua", "اللهم بك أصبحنا وبك أمسينا وبك نحيا وبك نموت وإليك المصير"),
            ("Evening Dua", "اللهم إني أمسيت أشهدك أنك أنت الله لا إله إلا أنت وحدك لا شريك لك"),
            ("Before Sleeping", "بِسْمِكَ اللَّهُمَّ أَمُوتُ وَأَحْيَا"),
            ("Waking Up", "الحمد لله الذي أحيانا بعد ما أماتنا وإليه النشور"),
            ("Before Eating", "بِسْمِ اللَّهِ"),
            ("After Eating", "الْحَمْدُ لِلَّهِ الَّذِي أَطْعَمَنَا وَسَقَانَا وَجَعَلَنَا مِنَ الْمُسْلِمِينَ"),
            ("Before Entering Toilet", "اللهم إني أعوذ بك من الخبث والخبائث"),
            ("After Leaving Toilet", "غفرانك"),
            ("Before Traveling", "سُبْحَانَ الَّذِي سَخَّرَ لَنَا هَذَا وَمَا كُنَّا لَهُ مُقْرِنِينَ"),
            ("Dua for Parents", "رَّبِّ ارْحَمْهُمَا كَمَا رَبَّيَانِي صَغِيرًا"),
            ("Dua Before Studying", "اللهم إني أسألك فهم النبيين وحفظ المرسلين"),
            ("Dua After Studying", "اللهم اجعلني من الفاهمين"),
            ("Dua for Entering Home", "اللهم إني أسألك خير المولج وخير المخرج"),
            ("Dua for Leaving Home", "بسم الله توكلت على الله ولا حول ولا قوة إلا بالله"),
            ("Dua for Entering the Mosque", "اللهم افتح لي أبواب رحمتك"),
            ("Dua for Leaving the Mosque", "اللهم إني أسألك من فضلك"),
            ("Dua Before Wearing Clothes", "الحمد لله الذي كساني هذا الثوب"),
            ("Dua for New Clothes", "اللهم لك الحمد كما كسوتنيه"),
            ("Dua Before Entering a Market", "لا إله إلا الله وحده لا شريك له"),
            ("Dua for Health", "اللهم اشفني شفاء لا يغادر سقما"),
            ("Dua for Strength", "حسبنا الله ونعم الوكيل"),
            ("Dua for Rizq", "اللهم ارزقني رزقا حلالا طيبا مباركا"),
            ("Dua for Success", "اللهم لا سهل إلا ما جعلته سهلا"),
            ("Dua for Marriage", "اللهم ارزقني الزوج الصالح"),
            ("Dua for Children", "رَبِّ هَبْ لِي مِنَ الصَّالِحِينَ"),
            ("Dua for Patience", "رَبِّ أَوْزِعْنِي أَنْ أَشْكُرَ نِعْمَتَكَ"),
            ("Dua for Contentment", "اللهم اجعلني قانعا بما رزقتني"),
            ("Dua for Protection from Arrogance", "اللهم إني أعوذ بك من الكبر والعجب"),
        ],
        "🛡️ Protection Duas": [
            ("Seeking Allah's Protection", "أعوذ بكلمات الله التامات من شر ما خلق"),
            ("Protection from Evil Eye", "اللهم بارك ولا تضر"),
            ("Protection from Enemies", "اللهم اكفنيهم بما شئت"),
            ("Protection from Anxiety & Depression", "اللهم إني أعوذ بك من الهم والحزن"),
            ("Dua Against Harm", "اللهم إني أعوذ بك من البرص والجنون والجذام وسيئ الأسقام"),
            ("Dua for Protection of Family", "اللهم احفظ لي أهلي وأحبتي من كل سوء"),
        ],
        "🕌 Ramadan Duas": [
            ("Suhoor Dua", "وَبِصَوْمِ غَدٍ نَّوَيْتُ مِنْ شَهْرِ رَمَضَانَ"),
            ("Iftar Dua", "اللهم إني لك صمت وبك آمنت وعليك توكلت وعلى رزقك أفطرت"),
            ("Dua for Laylatul Qadr", "اللهم إنك عفو كريم تحب العفو فاعف عني"),
            ("Dua for First Ashra (Mercy)", "اللهم ارحمنا برحمتك"),
            ("Dua for Second Ashra (Forgiveness)", "اللهم اغفر لي ذنوبي"),
            ("Dua for Third Ashra (Freedom from Hell)", "اللهم أجرني من النار"),
        ],
        "🤲 Forgiveness & Mercy Duas": [
            ("Dua for Forgiveness", "رب اغفر لي وتب علي إنك أنت التواب الرحيم"),
            ("Dua for Mercy", "اللهم ارحمني برحمتك الواسعة"),
            ("Dua for Repentance", "اللهم إني ظلمت نفسي فاغفر لي"),
            ("Dua for a Pure Heart", "اللهم طهر قلبي من النفاق"),
            ("Dua for the Day of Judgment", "اللهم اجعل قبري روضة من رياض الجنة"),
        ],
        "📖 Quranic & Special Duas": [
            ("Dua from Surah Al-Fatiha", "اهْدِنَا الصِّرَاطَ الْمُسْتَقِيمَ"),
            ("Dua from Surah Al-Baqarah", "رَبَّنَا آتِنَا فِي الدُّنْيَا حَسَنَةً وَفِي الْآخِرَةِ حَسَنَةً وَقِنَا عَذَابَ النَّارِ"),
            ("Dua from Surah Al-Kahf", "رَبِّ زِدْنِي عِلْمًا"),
            ("Dua for Rizq", "اللهم ارزقني رزقا حلالا طيبا مباركا"),
            ("Dua for the Hereafter", "اللهم اجعل قبري نورا"),
        ]
    }

    # Display Duas
    if selected_category == "📜 Show All":
        for category, duas in duas_collection.items():
            st.markdown(f"### {category}")
    
            for title, dua in duas:
                st.markdown(f"#### {title}")
                # st.write(f"<div dir='rtl' style='font-size:22px; margin:10px 0; '>{dua}</div>", unsafe_allow_html=True)
                st.markdown(f"<div dir='rtl' style='font-size:22px; margin:10px 0; '> <p> {dua} <p/></div>", unsafe_allow_html=True)
                st.markdown("---")
    else:
        st.markdown(f"### {selected_category}")
        for title, dua in duas_collection[selected_category]:
            st.markdown(f"#### {title}")
            st.markdown(f"<div dir='rtl' style='font-size:22px; margin:10px 0; '>{dua}</div>", unsafe_allow_html=True)
            st.markdown("---")

# --------------- Ramadan Section 🕌 (Prayer Times) ---------------
def get_prayer_times(country, city):
    """ Fetches prayer times from API """
    url = f"https://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=2"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["data"]["timings"]
    else:
        return None
def ramadan_section():
    st.markdown("<h1 style='color: #FFD700;'>🕌 Prayer Times</h1>", unsafe_allow_html=True)

    countries = ["Pakistan", "Saudi Arabia", "UAE", "USA", "UK", "India", "Bangladesh", "Egypt", "Turkey", "Malaysia"]
    country = st.selectbox("🌍 Select your country:", countries)
    city = st.text_input("🏙️ Enter your city:")
    
    if st.button("🔍 Get Prayer Times"):
        
        if city:
            timings = get_prayer_times(country, city)
            if timings:
                st.markdown("<h3 style='color: #FFD700;'>🕌 Today's Prayer Times:</h3>", unsafe_allow_html=True)

                for prayer, time in timings.items():
                    if prayer in ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]:
                        st.markdown(
                            f"""
                            <div style='background-color: #333; padding: 10px; border-radius: 10px; 
                                        margin-bottom: 10px; color: #E5E5E5;'>
                                <strong style='color: #FFD700;'>{prayer}:</strong> 🕰️ {time}
                            </div>
                            """, 
                            unsafe_allow_html=True
                        )
            else:
                st.error("⚠️ Could not fetch prayer times. Please check your city name.")
        else:
            st.warning("⚠️ Please enter a city.")

# --------------- Dynamic Page Content ---------------
if menu == "🏠 Home":
    home_section()
elif menu == "📖 Quran":
    quran_section()
elif menu == "📿 Tasbeeh":
    tasbeeh_section()
elif menu == "🤲 Duas & Wazaif":
    duas_wazaif_section()
elif menu == "🕌 Ramadan":
    ramadan_section()
