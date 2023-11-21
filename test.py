import os
import streamlit as st
from streamlit_chat import message
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI API
openai_api_key = st.secrets.OPENAI_API_KEY

# Initialize LLM
llm = OpenAI(temperature=0, openai_api_key=openai_api_key)

# Initialize memory
memory = ConversationBufferMemory()

# Initialize conversation chain
conversation = ConversationChain(llm=llm, memory=memory)

st.title("Chat with AI")

# Initialize chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def get_text():
    input_text = st.text_input("You: ", "", key="input")
    return input_text

user_input = get_text()

if user_input:
    output = conversation.predict(input=user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output.text)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['generated'][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')