import os
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import config

def run_ingestion():
    """
    Reads PDFs from the data directory, chunks the text, and stores it in a FAISS vector database.
    """
    print(f"Starting ingestion from: {config.DATA_DIR}")
    
    # 1. Load PDFs
    documents = []
    pdf_files = [f for f in os.listdir(config.DATA_DIR) if f.endswith(".pdf")]
    
    if not pdf_files:
        print("No PDF files found in the data directory. Please add some legal documents to 'data/' folder.")
        return

    for pdf_file in pdf_files:
        pdf_path = os.path.join(config.DATA_DIR, pdf_file)
        print(f"Loading {pdf_file}...")
        loader = PyMuPDFLoader(pdf_path)
        documents.extend(loader.load())

    print(f"Loaded {len(documents)} pages from {len(pdf_files)} files.")

    # 2. Split Text
    # For legal documents, overlap and separators are key to maintain context of articles.
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.CHUNK_SIZE,
        chunk_overlap=config.CHUNK_OVERLAP,
        separators=["\n\n", "\n", "Madde", "MADDE", ".", " "]
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split documents into {len(chunks)} chunks.")

    # 3. Create Embeddings
    print(f"Using embedding model: {config.EMBEDDING_MODEL_NAME}")
    embeddings = HuggingFaceEmbeddings(model_name=config.EMBEDDING_MODEL_NAME)

    # 4. Create and Save Vector Store
    print("Creating FAISS index...")
    vector_db = FAISS.from_documents(chunks, embeddings)
    
    print(f"Saving vector database to: {config.DB_DIR}")
    vector_db.save_local(config.DB_DIR)
    print("Ingestion complete!")

if __name__ == "__main__":
    run_ingestion()
