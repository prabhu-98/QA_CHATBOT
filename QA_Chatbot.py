import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Configure the environment and API key
def configure():
    load_dotenv()

# Set up the page configuration
st.set_page_config(
    page_title="eduequify-a q&a chatbot",
    page_icon="QA_logo.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load the environment and initialize the chatbot model
configure()
genai.configure(api_key=os.getenv('api_key'))
model = genai.GenerativeModel("gemini-pro")

# Start the initial chat session
chat_session = model.start_chat(
    history=[
        {
          "role": "user",
          "parts": [
            "hello",
          ],
        },
        {
          "role": "model",
          "parts": [
            "hello! Myself EQUIFY,the chat bot. How can I help you today?",
          ],
        },
    ]
)

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User interface setup
col1, col2 = st.columns([1, 4])
col1.image(r"c:\users\prabhu das\downloads\eduequify-modified (1).png")
col1.markdown("#eduequify")

# Main chatbot section
col2.title("Q&A Chatbot")
with col2.expander("About this app"):
    st.write("""
                This is a chatbot that answers the questions of the students without any gender discriminations in the response. 😇
            """)

# User input and chat history display
question = st.text_input("Enter your query:")
button = st.button('Submit')

if button and question:
    result = chat_session.send_message(question)
    st.session_state.chat_history.append({"role": "user", "parts": [question]})
    st.session_state.chat_history.append({"role": "model", "parts": [result.text]})
    st.write(result.text)

if st.session_state.chat_history:
    with st.expander("Chat History"):
        for chat in st.session_state.chat_history:
            role = chat["role"]
            parts = chat["parts"]
            if role == "user":
                st.write("User: ", parts[0])
            else:
                st.write("Chatbot: ", parts[0])







