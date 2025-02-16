#langchain for bot creation 
from langchain import ChatOpenAI
from langchain_core.prompts import ChatMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import ollama

# for web interface dev

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

#setting up the enviroment 
os.environ["LANGCHAIN_TRACKING_V2"] = "TRUE"
os.environ["LANGCHAIN_API_KEY"]= os.getenv("LANGCHAIN_API_KEY")

#prompt Template 

prompt = ChatMessagePromptTemplate.from_message
(
    [
        ("system","You are a helpful bot , Please respond to the quries")
        ("user","Question:{question}")
    ]
)
 
#streamlit framework

st.title("Vanga Pesalam..! with ''langchain'' using 'Ollama'")
input_text = st.text_input("Search panunga: ")

#Feching - Ollama LLM
llm = ollama(model = "llama3.2")
output_praser = StrOutputParser
chain = prompt|llm|output_praser

if input_text :
    st.write(chain.invoke({question:input_text}))
