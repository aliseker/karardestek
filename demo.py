import sys
from retrieval import get_vector_store, get_standard_retriever

def main():
    print("Veri tabanı yükleniyor (Local HuggingFace Embeddings)...")
    try:
        vector_store = get_vector_store()
    except Exception as e:
        print("Hata: Vektör veri tabanı yüklenemedi. Lütfen önce 'python ingest.py' çalıştırdığınızdan emin olun.")
        print(f"Detay: {e}")
        return

    # Sadece standart retriever kullanıyoruz çünkü OpenAI API key'e ihtiyaç duymuyor (tamamen offline çalışır).
    retriever = get_standard_retriever(vector_store, k=2)
    
    print("\n" + "="*50)
    print("   LEGALDOC NAVIGATOR - ÇEVRİMDIŞI DEMO EKRANI")
    print("="*50)
    print("Çıkmak için 'q', 'quit' veya 'cikis' yazın.\n")

    while True:
        try:
            query = input("Hukuki sorunuzu girin: ")
        except (KeyboardInterrupt, EOFError):
            break
            
        if query.lower() in ['q', 'quit', 'exit', 'cikis']:
            print("Çıkış yapılıyor...")
            break
            
        if not query.strip():
            continue
            
        print("\n[+] Vektör veri tabanında aranıyor...\n")
        docs = retriever.invoke(query)
        
        if not docs:
            print("İlgili bir sonuç bulunamadı.")
        else:
            for i, doc in enumerate(docs):
                print(f"--- Bulunan Madde / Paragraf {i+1} ---")
                print(doc.page_content.strip())
                print("-" * 40)
        print("\n")

if __name__ == "__main__":
    main()
