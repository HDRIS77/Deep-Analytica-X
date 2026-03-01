import streamlit as st
import requests
import os
import io
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

# إعدادات الصفحة
st.set_page_config(page_title="Intel-Core-X: Devil's Advocate", layout="wide")

# استدعاء الـ API Key من إعدادات Streamlit
API_KEY = st.secrets["MY_SECRET_API_KEY"]

# دالة التنبيهات الأمنية الوامضة
def security_alert():
    st.markdown("""
        <style>
        @keyframes blinker { 50% { opacity: 0; } }
        .security-alert {
            background-color: #ff4b4b; padding: 20px; color: white;
            font-weight: bold; text-align: center; border-radius: 10px;
            animation: blinker 1s linear infinite; margin-bottom: 20px;
        }
        </style>
        <div class="security-alert">⚠️ تحذير أمني: تم اكتشاف فجوة استخباراتية خطيرة - جاري تشريح البيانات المسكوت عنها ⚠️</div>
    """, unsafe_allow_html=True)

def get_ai_analysis(prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent?key={API_KEY}"
    headers = {'Content-Type': 'application/json'}
    data = {"contents": [{"parts": [{"text": prompt}]}]}
    response = requests.post(url, headers=headers, json=data)
    return response.json()['candidates'][0]['content']['parts'][0]['text']

# دالة توليد PDF سري للغاية
def create_top_secret_pdf(target, content):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    c.setStrokeColorRGB(0.7, 0, 0)
    c.rect(0.2*inch, 0.2*inch, width-0.4*inch, height-0.4*inch, stroke=1)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(0.5*inch, height-0.5*inch, "INTEL-CORE-X SYSTEM / TOP SECRET")
    c.setFont("Helvetica", 10)
    text_obj = c.beginText(0.6*inch, height-1.5*inch)
    for line in content.split('\n'):
        text_obj.textLine(line[:90])
    c.drawText(text_obj)
    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer

# واجهة المستخدم
st.title("🔍 منصة التحليل الاستخباري (محامي الشيطان)")

target = st.text_input("أدخل الهدف المراد تشريحه:")

if st.button("بدء التحليل العميق"):
    if target:
        security_alert() # تفعيل التنبيه الوامض
        
        # برومبت محامي الشيطان المطور
        prompt = f"""أنت الآن محامي الشيطان وخبير استخبارات. حلل {target} بدون تملق. 
        1. الوجه القبيح والكوارث المخفية. 2. لعبة العرائس والمتحكمون الحقيقيون. 
        3. سيناريو الانهيار القادم. 4. خطة النجاة الميكافيلية.
        تحدث بلهجة حادة ومباشرة."""
        
        analysis = get_ai_analysis(prompt)
        st.markdown("### 📊 التقرير الاستخباراتي:")
        st.write(analysis)
        
        pdf = create_top_secret_pdf(target, analysis)
        st.download_button("📂 تحميل التقرير (TOP SECRET PDF)", pdf, f"{target}_report.pdf")
