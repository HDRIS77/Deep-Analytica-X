import streamlit as st
import requests
import io
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# إعدادات الصفحة
st.set_page_config(page_title="Intel-Core-X: Devil's Advocate", layout="wide")

# جلب المفتاح بشكل آمن من Streamlit Secrets
# تأكد أن الاسم في Secrets هو GROQ_API_KEY
if "GROQ_API_KEY" in st.secrets:
    API_KEY = st.secrets["GROQ_API_KEY"]
else:
    # استخدام مفتاحك كاحتياطي مؤقت (لا يفضل للنشر العام)
    API_KEY = "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"

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
            box-shadow: 0px 0px 15px #ff0000;
        }
        </style>
        <div class="security-alert">⚠️ تحذير: تم تفعيل بروتوكول محامي الشيطان - جاري استخراج البيانات السوداء ⚠️</div>
    """, unsafe_allow_html=True)

def get_groq_analysis(target):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    
    # استخدام الموديل الأحدث llama-3.3-70b-versatile
    data = {
        "model": "llama-3.3-70b-versatile", 
        "messages": [
            {"role": "system", "content": "أنت محامي الشيطان وخبير استخبارات. فكك الملفات بلا رحمة."},
            {"role": "user", "content": f"حلل {target} استراتيجياً وسياسياً واقتصادياً. اذكر المخططات السرية، المتحكمين الفعليين، وسيناريوهات الانهيار والحلول القاسية."}
        ]
    }
    
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    return f"خطأ في الاتصال: {response.text}"

# واجهة المستخدم
st.title("🔦 عقل Intel-Core-X الاستقصائي")

target_input = st.text_input("أدخل الهدف المراد تشريحه:", placeholder="مثلاً: اقتصاد مصر أو صراعات المنطقة")

if st.button("تفعيل التشريح العميق"):
    if target_input:
        security_alert_ui()
        result = get_groq_analysis(target_input)
        st.markdown("### 📜 التقرير الاستخباراتي المستخرج:")
        st.write(result)
        
        # إضافة زر التحميل (دالة PDF كما في الكود السابق)
    else:
        st.error("أدخل هدفاً أولاً.")
