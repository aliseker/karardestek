import os
from dotenv import load_dotenv

load_dotenv()

# Project Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
DB_DIR = os.path.join(BASE_DIR, "vector_db")

# Model Configurations
EMBEDDING_MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"  # Turkish support
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
LLM_MODEL_NAME = "gpt-4o-mini"

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Create directories if they don't exist
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(DB_DIR, exist_ok=True)
