from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
import streamlit as st

load_dotenv()


# Function to connect with the database
def init_database(user: str,password: str, port: str, database: str) -> SQLDatabase:
    db_uri = f"mysql://{user}:{password}@{host}:{port}/{database}"
    return SQLDatabase.from_uri(db_uri)


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