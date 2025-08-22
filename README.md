# Database-Chat-Assistant
An interactive AI-powered chatbot built with Streamlit, LangChain, and MySQL that allows users to query databases using natural language instead of writing SQL manually.

## Project Demo

[DEMO](https://drive.google.com/file/d/187d3Ad1WdlLynHtuwZC6WwjjTP7K0NV2/view?usp=sharing)

## 🚀 Features

Natural Language Queries → Ask questions like “Show top 5 customers by total purchases” and get instant results.

SQL Generation → Automatically converts user queries into valid SQL queries using LLMs (Llama 3.3 via Groq API).

Database Agnostic → Works with any MySQL database (default tested on Chinook DB).

Conversational Memory → Keeps track of chat history for contextual queries.

Dual Response → SQL query is generated.

Query results are explained in simple human-readable format.

Streamlit Interface → Clean UI with chat-style interaction.

Secure Credentials → Database password handled with environment variables and URL encoding.

## 🛠️ Steps to Recreate the Project
1. Clone the Repository
```
git clone https://github.com/ratnesh134/Database-Chat-Assistant.git
cd chat-with-mysql
```
2. Create Virtual Environment
```
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```
3. Install Dependencies
```
pip install -r requirements.txt
```

requirements.txt should include:
```
streamlit
python-dotenv
langchain
langchain-community
langchain-groq
mysql-connector-python
sqlparse
```
4. Set Environment Variables
```
Create a .env file in the project root:
DB_PASSWORD=your_db_password
GROQ_API_KEY=your_groq_api_key
```
5. Run the Application
```
streamlit run app.py
```
6. Connect to Database

Open the app in browser (default: http://localhost:8501).

Enter host, port, user, password, and database name in the sidebar.

Click Connect.

## 🏗️ Architecture & Design Flow
High-Level Flow

User Input → User asks a question in natural language.

SQL Generation Chain

Prompt + Schema + Chat history → LLM generates SQL query.

Query validated against database schema.

Database Execution → SQL query executed using SQLDatabase from LangChain.

Response Chain

User query + SQL + results + schema → LLM generates explanation in plain English.

UI Layer (Streamlit)

Chat history displayed.

AI responses streamed in real-time.

Sidebar used for DB connection settings.

## Key Components

LangChain → Provides chaining, prompt templates, and SQL database utilities.

Groq LLM (Llama 3.3) → Generates SQL queries + explanations.

Streamlit → Chat interface and database connection settings.

Session State → Stores chat history & database object persistently.

## 📂 Project Structure
```
chat-with-mysql/
│── app.py                 # Main Streamlit app
│── requirements.txt       # Python dependencies
│── .env                   # Environment variables (not committed)
│── README.md              # Documentation
```
