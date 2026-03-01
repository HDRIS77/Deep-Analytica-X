import streamlit as st
import requests
import io
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# إعدادات الصفحة
st.set_page_config(page_title="Intel-Core-X: Devil's Advocate", layout="wide")

# جلب المفتاح من Secrets (تأكد من وضعه في إعدادات Streamlit Secrets باسم GROQ_API_KEY)
# أو يمكنك وضعه مؤقتاً هنا للتجربة ولكن لا ينصح بذلك برمجياً
API_KEY = st.secrets.get("GROQ_API_KEY", "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")

# دالة التنبيه الأمني الوامض
def security_alert_ui():
    st.markdown("""
        <style>
        @keyframes blinker { 50% { opacity: 0; } }
        .security-alert {
            background-color: #8b0000; border: 3px solid #ff0000;
            padding: 20px; color: #ffffff; font-weight: bold;
            text-align: center; border-radius: 10px;
            animation: blinker 0.6s linear infinite; margin-bottom: 25px;
            font-size: 20px; box-shadow: 0px 0px 15px #ff0000;
        }
        </style>
        <div class="security-alert">⚠️ تحذير: تم تفعيل بروتوكول محامي الشيطان - جاري استخراج البيانات السوداء ⚠️</div>
    """, unsafe_allow_html=True)

def get_groq_analysis(target):
    # استخدام موديل Llama 3 من Groq للتحليل الاستخباري
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    prompt = f"""
    أنت الآن "محامي الشيطان" (The Devil's Advocate). وظيفتك هي تفكيك ملف {target} استخباراتياً.
    ممنوع التملق، ممنوع المجاملة، وممنوع استخدام لغة دبلوماسية.
    حلل الآتي:
    1. المخططات السوداء: ما الذي يحدث خلف الستار وتحت الأرض (أنفاق، مراكز بيانات سرية، صفقات مشبوهة)؟
    2. المحركون الفعليون: من يملك القرار المالي والسياسي الحقيقي في {target} بعيداً عن الرواية الرسمية؟
    3. التشبيك الدولي: كيف يتم استخدام هذه الدولة كقطعة شطرنج في صراع القوى العظمى؟
    4. التنبؤ بالكارثة: متى وكيف سيحدث الانهيار القادم؟ أعطِ أرقاماً وتحليلات ميكافيلية باردة.
    5. الحل القاسي: خطة نجاة مجردة من الإنسانية لإنقاذ هيكل الدولة.
    """

    data = {
        "model": "llama3-8b-8192", # موديل قوي وسريع جداً
        "messages": [{"role": "system", "content": "أنت خبير استخبارات عسكري لا يعرف الرحمة."},
                     {"role": "user", "content": prompt}]
    }
    
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"خطأ في الاتصال بالسيرفر السري: {response.text}"

def create_pdf(target, text):
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(300, 800, f"TOP SECRET REPORT: {target.upper()}")
    c.line(50, 780, 550, 780)
    
    text_object = c.beginText(50, 750)
    text_object.setFont("Helvetica", 10)
    for line in text.split('\n'):
        text_object.textLine(line[:100])
    c.drawText(text_object)
    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer

# واجهة الموقع
st.title("🔦 عقل Intel-Core-X الاستقصائي")
st.sidebar.warning("هذه المنصة تعمل ببروتوكول محامي الشيطان. المعلومات قد تكون صادمة.")

target_input = st.text_input("أدخل الدولة أو القضية المراد تشريحها:", placeholder="مثلاً: صراعات شرق المتوسط أو اقتصاد منطقة X")

if st.button("تفعيل التشريح العميق"):
    if target_input:
        security_alert_ui() # التنبيه الأحمر الوامض
        
        analysis_res = get_groq_analysis(target_input)
        
        st.markdown("### 📜 التقرير الاستخباراتي المستخرج:")
        st.write(analysis_res)
        
        pdf_file = create_pdf(target_input, analysis_res)
        st.download_button("📥 تحميل الوثيقة السرية (PDF)", pdf_file, f"DEVL_ADV_{target_input}.pdf")
    else:
        st.error("أدخل هدفاً أولاً.")
