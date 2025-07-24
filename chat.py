from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
import os
os.environ["GOOGLE_API_KEY"] = "AIzaSyBlJ6adeOgncS9jFKQv_PSypeIsT0ZzmG8"
import google.generativeai as genai
genai.configure(api_key='YOUR_API_KEY')

model = genai.GenerativeModel('gemini-2.0-flash')  # works only with v1



genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#function to load Gemini Pro model and get response
model=genai.GenerativeModel("gemini-2.0-flash")
chat=model.start_chat(history=[])

def get_gemini_response(question):
    response=chat.send_message(question,stream=True)
    return response

##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("TechManiAI")

# Initialize session state for chat history if it dosen't exist
if  'chat-history' not in st.session_state:
    st.session_state['chat_history'] = []

input=st.text_input("Input:",key="input")
submit=st.button("Ask Your Question") 

if submit and input:
    response=get_gemini_response(input)
    ## Add user query and response to session chat history
    st.session_state['chat_history'].append(("You",input))
    st.subheader("TechManiAI")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("BOT",chunk.text))
st.subheader("The chat history is")

for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")