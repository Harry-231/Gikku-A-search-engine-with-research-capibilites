# 🌐 Gikku Chat Search Engine

**Gikku** is a sleek and intelligent AI-powered chat-based search engine. Built using LangChain, Streamlit, and Groq's blazing-fast LLaMA-3 model, Gikku can search across Wikipedia, Arxiv, and the web in real time — providing accurate and contextual responses in a beautifully designed interface.

Checkout the app at : https://gikku-a-search-engine-with-research-capibilites-lvudxzloax9xd3.streamlit.app/

![Gikku Screenshot](https://github.com/Harry-231/Gikku-A-search-engine-with-research-capibilites/blob/main/Screenshot%202025-06-17%20191246.png) <!-- Optional: Include a screen recording or UI snapshot -->

---

## 🚀 Features

- 🔎 Natural language-based web search
- 📚 Accesses Wikipedia and Arxiv with LLM-backed summarization
- 🤖 Powered by Groq’s `Llama3-8b-8192` via LangChain’s agent framework
- 💬 Conversational memory using `st.session_state`
- 🌈 Beautiful, real-time UI powered by Streamlit

---

## 🧠 Tech Stack

| Layer        | Technology                         |
|--------------|-------------------------------------|
| 💬 Language Model | [Groq LLaMA 3 (8b, 8192)]           |
| 🧱 Framework     | [LangChain](https://www.langchain.com/) |
| 🎨 UI           | [Streamlit](https://streamlit.io/)        |
| 🔌 Tools        | Wikipedia, Arxiv, Web Search APIs |

---

## 🧰 Frameworks & Libraries

- **LangChain Agents & Tools** – Orchestrates tool-based interactions
- **StreamlitCallbackHandler** – Streams intermediate steps live
- **Groq ChatGroq API** – Ultra-fast, cost-effective LLM serving
- **Session State** – Maintains conversation history per session

---

## ⚙️ Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/gikku-chat-search.git
cd gikku-chat-search
```

### 2. Create a Virtual Environment
```bash
conda create -n gikku-env python=3.10
conda activate gikku-env
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Add Your API Key
- Get your API key from [Groq Console](https://console.groq.com/)
- Paste it into the sidebar input when you run the app

### 5. Run the App
```bash
streamlit run app.py
```

---

## 💡 Example Query Prompts
- *"Who is Alan Turing?"
- *"Summarize recent research on quantum computing from Arxiv"
- *"Search for the history of the Eiffel Tower"

---

## 📂 Project Structure
```bash
├── app.py               # Main Streamlit app
├── tools.py             # LangChain tool definitions
├── assets/              # Images, GIFs, or media
├── README.md            # This file
└── requirements.txt     # Python dependencies
```

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change. 

---

## 🛡 License
This project is licensed under the [MIT License](LICENSE).

---

## 🌟 Acknowledgments
- Inspired by OpenAI’s ChatGPT with browsing
- Built with ❤️ using LangChain and Streamlit

---

> _"Hi, I’m Gikku — your AI assistant who can search the web just like ChatGPT with browsing."_ 🧠💬
