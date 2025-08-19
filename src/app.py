import os
import urllib.parse

from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
import streamlit as st

load_dotenv()

raw_password = os.getenv("DB_PASSWORD")
enocoded_password = urllib.parse.quote_plus(raw_password)

# Function to connect with the database
def init_database(user: str,password: str,host: str, port: str, database: str) -> SQLDatabase:
    db_uri = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"
    return SQLDatabase.from_uri(db_uri)


st.set_page_config(page_title="Chat With MySQL",page_icon=":speech_balloon")

st.title("Chat With MySQL")


# Sidebar components
with st.sidebar:
    st.subheader("Settings")
    st.write("Simple Chat application using MySQL, Connect to the database !!")

    st.text_input("Host",value="localhost",key="Host")
    st.text_input("Port",value="3306", key="Port")
    st.text_input("User",value="root", key="User")
    st.text_input("Password",type="password",value=enocoded_password, key="Password")
    
    st.text_input("Database",value="Chinook", key="Database")

    if st.button("Connect"):
        with st.spinner("Connecting to database..."):
            db = init_database(
                st.session_state["User"],
                st.session_state["Password"],
                st.session_state["Host"],
                st.session_state["Port"],
                st.session_state["Database"]
            )

            st.session_state.db = db
            st.success("Connected to Database !!")


st.chat_input("Type a message...")