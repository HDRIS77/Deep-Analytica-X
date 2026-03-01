import streamlit as st
import requests
import io
import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# --- إعدادات الصفحة الفنية ---
st.set_page_config(page_title="Intel-Core-X | Devil's Advocate", layout="wide", initial_sidebar_state="expanded")

# --- إدارة المفتاح السري ---
# ملاحظة: سيحاول الكود جلب المفتاح من Secrets أولاً، وإذا لم يجده سيستخدم المفتاح الذي زودتني به.
GROQ_API_KEY = st.secrets.get("GROQ_API_KEY", "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")

# --- دالة التنبيه الأمني الوامض (CSS) ---
def trigger_security_alert():
    st.markdown("""
        <style>
        @keyframes blinker { 50% { opacity: 0; } }
        .security-banner {
            background-color: #660000; border: 4px solid #ff0000;
            padding: 20px; color: #ffffff; font-weight: bold;
            text-align: center; border-radius: 12px;
            animation: blinker 0.7s linear infinite;
            box-shadow: 0px 0px 20px #ff0000; margin-bottom: 25px;
            font-family: 'Courier New', Courier, monospace;
        }
        </style>
        <div class="security-banner">
            ⚠️ بروتوكول "محامي الشيطان" نشط: يتم الآن اختراق التعتيم الإعلامي وتحليل الفجوات الاستخباراتية ⚠️
        </div>
    """, unsafe_allow_html=True)

# --- محرك التحليل (Groq API) ---
def fetch_devil_analysis(target):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    # البرومبت المطور للتحليل الزمني ونسب الاحتمالات
    system_prompt = """أنت "كبير المحللين في وكالة استخبارات" تعمل بصفة محامي الشيطان. 
    وظيفتك تفكيك الأحداث الجارية (مثل ملفات إيران، الحروب، والاغتيالات) بدقة عسكرية. 
    لا تجامل، لا تملق، اذكر الحقائق القاسية والمخططات المسكوت عنها."""
    
    user_prompt = f"""
    قم بتشريح ملف {target} بناءً على القواعد التالية:
    1. **رصد الأحداث العاجلة**: اربط التحليل بآخر الأخبار (مثل الاغتيالات، التحركات العسكرية، أو الانهيارات الاقتصادية).
    2. **الجدول الزمني للعمليات**: حدد تواريخ مفصلية لما حدث وما سيحدث بناءً على المعطيات.
    3. **تحليل المخطط (The Deep Scheme)**: ما هو المخطط الذي يخدمه هذا الحدث؟ (تغيير ديموغرافي، سيطرة طاقة، إلخ).
    4. **تقدير الموقف (قريب المدى - 3 أشهر)**: توقع الرد أو الخطوة القادمة بدقة مع نسبة احتمالية (%).
    5. **تقدير الموقف (بعيد المدى - 5 سنوات)**: شكل المنطقة أو الدولة المستقبلي مع نسبة احتمالية (%).
    6. **مؤشر خطر الصراع**: أعطِ تقييماً من 100% لمدى خطورة الموقف حالياً.
    """

    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.5 # درجة منخفضة لضمان الدقة التحليلية وعدم التخريف
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        return f"فشل في الاتصال بالعقل الاصطناعي: {str(e)}"

# --- دالة صناعة التقرير PDF السري ---
def generate_pdf_report(target, text):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    c.setStrokeColorRGB(0.5, 0, 0)
    c.rect(15, 15, width-30, height-30, stroke=1)
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width/2, height-50, f"CLASSIFIED REPORT: {target.upper()}")
    c.setFont("Helvetica", 10)
    c.drawString(50, height-70, f"DATE: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
    
    to = c.beginText(50, height-100)
    for line in text.split('\n'):
        to.textLine(line[:95])
    c.drawText(to)
    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer

# --- واجهة المستخدم (Streamlit UI) ---
st.title("🔦 المنصة الاستخباراتية: Intel-Core-X")
st.markdown("---")

with st.sidebar:
    st.header("⚙️ إعدادات المحلل")
    st.info("المنصة مفعلة الآن بنمط 'محامي الشيطان' للبحث عن الحقائق غير المعلنة.")
    risk_threshold = st.slider("مستوى الحذر الاستراتيجي", 0, 100, 85)

# المدخلات
target_subject = st.text_input("أدخل الدولة، المحافظة، أو القضية العاجلة:", placeholder="مثلاً: الصراع الإيراني الإسرائيلي حالياً")

if st.button("تفعيل التشريح الاستخباراتي"):
    if target_subject:
        # 1. إظهار التنبيه الوامض
        trigger_security_alert()
        
        # 2. جلب التحليل
        with st.spinner("جاري معالجة البيانات وتحليل المسارات الزمنية..."):
            raw_analysis = fetch_devil_analysis(target_subject)
            
            # 3. عرض النتائج
            st.markdown("### 📊 التقرير الاستراتيجي المستخرج:")
            st.markdown(raw_analysis)
            
            # 4. مؤشر الخطر (قيمة افتراضية مستخرجة من النص لو أمكن، أو عرض ثابت)
            st.sidebar.warning(f"مؤشر خطر الصراع الحالي: {risk_threshold}%")
            
            # 5. زر تحميل الـ PDF
            report_pdf = generate_pdf_report(target_subject, raw_analysis)
            st.download_button(
                label="📥 تحميل الوثيقة المسربة (PDF)",
                data=report_pdf,
                file_name=f"INTEL_REPORT_{target_subject}.pdf",
                mime="application/pdf"
            )
    else:
        st.error("⚠️ يرجى إدخال هدف للتحليل.")
