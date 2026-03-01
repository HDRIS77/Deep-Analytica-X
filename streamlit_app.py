import streamlit as st
import requests
import os
import io
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

# إعدادات الصفحة
st.set_page_config(page_title="Intel-Core-X: Devil's Advocate", layout="wide")

# استدعاء المفتاح السري (يجب وضعه في Streamlit Secrets)
if "MY_SECRET_API_KEY" in st.secrets:
    API_KEY = st.secrets["MY_SECRET_API_KEY"]
else:
    st.error("خطأ أمني: مفتاح الـ API غير موجود في إعدادات Streamlit Secrets.")
    st.stop()

# دالة التنبيهات الأمنية الوامضة (CSS Animation)
def security_alert_ui():
    st.markdown("""
        <style>
        @keyframes blink { 50% { opacity: 0; } }
        .blink-bg {
            background-color: #ff0000; padding: 15px; color: white;
            font-weight: bold; text-align: center; border-radius: 5px;
            animation: blink 0.8s linear infinite; margin: 10px 0;
            border: 2px solid black;
        }
        </style>
        <div class="blink-bg">⚠️ فحص استخباري جارٍ: يتم الآن تشريح الفجوات الأمنية والسياسية ⚠️</div>
    """, unsafe_allow_html=True)

def get_ai_analysis(prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent?key={API_KEY}"
    headers = {'Content-Type': 'application/json'}
    data = {"contents": [{"parts": [{"text": prompt}]}]}
    response = requests.post(url, headers=headers, json=data)
    return response.json()['candidates'][0]['content']['parts'][0]['text']

# دالة إنشاء PDF سري للغاية
def create_pdf(target, content):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(1*inch, 10.5*inch, f"TOP SECRET REPORT: {target}")
    c.setFont("Helvetica", 10)
    text_obj = c.beginText(1*inch, 10*inch)
    for line in content.split('\n'):
        text_obj.textLine(line[:90])
    c.drawText(text_obj)
    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer

# واجهة المستخدم
st.title("🔍 محرك محامي الشيطان للاستخبارات")

target = st.text_input("أدخل الدولة أو الهدف المراد تحليله:")

if st.button("بدء التشريح العميق"):
    if target:
        security_alert_ui() # التنبيه الأحمر الوامض
        
        # البرومبت القاسي (محامي الشيطان)
        devil_prompt = f"""
        أنت الآن محامي الشيطان وخبير مخابرات. فكك وضع {target} بلا رحمة:
        1. الكوارث المخفية ولعبة العرائس.
        2. من المتحكم الحقيقي خلف الستار؟
        3. سيناريو الانهيار القريب والبعيد.
        4. حلول ميكافيلية قاسية.
        تحدث بلهجة استقصائية حادة جداً.
        """
        
        analysis = get_ai_analysis(devil_prompt)
        st.markdown("### 📊 النتائج المسربة:")
        st.write(analysis)
        
        pdf_data = create_pdf(target, analysis)
        st.download_button("📂 تحميل التقرير السري (PDF)", pdf_data, f"INTEL_{target}.pdf")
