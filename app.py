import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun , WikipediaQueryRun , DuckDuckGoSearchRun
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler
import os 
from dotenv import load_dotenv

api_wrapper_wiki = WikipediaAPIWrapper(top_k_results = 1 , doc_content_chars_max = 250) 
wiki = WikipediaQueryRun(api_wrapper = api_wrapper_wiki)

api_wrapper_arxiv = ArxivAPIWrapper(top_k_results = 5 , doc_content_chars_max = 250)
arxiv = ArxivQueryRun(api_wrapper = api_wrapper_arxiv)

search = DuckDuckGoSearchRun(name= "search")

st.set_page_config(page_title="Gikku Chat Search Engine", page_icon="🔍")

st.title("🔎 Chat Search Engine — Gikku")

# ───────────────────────────────── Sidebar ────────────────────────────────────
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your Groq API key:", type="password")

if st.sidebar.button("🗑️ Clear chat"):
    st.session_state.pop("messages", None)
    st.experimental_rerun()

# ───────────────────────────── Session‑state history ──────────────────────────
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {
            "role": "assistant",
            "content": "Hi, I’m **Gikku** — your AI assistant who can search the web just like ChatGPT with browsing."
        }
    ]

# Render chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# ──────────────────────────── Handle user prompt ─────────────────────────────
if prompt := st.chat_input("Ask me anything…"):
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    
    if not api_key:
        err = "⚠️ Please enter your Groq API key in the sidebar to continue."
        st.chat_message("assistant").write(err)
        st.session_state.messages.append({"role": "assistant", "content": err})
        st.stop()

    llm = ChatGroq(
        groq_api_key=api_key,
        model_name="Llama3-8b-8192",
        streaming=True,
    )

    tools = [wiki, arxiv, search]  

    search_agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        handle_parsing_errors=True,  
        verbose=False,
    )

    # ─────────────────────────── Agent call & streaming ───────────────────────
    with st.chat_message("assistant"):
        container = st.container()
        st_cb = StreamlitCallbackHandler(container, expand_new_thoughts=True)

        try:
            
            agent_output = search_agent.invoke({"input": prompt}, callbacks=[st_cb])
            
            reply = agent_output.get("output", agent_output)
        except Exception as exc:
            reply = f"Sorry, I ran into an error: `{exc}`"

        st.write(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})
