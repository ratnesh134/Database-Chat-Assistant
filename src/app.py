from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.set_page_config(page_title="Chat With MySQL",page_icon=":speech_balloon")

st.title("Chat With MySQL")


# Sidebar components
with st.sidebar:
    st.subheader("Settings")
    st.write("Simple Chat application using MySQL, Connect to the database !!")

    st.text_input("Host",value="localhost")
    st.text_input("Port",value="3306")
    st.text_input("User",type="password",value="Ratneshm@7$")
    st.text_input("Database",value="Chinook")

    st.button("Connect")


st.chat_input("Type a message...")