import os
import urllib.parse

from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

load_dotenv()

# Encoding the password, to avoid errors
raw_password = os.getenv("DB_PASSWORD")
enocoded_password = urllib.parse.quote_plus(raw_password) 

# Function to connect with the database
def init_database(user: str,password: str,host: str, port: str, database: str) -> SQLDatabase:
    db_uri = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"
    return SQLDatabase.from_uri(db_uri)


# SQL Chain
def get_sql_chain(db):
    template = """
    You are a data analyst at a company. You are interacting with a user who is asking you questions about the company's database.
    Based on the table schema below, write a SQL query that would answer the user's question. Take the conversation history into account.
    
    <SCHEMA>{schema}</SCHEMA>
    
    Conversation History: {chat_history}
    
    Write only the SQL query and nothing else. Do not wrap the SQL query in any other text, not even backticks.
    
    For example:
    Question: which 3 artists have the most tracks?
    SQL Query: SELECT ArtistId, COUNT(*) as track_count FROM Track GROUP BY ArtistId ORDER BY track_count DESC LIMIT 3;
    Question: Name 10 artists
    SQL Query: SELECT Name FROM Artist LIMIT 10;
    
    Your turn:
    
    Question: {question}
    SQL Query:
    """
    prompt = ChatPromptTemplate(template)
    llm = ChatGroq(model="llama-3.3-70b-versatile")

    def get_schema(_):
        return db.get_table_info()  # returns the table schema of the database
    
    
    # Chain formation
    return (                               
    RunnablePassthrough.assign(schema=get_schema)
    | prompt
    | llm
    | StrOutputParser
    )

# Chat History Initialization
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content="Hello! I'm a SQL assistant. Ask me anything about your database"),

    ]


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


for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.markdown(message.content)
    
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.markdown(message.content)

# Chat block
user_query = st.chat_input("Type a message...") 


# Chat History Storage                                                                                                                  
if user_query is not None and user_query.strip()!="":
    st.session_state.chat_history.append(HumanMessage(content=user_query))

    with st.chat_message("Human"):    # to showcase the message on the screen
        st.markdown(user_query)

    with st.chat_message("AI"):
        response = "I don't know how to respond to that. "
        st.markdown(response)

    st.session_state.chat_history.append(AIMessage(content=response))