import shutil
import os

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

DB_PATH = "chroma_db"


def create_vectorstore(chunks):

    # Delete old DB so each upload starts fresh
    if os.path.exists(DB_PATH):
        shutil.rmtree(DB_PATH)

    vectorstore = Chroma.from_texts(
        texts=chunks,
        embedding=embedding,
        persist_directory=DB_PATH
    )

    print("=" * 60)
    print("✅ Vector Store Created")
    print("Stored Chunks:", vectorstore._collection.count())
    print("=" * 60)

    return vectorstore


def load_vectorstore():

    return Chroma(
        persist_directory=DB_PATH,
        embedding_function=embedding
    )


def search_resume(query, k=3):

    vectorstore = load_vectorstore()

    print("=" * 60)
    print("Database Count:", vectorstore._collection.count())

    docs = vectorstore.similarity_search(query, k=k)

    print("Retrieved:", len(docs))

    for i, doc in enumerate(docs):
        print(f"\nChunk {i+1}")
        print(doc.page_content[:300])

    print("=" * 60)

    return docs