from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

DB_DIR = "chroma_db"

def create_vectorstore(chunks):
    documents = [Document(page_content=chunk) for chunk in chunks]

    vectorstore = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=DB_DIR
    )

    return vectorstore


def search_vectorstore(query):
    vectorstore = Chroma(
        persist_directory=DB_DIR,
        embedding_function=embeddings
    )

    return vectorstore.similarity_search(query, k=3)