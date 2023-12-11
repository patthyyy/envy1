
import streamlit as st
import openai
import json
import pandas as pd

# Get the API key from the sidebar called OpenAI API key
user_api_key = st.sidebar.text_input("OpenAI API key", type="password")

client = openai.OpenAI(api_key=user_api_key)
prompt = """Imagine yourself as a pharmacist. You will receive a patient's symptoms and recommend medications. Provide suggestions in a JSON array with one suggestion per line. Each suggestion should include the following fields:
- "Symptoms"
- "Recommended Medication"
- "Medication Class"
- "Administration Method"
Wait for the user to initiate the conversation before providing any information."""    


st.title('Medicine doctor')
st.markdown('Input a patient \'s symptoms that you want to treat. \n\
            The AI will give you suggestions on how to treat it.')

user_input = st.text_area("Enter some symtoms to treat:", "Your text here")


# submit button after text input
if st.button('Submit'):
    messages_so_far = [
        {"role": "system", "content": prompt},
        {'role': 'user', 'content': user_input},
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages_so_far
    )
    # Show the response from the AI in a box
    # st.markdown('**AI response:**')
    # suggestion_dictionary = response.choices[0].message.content


    # sd = json.loads(suggestion_dictionary)

    # print (sd)
    # suggestion_df = pd.DataFrame.from_dict(sd)
    # print(suggestion_df)
    # st.table(suggestion_df)
     # Extract AI's reply from the response
    ai_reply = response['choices'][0]['message']['content']
    
    # Show the response from the AI in a box
    st.markdown('**AI response:**')
    st.write(ai_reply)