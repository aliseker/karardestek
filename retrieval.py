from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_classic.retrievers.multi_query import MultiQueryRetriever
from langchain_core.documents import Document
from langchain_core.prompts import PromptTemplate
import config
from llm import get_llm

def get_vector_store():
    """
    Loads the FAISS vector store from disk.
    """
    embeddings = HuggingFaceEmbeddings(model_name=config.EMBEDDING_MODEL_NAME)
    # allow_dangerous_deserialization=True is required for loading local FAISS indices safely in newer langchain versions
    return FAISS.load_local(config.DB_DIR, embeddings, allow_dangerous_deserialization=True)

def get_standard_retriever(vector_store, k=4):
    """
    Returns a standard similarity search retriever.
    """
    return vector_store.as_retriever(search_kwargs={"k": k})

def get_multiquery_retriever(vector_store, llm, k=4):
    """
    Returns a MultiQueryRetriever which generates multiple variations of the user query
    to improve retrieval recall.
    """
    base_retriever = vector_store.as_retriever(search_kwargs={"k": k})
    return MultiQueryRetriever.from_llm(
        retriever=base_retriever,
        llm=llm
    )

def get_hyde_retriever(vector_store, llm, k=4):
    """
    Returns a custom function that simulates a HyDE (Hypothetical Document Embeddings) retriever.
    It generates a hypothetical legal document/answer to the query, and uses that text to search
    the vector store.
    """
    prompt_template = """
    Aşağıdaki soruya yanıt veren varsayımsal (hypothetical) bir hukuki metin parçası (kanun maddesi, tüzük, yönetmelik vs.) yazın. 
    Lütfen sadece varsayımsal metni döndürün, başka bir açıklama yapmayın.

    Soru: {question}
    Varsayımsal Metin:
    """
    prompt = PromptTemplate(input_variables=["question"], template=prompt_template)
    
    def hyde_retrieve(query: str):
        # 1. Generate hypothetical document
        chain = prompt | llm
        hypothetical_doc_response = chain.invoke({"question": query})
        hypothetical_doc = hypothetical_doc_response.content
        
        # 2. Use hypothetical document to retrieve actual documents
        base_retriever = vector_store.as_retriever(search_kwargs={"k": k})
        return base_retriever.invoke(hypothetical_doc)
        
    return hyde_retrieve
