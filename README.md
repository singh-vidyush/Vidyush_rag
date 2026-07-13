# 🚀 RAG Chatbot with Gemini, LangChain & ChromaDB

A Retrieval-Augmented Generation (RAG) chatbot that answers questions from your own documents using **Google Gemini**, **LangChain**, **ChromaDB**, and **Hugging Face Embeddings**.

---

## ✨ Features

- 📄 Supports PDF, DOCX, and TXT files
- 🔍 Semantic search using ChromaDB
- 🤖 Powered by Google Gemini
- 🧠 Hugging Face embeddings
- 📚 Retrieval-Augmented Generation (RAG)
- ⚡ Fast and context-aware responses

---

## 🏗️ Architecture

```text
Documents
    │
    ▼
Document Loaders
    │
    ▼
Text Chunking
    │
    ▼
Embeddings Model
    │
    ▼
ChromaDB Vector Store
    │
    ▼
Retriever
    │
    ▼
Gemini LLM
    │
    ▼
Answer Generation
```

## 🛠️ Tech Stack

- Python
- LangChain
- ChromaDB
- Hugging Face Embeddings
- Google Gemini API

---

## 📂 Supported File Types

- PDF
- DOCX
- TXT

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/singh-vidyush/Vidyush_rag.git
cd Vidyush_rag
```

Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GEMINI_API=your_api_key
```

---

## 🚀 Run the Application

```bash
python rag.py
```

Example:

```text
Ask question...
What is GPT-3.5?

Answer:
GPT-3.5 is a large language model developed by OpenAI...
```

---

## 📈 Future Enhancements

- Streamlit UI
- Chat history memory
- Source citations
- Hybrid search
- Docker deployment

---

## 👨‍💻 Author

**Vidyush Singh**

AI & Machine Learning Enthusiast

GitHub: https://github.com/singh-vidyush

---

⭐ Star this repository if you found it useful!
