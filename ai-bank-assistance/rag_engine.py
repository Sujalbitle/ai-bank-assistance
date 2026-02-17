import os
from langchain_groq import ChatGroq
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain.chains import RetrievalQA
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_rag_chain():
    """
    Initializes and returns the RAG chain.
    """
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables.")

    # 1. Load the data
    loader = TextLoader("data/banking_faqs.txt")
    documents = loader.load()

    # 2. Split the text into chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(documents)

    # 3. Create embeddings and vector store
    # Using a free, local embedding model from HuggingFace
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(texts, embeddings)

    # 4. Create the retriever
    retriever = vectorstore.as_retriever()

    # 5. Initialize the Groq LLM
    llm = ChatGroq(
        temperature=0, 
        groq_api_key=api_key, 
        model_name="llama3-70b-8192"
    )

    # 6. Create the RetrievalQA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True
    )

    return qa_chain

if __name__ == "__main__":
    # Simple test
    try:
        chain = get_rag_chain()
        response = chain.invoke("What is the interest rate for savings account?")
        print(response['result'])
    except Exception as e:
        print(f"Error: {e}")
