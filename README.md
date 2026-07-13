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
GEMINI_API=your_gemini_api_key
HF_API=your_huggingface_api_key
```

---

## 🚀 Run the Application

```bash
python rag.py
```

Example:

```text
Ask question...
tell me about rag.

Answer:
========== RETRIEVED DOCS ==========
Retrieval-Augmented Generation (RAG) is a technique used to optimize the output of an LLM by referencing an authoritative knowledge base outside of its original training data.

In the context of LLM architecture, RAG functions as a bridge between the model's pre-trained weights and external, private, or real-time data. The process typically follows these steps:

1.  **Retrieval:** When a prompt is submitted, the syst...
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
