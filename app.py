from dotenv import load_dotenv
load_dotenv()

import os
import google.generativeai as genai 
import streamlit as st

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))  # Fix the method name to configure
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)  # Fix the parameter name to stream
    return response

st.set_page_config("Q&A Chatbot")
st.header("Conversational Chatbot")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input_text = st.text_input("Input: ", key="input")
submit = st.button("Send")

if input_text and submit:
    response = get_gemini_response(input_text)
    st.session_state['chat_history'].append(("You", input_text))
    st.subheader("Response:")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Response", chunk.text))

st.subheader("Chat History:")
for role, response in st.session_state['chat_history']:
    st.write(f"{role}: {response}")
