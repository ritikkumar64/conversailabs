from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def store_content(text):
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_texts([text], embeddings)
    return vector_store