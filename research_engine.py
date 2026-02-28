import os
import requests

# هذا الجزء لجلب المفتاح السري الذي وضعته في الـ Settings
API_KEY = os.getenv('MY_SECRET_API_KEY') 

def get_ai_analysis(prompt):
    """
    هذه الوظيفة ترسل طلبك لعقل الذكاء الاصطناعي ليقوم بالتحليل العميق.
    سأفترض أنك تستخدم Google Gemini لأنه الأفضل في الربط التاريخي حالياً.
    """
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent?key={API_KEY}"
    headers = {'Content-Type': 'application/json'}
    data = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }
    
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['candidates'][0]['content']['parts'][0]['text']
    else:
        return f"خطأ في الاتصال: {response.text}"

def deep_investigation(topic):
    # تعليمات "محامي الشيطان" للذكاء الاصطناعي ليكون استقصائياً
    investigation_prompt = f"""
    أنت الآن محقق استقصائي خبير ومحلل جيوسياسي. حلل الموضوع التالي: {topic}
    المطلوب منك تنفيذ الآتي بدقة متناهية:
    1. مذكرات الأحداث: جدول زمني من البداية للنهاية.
    2. الروابط الخفية: من هم الأشخاص أو الجهات المرتبطة بهذا الموضوع (حتى لو لم تذكرهم الصحف الرسمية حالياً).
    3. تحليل الفجوات (Gap Analysis): ما هي النقاط التي يتجنب الإعلام الحديث عنها؟ وما هي الصور أو التسريبات التي أحدثت جدلاً؟
    4. السياق التاريخي: هل هذا الحدث مرتبط بأحداث قديمة مشابهة؟
    
    اجعل الأسلوب سردي مفصل (Long-form) وكأنك تكتب تقرير استخباراتي خاص.
    """
    return get_ai_analysis(investigation_prompt)

# لتجربة المحرك على موضوع "جزيرة إبشتاين"
if __name__ == "__main__":
    result = deep_investigation("جزيرة إبشتاين")
    print(result)
