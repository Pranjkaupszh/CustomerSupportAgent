import streamlit as st
from system import A2ASystem

system=A2ASystem()

st.title(" A2A Multi-Agent Customer Support 🤖")

if "chat" not in st.session_state:
    st.session_state.chat=[]

query=st.chat_input("Ask your question")

if query:

    st.session_state.chat.append(("user",query))

    answer=system.process(query)

    st.session_state.chat.append(("assistant",answer))


for role,msg in st.session_state.chat:

    st.chat_message(role).write(msg)
