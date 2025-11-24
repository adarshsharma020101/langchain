from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models import ChatOllama
import streamlit as st 
import os
from dotenv import load_dotenv

load_dotenv()

## Fix 1: Correcting Environment Variable Typos
os.environ["LANGCHAIN_TRACING_V2"] = "true" # Was "LANCHAING..."
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY") # Was "KEYS"

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user's queries."),
        ("user", "Question: {question}")
    ]
)

## Streamlit framework
st.title("LangChain Demo with Ollama")
input_text = st.text_input("Search the topic you want")

## Fix 2: Using ChatOllama and correct model naming
# Ensure you have pulled this model in your terminal (e.g., 'ollama pull gemma2')
llm = ChatOllama(model="gemma2") 
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))