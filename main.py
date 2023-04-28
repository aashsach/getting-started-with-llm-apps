import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

llm = ChatOpenAI()

st.title('Chat with LLM')

question = st.text_area(label="Ask something")

button = st.button("Get Answer")

if button:
  with st.spinner("thinking..."):
    question = HumanMessage(content=question)
    answer = llm([question])
  st.write(answer.content)
