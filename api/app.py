from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
import os
from langchain_community.chat_models import ChatOllama
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title = "Langchain Server",
    version = "1.0",
    description = "A simple API server"
)

add_routes(
    app,
    ChatOllama(),
    path = "/ollama",
)
llm = ChatOllama(model="gemma2") 

prompt =  ChatPromptTemplate.from_template("Write me a poem {topic} for a child")

add_routes(
    app,
    prompt|llm,
    path = "/poem"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)