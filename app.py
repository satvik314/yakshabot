import os
import openai
from openai import OpenAI
import streamlit as st
from streamlit_message import message

os.environ['OPENAI_API_KEY'] = st.secrets.OPENAI_API_KEY

st.title("Yaksha Bot")
st.subheader("Get interviewed by AI!")

st.chat_input("Enter your query")