import sys

with open("setup_result.txt", "w") as f:
    f.write(f"Python executable: {sys.executable}\n")
    f.write(f"Python version: {sys.version}\n")

    try:
        import langchain_groq
        f.write("langchain_groq: OK\n")
    except ImportError as e:
        f.write(f"langchain_groq: FAIL - {e}\n")

    try:
        from langchain_huggingface import HuggingFaceEmbeddings
        f.write("langchain_huggingface: OK\n")
    except ImportError as e:
        f.write(f"langchain_huggingface: FAIL - {e}\n")

    try:
        import faiss
        f.write("faiss: OK\n")
    except ImportError as e:
        f.write(f"faiss: FAIL - {e}\n")

    try:
        from langchain_community.document_loaders import TextLoader
        f.write("TextLoader: OK\n")
    except Exception as e:
        f.write(f"TextLoader: FAIL - {e}\n")

    try:
        from langchain_community.vectorstores import FAISS
        f.write("FAISS wrapper: OK\n")
    except Exception as e:
        f.write(f"FAISS wrapper: FAIL - {e}\n")

    try:
        from langchain_text_splitters import CharacterTextSplitter
        f.write("CharacterTextSplitter: OK\n")
    except Exception as e:
        f.write(f"CharacterTextSplitter: FAIL - {e}\n")

    try:
        from langchain.chains import RetrievalQA
        f.write("RetrievalQA: OK\n")
    except Exception as e:
        f.write(f"RetrievalQA: FAIL - {e}\n")

    try:
        from dotenv import load_dotenv
        f.write("dotenv: OK\n")
    except Exception as e:
        f.write(f"dotenv: FAIL - {e}\n")
