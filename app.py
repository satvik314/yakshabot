import os
import openai
from openai import OpenAI
import streamlit as st
from streamlit_message import message
from langchain import ConversationChain, ConversationBufferMemory

os.environ['OPENAI_API_KEY'] = st.secrets.OPENAI_API_KEY

st.title("Yaksha Bot")
st.subheader("Get interviewed by AI!")

# Initialize ConversationChain and ConversationBufferMemory
conversation_chain = ConversationChain()
conversation_buffer = ConversationBufferMemory()

# Get user input
user_input = st.chat_input("Enter your query")

# Pass user input into ConversationChain
conversation_chain.add_message(user_input)
