from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
#creating my prompt
prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful AI bot. Your name is {jarvis}."),
        ("user", "Question:{question}")
])
#streamlit 
st.title("My GPT")
input_text = st.text_input("What is your question?")
#ollama  framework
llm = Ollama(model="gemma2:2b")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser
# gpt output
if input_text:
    st.write(chain.invoke({"jarvis": "Jarvis", "question": input_text}))
    