import streamlit as st
import google.generativeai as genai


# Set up the page configuration
st.set_page_config(
    page_title="EduEquify->A q&a chatbot",
    page_icon="QA_logo.png",
    layout="wide",
    initial_sidebar_state="expanded"
)


genai.configure(api_key=st.secrets["api_key"])
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
            "hello! Myself EQUIFY, the chatbot. How can I help you today?",
          ],
        },
        
        {
          "role": "user",
          "parts": [
            "how can you help me?",
          ],
        },
        {
          "role": "model",
          "parts": [
            "my name is eduequify, i am a chatbot.i can help you to answer any questions.",
          ],
        },
    ]
)

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User interface setup
col1, col2 = st.columns([1, 4])
col1.image("QA_logo.png")
col1.markdown("#EduEquify")

# Main chatbot section
col2.title("Q&A Chatbot")
with col2.expander("About this app"):
    st.write("""
                This chatbot answers the student's questions without any gender discrimination in the response. 😇
            """)

# User input and chat history display
question = st.text_input("Enter your query:")
button = st.button('Submit')

if button and question:
    result = chat_session.send_message(question)
    st.session_state.chat_history.append({"role": "user", "parts": [question]})
    st.session_state.chat_history.append({"role": "model", "parts": [result.text]})
    st.write(result.text)
    question = ""  # Clear the text input after submitting

if st.session_state.chat_history:
    with st.expander("Chat History"):
        for chat in st.session_state.chat_history:
            role = chat["role"]
            parts = chat["parts"]
            if role == "user":
                st.write("User: ", parts[0])
            else:
                st.write("Chatbot: ", parts[0])







