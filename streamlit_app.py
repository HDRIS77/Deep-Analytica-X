import streamlit as st
import requests
import datetime
import time
import random

# --- إعدادات الواجهة الفائقة (HUD Style) ---
st.set_page_config(page_title="NEXUS COMMAND CENTER", layout="wide")

st.markdown("""
    <style>
    /* خلفية داكنة جداً مع تدرج لوني استخباراتي */
    .stApp {
        background: radial-gradient(circle, #001220 0%, #000000 100%);
        color: #00d4ff;
        font-family: 'Share Tech Mono', monospace;
    }
    
    /* لوجو NEXUS نيون ثلاثي الأبعاد */
    .nexus-logo {
        text-align: center;
        font-size: 80px;
        font-weight: 900;
        color: #fff;
        text-shadow: 0 0 10px #0073ff, 0 0 20px #0073ff, 0 0 40px #0073ff, 0 0 80px #0073ff;
        letter-spacing: 15px;
        margin-top: 10px;
        text-transform: uppercase;
    }

    /* شريط البيانات العلوي */
    .top-bar {
        border-bottom: 2px solid #0073ff;
        padding: 10px;
        display: flex;
        justify-content: space-between;
        font-size: 14px;
        background: rgba(0, 115, 255, 0.1);
    }

    /* تصميم كروت البيانات (HUD Units) */
    .hud-box {
        border: 1px solid #0073ff;
        padding: 20px;
        background: rgba(0, 0, 0, 0.6);
        border-radius: 5px;
        box-shadow: inset 0 0 15px rgba(0, 115, 255, 0.2);
        margin-bottom: 20px;
    }

    /* الأنيميشن الخاص بالنبض الأحمر للمناطق الساخنة */
    @keyframes pulse-red {
        0% { transform: scale(1); opacity: 1; }
        100% { transform: scale(2.5); opacity: 0; }
    }
    .hotspot {
        width: 12px; height: 12px; background: #ff0000;
        border-radius: 50%; position: absolute;
        box-shadow: 0 0 20px #ff0000;
        animation: pulse-red 2s infinite;
    }
    </style>
""", unsafe_allow_html=True)

# --- الهيكل العلوي للموقع ---
st.markdown('<div class="nexus-logo">NEXUS</div>', unsafe_allow_html=True)

now = datetime.datetime.now()
st.markdown(f"""
    <div class="top-bar">
        <span>🛰️ SAT-LINK: ACTIVE</span>
        <span>🕒 {now.strftime("%H:%M:%S")}</span>
        <span>🌍 TARGETING_SYSTEM: READY</span>
    </div>
""", unsafe_allow_html=True)

# --- محاكي الخريطة الحرارية (World Map HUD) ---
st.markdown('<div class="hud-box" style="height: 350px; position: relative; overflow: hidden; background: url(\'https://i.pinimg.com/originals/05/26/13/05261394f55a1599386d3896504a3770.gif\'); background-size: cover; opacity: 0.6;">', unsafe_allow_html=True)
# إضافة نقاط نبض عشوائية
for i in range(6):
    t, l = random.randint(10, 80), random.randint(5, 95)
    st.markdown(f'<div class="hotspot" style="top:{t}%; left:{l}%;"></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- المحرك الاستخباراتي (Groq) ---
API_KEY = st.secrets.get("GROQ_API_KEY", "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")

def nexus_command_engine(target, mode):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    
    system_instr = f"""
    أنت نظام NEXUS للمعلومات العسكرية. تاريخ اليوم: {now.strftime("%Y-%m-%d")}.
    النمط المفعّل: {mode}.
    مهمتك تشريح ملف {target} بأسلوب محامي الشيطان.
    ركز على: 1. المخططات غير المعلنة. 2. أسماء الفاعلين خلف الستار. 3. الفجوات الإعلامية. 4. جداول زمنية دقيقة بالثانية والدقيقة.
    في النهاية، اكتب إجبارياً: RISK_SCORE: X%
    """
    
    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "system", "content": system_instr},
                     {"role": "user", "content": f"أعطني التقرير السري حول {target}"}],
        "temperature": 0.2
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        return response.json()['choices'][0]['message']['content']
    except:
        return "CRITICAL ERROR: CONNECTION TO CORE LOST."

# --- منطقة التحكم والمدخلات ---
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<div class="hud-box">', unsafe_allow_html=True)
    target = st.text_input("📍 أدخل إحداثيات الهدف الاستراتيجي:", placeholder="دولة، منظمة، أو حدث عاجل...")
    mode = st.radio("إعدادات التشريح المعرفي:", ["Deep Investigation", "Ultra Black Ops (كشف المخططات)"], horizontal=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="hud-box">', unsafe_allow_html=True)
    st.write("📊 إحصائيات النظام")
    st.write(f"CPU: {random.randint(40, 70)}%")
    st.write(f"ENCRYPTION: 256-bit")
    st.write(f"SOURCES: Classified")
    st.markdown('</div>', unsafe_allow_html=True)

if st.button("🔥 بدء التشريح العميق"):
    if target:
        st.write("⏳ جاري اختراق البروتوكولات...")
        report = nexus_command_engine(target, mode)
        
        # معالجة مؤشر الخطر
        risk = "90"
        if "RISK_SCORE:" in report:
            risk = report.split("RISK_SCORE:")[1].split("%")[0].strip()
        
        # عرض النتائج
        st.markdown(f"""
            <div class="hud-box" style="border-color: #ff0000;">
                <h2 style="color: #ff0000; text-align: center;">REPORT DATA: {target.upper()}</h2>
                <h3 style="text-align: center; color: #fff;">LIVE THREAT LEVEL: {risk}%</h3>
            </div>
        """, unsafe_allow_html=True)
        
        st.code(report, language="markdown") # عرض التقرير كأكواد مسربة
        
        st.sidebar.markdown(f"<h1 style='color:red; text-align:center;'>{risk}%</h1>", unsafe_allow_html=True)
        st.sidebar.progress(int(risk))
    else:
        st.warning("يرجى إدخال هدف أولاً.")
