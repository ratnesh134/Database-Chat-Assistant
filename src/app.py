from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.set_page_config(page_title="Chat With MySQL",page_icon=":speech_balloon")

st.title("Chat With MySQL")