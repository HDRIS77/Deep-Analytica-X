import streamlit as st
import requests
import os

# إعدادات الصفحة
st.set_page_config(page_title="Deep Analytica X", layout="wide")

# استدعاء الـ API Key من إعدادات Streamlit الآمنة
API_KEY = st.secrets["MY_SECRET_API_KEY"]

def get_ai_response(prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent?key={API_KEY}"
    headers = {'Content-Type': 'application/json'}
    data = {"contents": [{"parts": [{"text": prompt}]}]}
    try:
        response = requests.post(url, headers=headers, json=data)
        return response.json()['candidates'][0]['content']['parts'][0]['text']
    except:
        return "حدث خطأ في الاتصال بالعقل الاصطناعي. تأكد من الـ API Key."

# الواجهة
st.title("🔍 منصة التحليل الاستقصائي والجيوسياسي")
st.markdown("---")

# القائمة الجانبية (Sidebar) للهيستوري والإعدادات
with st.sidebar:
    st.header("📜 سجل البحث")
    if 'history' not in st.session_state:
        st.session_state.history = []
    for item in st.session_state.history:
        st.write(f"- {item}")

# منطقة المدخلات
col1, col2 = st.columns([3, 1])
with col1:
    target = st.text_input("أدخل الهدف (دولة، محافظة، أو قضية):", placeholder="مثلاً: جزيرة إبشتاين أو محافظة الإسكندرية")
with col2:
    mode = st.selectbox("نوع التحليل:", ["استقصائي (كشف المسكوت عنه)", "اقتصادي وجيوسياسي"])

if st.button("بدأ التحليل العميق"):
    if target:
        with st.spinner("جاري جلب البيانات والربط بين الأحداث..."):
            if mode == "استقصائي (كشف المسكوت عنه)":
                prompt = f"حلل {target} استقصائياً: مذكرات الأحداث، الروابط الخفية، وما لم يذكره الإعلام."
            else:
                prompt = f"حلل {target} اقتصادياً: المشاكل، الحلول المبتكرة، وتأثير السياسة."
            
            answer = get_ai_response(prompt)
            st.session_state.history.append(target)
            
            st.markdown("### 📊 النتيجة:")
            st.write(answer)
            
            # زر التحميل
            st.download_button("تحميل التقرير (Text)", answer, file_name=f"{target}_report.txt")
    else:
        st.warning("يرجى إدخال هدف للبحث.")
