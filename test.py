import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "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"

# Streamlit app title and description
st.title("Chatbot with OpenAI GPT-3.5 Turbo")
st.write("Ask a question and the chatbot will provide an answer!")

# User input box
user_input = st.text_input("Ask a question:")

# Button to generate response
if st.button("Get Answer"):
    # Create a prompt for the OpenAI API
    prompt = f"Question: {user_input}\nAnswer:"

    # Call the OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can also use "gpt-3.5-turbo"
        prompt=prompt,
        max_tokens=150
    )

    # Extract and display the AI's response
    ai_answer = response.choices[0].text.strip()
    st.write("AI Answer:", ai_answer)
