import os
from llm import get_llm
from retrieval import get_vector_store, get_standard_retriever, get_multiquery_retriever, get_hyde_retriever

def test_retrievers():
    try:
        print("Loading LLM...")
        llm = get_llm(temperature=0.0)
        
        print("Loading Vector Store...")
        vector_store = get_vector_store()
    except Exception as e:
        print(f"Error during initialization: {e}")
        print("Make sure you have an OPENAI_API_KEY set and the vector database is initialized via ingest.py.")
        return

    query = "İş sözleşmesinin feshi durumunda ihbar tazminatı nasıl hesaplanır?"
    print(f"\n--- Testing Query: {query} ---")

    # 1. Standard Retriever
    print("\n[1] Standard Retriever Results:")
    standard_retriever = get_standard_retriever(vector_store, k=2)
    standard_docs = standard_retriever.invoke(query)
    for i, doc in enumerate(standard_docs):
        print(f"Doc {i+1}: {doc.page_content[:150]}...")

    # 2. Multi-Query Retriever
    print("\n[2] Multi-Query Retriever Results:")
    mq_retriever = get_multiquery_retriever(vector_store, llm, k=2)
    mq_docs = mq_retriever.invoke(query)
    for i, doc in enumerate(mq_docs):
        print(f"Doc {i+1}: {doc.page_content[:150]}...")

    # 3. HyDE Retriever
    print("\n[3] HyDE Retriever Results:")
    hyde_retriever = get_hyde_retriever(vector_store, llm, k=2)
    hyde_docs = hyde_retriever(query)
    for i, doc in enumerate(hyde_docs):
        print(f"Doc {i+1}: {doc.page_content[:150]}...")

if __name__ == "__main__":
    test_retrievers()
