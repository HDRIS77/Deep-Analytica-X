import streamlit as st
import requests
import io
import datetime
import time
import random

# --- إعدادات الهوية البصرية والسمات (NEXUS DARK THEME) ---
st.set_page_config(page_title="NEXUS | Global Intelligence", layout="wide")

# CSS لتخصيص الواجهة بالكامل (اللون الداكن + النيون + الأنيميشن)
st.markdown("""
    <style>
    /* جعل الخلفية سوداء عميقة */
    .stApp {
        background-color: #050505;
        color: #e0e0e0;
    }
    
    /* لوجو NEXUS نيون أزرق مشع */
    .neon-logo {
        color: #fff;
        text-align: center;
        font-size: 70px;
        font-weight: bold;
        text-shadow: 0 0 10px #fff, 0 0 20px #0073ff, 0 0 30px #0073ff, 0 0 40px #0073ff;
        font-family: 'Orbitron', sans-serif;
        margin-top: 10px;
    }
    
    /* الساعة الحية ونظام المزامنة */
    .live-clock {
        color: #00d4ff;
        text-align: center;
        font-size: 18px;
        font-family: 'Share Tech Mono', monospace;
        margin-bottom: 30px;
        text-transform: uppercase;
        letter-spacing: 3px;
    }
    
    /* الخريطة الحرارية الاستخباراتية */
    .heat-map-container {
        border: 1px solid #0073ff;
        background: url('https://upload.wikimedia.org/wikipedia/commons/8/80/World_map_-_low_resolution.svg');
        background-size: cover;
        height: 300px;
        position: relative;
        border-radius: 10px;
        margin-bottom: 20px;
        opacity: 0.4;
    }
    
    .pulse-dot {
        width: 15px; height: 15px; background: red;
        border-radius: 50%; position: absolute;
        box-shadow: 0 0 15px red;
        animation: pulse 1.5s infinite;
    }
    
    @keyframes pulse { 0% { transform: scale(1); opacity: 1; } 100% { transform: scale(3); opacity: 0; } }
    
    /* البانر الأمني الوامض */
    .security-alert {
        background-color: #0a0a0a; border: 2px solid #00d4ff;
        padding: 15px; color: #00d4ff; text-align: center;
        border-radius: 5px; animation: blinker 2s linear infinite;
        font-family: 'Courier New', monospace; margin: 20px 0;
    }
    @keyframes blinker { 50% { opacity: 0.3; } }
    </style>
    
    <div class="neon-logo">NEXUS</div>
""", unsafe_allow_html=True)

# عرض الساعة والوقت المحدث
now = datetime.datetime.now()
st.markdown(f'<div class="live-clock">STATUS: ACTIVE | SYSTEM_TIME: {now.strftime("%H:%M:%S")} | DATA_SYNC: REAL-TIME</div>', unsafe_allow_html=True)

# --- محاكي الخريطة الحرارية (تفاعلية حسب البحث) ---
def display_heat_map():
    # أماكن عشوائية للنقاط الحمراء تعطي إيحاءً بالتوتر العالمي
    dots = ""
    for _ in range(5):
        top = random.randint(20, 80)
        left = random.randint(10, 90)
        dots += f'<div class="pulse-dot" style="top: {top}%; left: {left}%;"></div>'
    
    st.markdown(f'<div class="heat-map-container">{dots}</div>', unsafe_allow_html=True)

# --- إدارة الاتصال بـ Groq API ---
API_KEY = st.secrets.get("GROQ_API_KEY", "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")

def nexus_intelligence_engine(target):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    
    # البرومبت "محامي الشيطان" مع تاريخ اليوم الفعلي
    system_instruction = f"""
    أنت نظام NEXUS العسكري. تاريخ اليوم هو {now.strftime("%Y-%m-%d")}. 
    مهمتك تشريح ملف {target} بلهجة محامي الشيطان. 
    يجب أن يتضمن التقرير: 
    1. رصد ميداني (الأحداث في آخر 24 ساعة). 
    2. تحليل المخططات السفلية (أنفاق، صفقات سلاح، تحركات سرية).
    3. توقعات (المدى القريب: 72 ساعة) و (المدى البعيد: سنوات). 
    في نهاية الرد، اكتب حصراً: "FINAL_RISK_LEVEL: X%" (استبدل X بالنسبة).
    """
    
    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "system", "content": system_instruction},
                     {"role": "user", "content": f"أعطني التقرير المسرب عن {target}"}],
        "temperature": 0.2
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        return response.json()['choices'][0]['message']['content']
    except:
        return "CRITICAL ERROR: CONNECTION REFUSED BY INTEL-CORE."

# --- واجهة العمليات الاستخباراتية ---
display_heat_map()

target_query = st.text_input("📡 أدخل إحداثيات الهدف (اسم الدولة أو الحدث):", placeholder="مثلاً: الانقلاب العسكري المحتمل في X...")

if st.button("تفعيل التشريح العميق"):
    if target_query:
        st.markdown('<div class="security-alert">⚠️ جارٍ اختراق البروتوكولات الإعلامية.. سحب البيانات الحية جارٍ.. ⚠️</div>', unsafe_allow_html=True)
        
        with st.spinner("PROCESSING..."):
            report = nexus_intelligence_engine(target_query)
            
            # استخراج مؤشر الخطر تلقائياً
            risk_score = 70
            if "FINAL_RISK_LEVEL:" in report:
                try: risk_score = int(report.split("FINAL_RISK_LEVEL:")[1].split("%")[0].strip())
                except: pass
            
            # تحديث الشريط الجانبي
            st.sidebar.markdown(f"<h1 style='color:#ff0000; text-align:center;'>{risk_score}%</h1>", unsafe_allow_html=True)
            st.sidebar.markdown("<p style='text-align:center;'>THREAT PROBABILITY</p>", unsafe_allow_html=True)
            st.sidebar.progress(risk_score)
            
            # عرض التقرير
            st.markdown("### 📄 الوثيقة الاستخباراتية المستخرجة:")
            st.code(report, language='markdown') # وضع التقرير داخل صندوق كود ليعطي إيحاء تقني
            
            st.caption(f"توقيت الاستخراج: {datetime.datetime.now().strftime('%H:%M:%S')} | المصدر: NEXUS CORE")
    else:
        st.error("أدخل هدفاً أولاً.")
