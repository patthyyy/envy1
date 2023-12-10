import streamlit as st
import openai
# import openai
import json
import pandas as pd

user_api_key = st.sidebar.text_input("OpenAI API key", type= "password")

client = openai.OpenAI(api_key = user_api_key)

st.title('Writing tutor')
st.markdown('Input the writing that you want to improve. \n The AI will give you suggestions on how to improve it.')
user_input = st.text_area('Enter text:', 'Your text heare')
