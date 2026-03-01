import streamlit as st
import requests
import datetime
import io
import random
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# --- إعدادات الهوية البصرية (NEXUS DARK MODE) ---
st.set_page_config(page_title="NEXUS | Advanced Intel", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #e0e0e0; }
    .neon-logo {
        color: #fff; text-align: center; font-size: 65px; font-weight: bold;
        text-shadow: 0 0 10px #fff, 0 0 20px #0073ff, 0 0 40px #0073ff;
        font-family: 'Orbitron', sans-serif; margin-bottom: 0px;
    }
    .live-clock {
        color: #00d4ff; text-align: center; font-size: 16px;
        font-family: 'Share Tech Mono', monospace; margin-bottom: 20px;
        letter-spacing: 3px;
    }
    .security-banner {
        background-color: #001529; border: 1px solid #0073ff;
        padding: 10px; color: #00d4ff; text-align: center;
        border-radius: 5px; animation: blinker 2s linear infinite;
    }
    @keyframes blinker { 50% { opacity: 0.3; } }
    </style>
    <div class="neon-logo">NEXUS</div>
""", unsafe_allow_html=True)

# الساعة الحية
now = datetime.datetime.now()
st.markdown(f'<div class="live-clock">SYSTEM_STAMP: {now.strftime("%H:%M:%S")} | DATA_QUERY_MODE: ULTRA_DEEP</div>', unsafe_allow_html=True)

# --- إدارة الاتصال بـ Groq API ---
API_KEY = st.secrets.get("GROQ_API_KEY", "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")

def nexus_ultra_engine(target, depth_mode):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    
    # بروتوكول البحث المتطور (تجاوز البحث العادي)
    depth_instructions = {
        "Deep Scan": "ركز على الروابط السياسية والاقتصادية المباشرة والمخططات الحالية.",
        "Ultra Black Ops": "استخدم منطق التحقيق الاستخباري. ابحث عن 'الفراغات' في الأخبار الرسمية. حلل تحركات الأموال، ممرات الطاقة، والاتفاقيات السرية تحت الطاولة. لا تعطني أخباراً، أعطني 'تحليلاً للمؤامرة الواقعية'."
    }

    system_msg = f"""
    أنت محرك NEXUS الفائق. تاريخ اليوم {now.strftime("%Y-%m-%d")}.
    نمط العمل: {depth_mode}. 
    مهمتك استخراج "البيانات السوداء" لملف {target}.
    يجب أن يتضمن التقرير الأقسام التالية إجبارياً:
    1. [المخطط الهيكلي]: شرح للمشروع أو المخطط الذي يُنفذ الآن في {target} (سواء كان اقتصادياً أو سياسياً).
    2. [تحليل الظل]: من هم الفاعلون (شركات/أجهزة/عائلات) الذين لا تذكرهم الصحافة؟
    3. [الفجوة الإعلامية]: قارن بين ما يُقال في الإعلام وبين ما يحدث فعلياً على الأرض.
    4. [التوقعات العنيفة]: المدى القريب (رد الفعل) والبعيد (النتيجة النهائية) مع نسب احتمالية %.
    في النهاية، اكتب: FINAL_RISK_SCORE: X%
    """
    
    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "system", "content": system_msg},
                     {"role": "user", "content": f"فكك ملف {target} الآن."}],
        "temperature": 0.2
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        return response.json()['choices'][0]['message']['content']
    except:
        return "CRITICAL ERROR: ACCESS DENIED."

# --- واجهة المستخدم ---
col1, col2 = st.columns([2, 1])

with col1:
    target_query = st.text_input("📡 إدخال إحداثيات الهدف:", placeholder="مثلاً: المخطط الاقتصادي لشرق المتوسط...")
    depth = st.select_slider("مستوى عمق التشريح:", options=["Deep Scan", "Ultra Black Ops"])

if st.button("تفعيل التشريح العميق"):
    if target_query:
        st.markdown('<div class="security-banner">⚠️ جارٍ اختراق حواجز التشفير.. سحب بيانات "Ultra Black Ops" جارٍ.. ⚠️</div>', unsafe_allow_html=True)
        
        report = nexus_ultra_engine(target_query, depth)
        
        # استخراج مؤشر الخطر
        risk = "75"
        if "FINAL_RISK_SCORE:" in report:
            risk = report.split("FINAL_RISK_SCORE:")[1].split("%")[0].strip()
        
        st.sidebar.markdown(f"<h1 style='color:#00d4ff; text-align:center;'>{risk}%</h1>", unsafe_allow_html=True)
        st.sidebar.markdown("<p style='text-align:center;'>THREAT PROBABILITY</p>", unsafe_allow_html=True)
        st.sidebar.progress(int(risk))
        
        st.markdown("### 📄 الوثيقة المسربة:")
        st.code(report, language='markdown')
        
        # خيار تحميل PDF
        st.caption(f"تمت المزامنة في: {datetime.datetime.now().strftime('%H:%M:%S')}")
    else:
        st.error("أدخل هدفاً أولاً.")

# خريطة حرارية بسيطة في الأسفل
st.markdown("---")
st.write("🌐 حالة النزاع العالمي (Heat Map Simulation)")
dots = "".join([f'<div style="width:10px; height:10px; background:red; border-radius:50%; position:absolute; top:{random.randint(10,90)}%; left:{random.randint(10,90)}%; box-shadow:0 0 10px red;"></div>' for _ in range(8)])
st.markdown(f'<div style="background:#111; height:200px; position:relative; border-radius:10px; opacity:0.5;">{dots}</div>', unsafe_allow_html=True)
