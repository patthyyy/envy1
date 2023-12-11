import streamlit as st
import openai

# ใส่ API key ของคุณที่ได้จาก OpenAI
openai.api_key = "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"

# ข้อความเริ่มต้นที่จะให้กับผู้ใช้
prompt = """Imagine yourself as a pharmacist. You will receive a patient's symptoms and recommend medications. Provide suggestions in a JSON array with one suggestion per line. Each suggestion should include the following fields:
- "Symptoms"
- "Recommended Medication"
- "Medication Class"
- "Administration Method"
Wait for the user to initiate the conversation before providing any information."""

# สร้างหน้าต่าง Streamlit
st.title('Medicine Doctor')
st.markdown('Input a patient\'s symptoms that you want to treat. \n\
            The AI will give you suggestions on how to treat it.')

# กล่องใส่ข้อความของผู้ใช้
user_input = st.text_area("Enter some symptoms to treat:", "Your text here")

# ปุ่ม Submit
if st.button('Submit'):
    # สร้างโครงสร้างข้อความสำหรับ OpenAI API
    messages = [
        {"role": "system", "content": prompt},
        {'role': 'user', 'content': user_input},
    ]

    # ใช้ OpenAI API เพื่อรับการตอบกลับ
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7,
        max_tokens=150
    )

    # นำข้อความตอบกลับจาก OpenAI
    ai_reply = response['choices'][0]['message']['content']

    # แสดงผลลัพธ์จาก OpenAI
    st.markdown('**AI Response:**')
    st.write(ai_reply)
