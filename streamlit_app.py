import streamlit as st
import requests
import datetime
import time
import random

# --- نظام الهوية البصرية المتطور (HUD INFRASTRUCTURE) ---
st.set_page_config(page_title="NEXUS | COMMAND & CONTROL", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Share+Tech+Mono&display=swap');

    /* تحويل كامل للموقع للنمط الداكن والنيون */
    .stApp {
        background: #000000;
        background-image: 
            linear-gradient(rgba(0, 242, 255, 0.05) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 242, 255, 0.05) 1px, transparent 1px);
        background-size: 50px 50px;
        color: #00f2ff;
        font-family: 'Share Tech Mono', monospace;
    }

    /* لوجو النيون NEXUS */
    .neon-logo {
        font-family: 'Orbitron', sans-serif;
        color: #fff;
        text-align: center;
        font-size: 85px;
        font-weight: 900;
        text-shadow: 0 0 10px #00f2ff, 0 0 20px #00f2ff, 0 0 40px #0077ff, 0 0 80px #0077ff;
        letter-spacing: 25px;
        padding-top: 20px;
        animation: glow 3s ease-in-out infinite alternate;
    }

    @keyframes glow {
        from { text-shadow: 0 0 10px #00f2ff, 0 0 20px #00f2ff; }
        to { text-shadow: 0 0 20px #00f2ff, 0 0 50px #0077ff, 0 0 100px #0077ff; }
    }

    /* الساعة الحية ونظام التحديث */
    .status-bar {
        text-align: center;
        font-size: 18px;
        color: #00f2ff;
        border: 1px solid #00f2ff;
        width: 60%;
        margin: 10px auto;
        padding: 5px;
        background: rgba(0, 242, 255, 0.1);
        box-shadow: 0 0 15px rgba(0, 242, 255, 0.2);
    }

    /* شاشة الخريطة الحية (Radar Frame) */
    .radar-container {
        border: 2px solid #00f2ff;
        height: 450px;
        background: url('https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJqZ3R5Z3R5Z3R5Z3R5Z3R5Z3R5Z3R5Z3R5Z3R5Z3R5JmU9MSZ0PWE/3o7TKMGpxx7S0C5O0w/giphy.gif');
        background-size: cover;
        position: relative;
        border-radius: 5px;
        box-shadow: 0 0 25px rgba(0, 242, 255, 0.3);
        margin-bottom: 20px;
    }

    /* نقاط الصراع (Hotspots) */
    .war-dot {
        width: 14px; height: 14px; background: #ff0000;
        border-radius: 50%; position: absolute;
        box-shadow: 0 0 20px #ff0000;
        animation: pulse-red 1s infinite;
    }

    @keyframes pulse-red {
        0% { transform: scale(1); opacity: 1; }
        100% { transform: scale(3.5); opacity: 0; }
    }

    /* كروت البيانات الاستخباراتية */
    .intel-card {
        background: rgba(0, 5, 10, 0.9);
        border: 1px solid #00f2ff;
        padding: 15px;
        margin: 5px 0;
        border-left: 4px solid #ff0000;
        font-size: 14px;
    }
    </style>
""", unsafe_allow_html=True)

# --- شاشة الرأس (Header) ---
st.markdown('<div class="neon-logo">NEXUS</div>', unsafe_allow_html=True)
now_time = datetime.datetime.now().strftime("%H:%M:%S")
st.markdown(f'<div class="status-bar">🛰️ LINK_STATUS: SECURE | TIME: {now_time} | PROTOCOL: ULTRA_BLACK_OPS</div>', unsafe_allow_html=True)

# --- الخريطة الحية والبيانات الجانبية (HUD Layout) ---
col_map, col_side = st.columns([3, 1])

with col_map:
    st.markdown('<div class="radar-container">', unsafe_allow_html=True)
    # توليد نقاط اشتعال لايف (تتغير عشوائياً عند كل ضغطة)
    for i in range(7):
        t, l = random.randint(15, 85), random.randint(10, 90)
        st.markdown(f'<div class="war-dot" style="top:{t}%; left:{l}%;"></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_side:
    st.markdown('<div class="intel-card"><b>SYSTEM LOG</b><br>Scanning Darknet...<br>Signals: Intercepted</div>', unsafe_allow_html=True)
    st.markdown('<div class="intel-card" style="border-left: 4px solid #00f2ff;"><b>GEO-INT</b><br>Coordinates Locked<br>Feed: Real-time</div>', unsafe_allow_html=True)
    st.markdown('<div class="intel-card" style="border-left: 4px solid #ffd700;"><b>AI_CORE</b><br>Llama-3.3 Active<br>Logic: DEVIL_ADV</div>', unsafe_allow_html=True)

# --- محرك البحث الاستخباراتي (Groq) ---
API_KEY = st.secrets.get("GROQ_API_KEY", "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")

def nexus_execute_intel(target):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    
    current_full_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    prompt = f"""
    أنت نظام NEXUS للمعلومات العسكرية والتحليل الاستراتيجي. تاريخ ووقت اللحظة الحالية: {current_full_time}.
    المهمة: تشريح ملف {target} فوراً وبدقة متناهية.
    المتطلبات الإجبارية للتقرير:
    1. [المخطط الهيكلي المسكوت عنه]: كشف الخطة الكبرى التي يتم تنفيذها الآن في {target}.
    2. [النقاط المشتعلة]: حدد أماكن التوتر والعمليات الجارية بالدقيقة والثانية.
    3. [المتحكمون في الظل]: اذكر أسماء الجهات والشركات الفاعلة في هذا الملف.
    4. [سيناريو الـ 48 ساعة]: ماذا سيحدث بناءً على التحركات الحالية؟
    5. نسبة الخطر الإجمالية: RISK_SCORE: X%
    استخدم لغة عسكرية، جافة، وصادمة.
    """
    
    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "system", "content": "NEXUS CORE OPERATIONAL AI"},
                     {"role": "user", "content": prompt}],
        "temperature": 0.1
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        return response.json()['choices'][0]['message']['content']
    except:
        return "CRITICAL FAILURE: SIGNAL LOST."

# --- منطقة العمليات (Input Area) ---
target_input = st.text_input("📡 إدخال إحداثيات الهدف (اسم الموضوع):", placeholder="مثلاً: المخطط العسكري في طهران الآن...")

if st.button("EXECUTE DEEP ANALYSIS"):
    if target_input:
        with st.status("🛠️ جارٍ اختراق البروتوكولات الإعلامية وجلب البيانات الحية...", expanded=True) as status:
            st.write("سحب إشارات القمر الصناعي...")
            time.sleep(1)
            st.write("تفكيك التشفير الاستخباراتي...")
            intel_report = nexus_execute_intel(target_input)
            status.update(label="✅ تجميع البيانات المكتمل", state="complete", expanded=False)
        
        # استخراج مؤشر الخطر
        risk = "85"
        if "RISK_SCORE:" in intel_report:
            risk = intel_report.split("RISK_SCORE:")[1].split("%")[0].strip()
        
        # عرض التقرير بأسلوب الشاشات المسربة
        st.markdown(f"### 📄 INTELLIGENCE FEED: {target_input.upper()}")
        st.code(intel_report, language='markdown')
        
        # التنبيهات في الشريط الجانبي
        st.sidebar.markdown(f"<h1 style='color:#ff0000; text-align:center;'>{risk}%</h1>", unsafe_allow_html=True)
        st.sidebar.markdown("<p style='text-align:center;'>THREAT PROBABILITY</p>", unsafe_allow_html=True)
        st.sidebar.progress(int(risk))
    else:
        st.error("Target Coordinates Missing.")

# شريط الأخبار المتحرك في الأسفل (Ticker)
st.markdown("""
    <marquee style="color: #00f2ff; font-family: 'Share Tech Mono'; border-top: 1px solid #00f2ff; padding: 5px;">
        ⚠️ URGENT: NEXUS SATELLITE 01 TRACKING NEW MOVEMENTS IN THE REGION... STATUS: MONITORING... ⚠️
    </marquee>
""", unsafe_allow_html=True)
