from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

def setup_chatbot(vector_store):
    llm = OpenAI(api_key="your_openai_api_key")  # Replace with your OpenAI API key
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vector_store.as_retriever())
    return qa

def generate_response(qa, query):
    try:
        response = qa.run(query)
        return response if response else "Sorry, I couldn't find any relevant information."
    except Exception as e:
        return f"Error generating response: {e}"