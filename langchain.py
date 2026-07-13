import os
from pathlib import Path
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader, TextLoader, Docx2txtLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from dotenv import load_dotenv
from google import genai



DATA_DIR = "RAG/data"
CHROMA_DIR = "chroma_db"

EMBEDDING_MODEL = HuggingFaceEmbeddings(model_name= "sentence-transformers/all-MiniLM-L6-v2")

docs = []

docs += DirectoryLoader(
    DATA_DIR,
    glob = "**/*.pdf",
    loader_cls= PyPDFLoader
).load()

docs += DirectoryLoader(
    DATA_DIR,
    glob = "**/*.docx",
    loader_cls= Docx2txtLoader
).load()

docs += DirectoryLoader(
    DATA_DIR,
    glob = "**/*.txt",
    loader_cls= TextLoader
).load()

print(f'Document length: {len(docs)}')



text_splitter = RecursiveCharacterTextSplitter(
    chunk_size= 500,
    chunk_overlap= 100
)

chunks = text_splitter.split_documents(docs)

print(f"Created chunks: {len(chunks)}")


if Path(CHROMA_DIR).exists():
    vector_db = Chroma(
        persist_directory= CHROMA_DIR,
        embedding_function= EMBEDDING_MODEL
    )

else:
    vector_db = Chroma.from_documents(
        documents= chunks,
        persist_directory= CHROMA_DIR,
        embedding= EMBEDDING_MODEL,
    )



TOP_K = 3
retriever = vector_db.as_retriever(search_kwargs= {"k": TOP_K})

load_dotenv()
gemini_api = os.getenv("GEMINI_API") 
client = genai.Client(api_key= gemini_api)

while True:
    print("Ask question...")
    question = input()
    if question.lower() in ['exit', 'quit', 'stop']:
        print('Stopped')
        break

    retrieved_docs = retriever.invoke(question)
    
    print("\n========== RETRIEVED DOCS ==========")
    for i, doc in enumerate(retrieved_docs):
        print(f"\n--- DOC {i+1} ---")
        print(doc.page_content[:500])


    context = '\n\n'.join(doc.page_content for doc in retrieved_docs)

    prompt = f"""
You are a senior AI Model Advisor chatbot.

Your ONLY area of knowledge is:
- LLMs (Large Language Models)
- SLMs (Small Language Models)
- their evolution
- architecture
- related AI/ML topics

Context:
{context}

User Question:
{question}

Answer the question using the context above.
If the context doesn't contain the answer, say so.
"""

    response = client.models.generate_content(
        model= "gemini-3.1-flash-lite",
        contents= prompt
    )

    print(response.text)