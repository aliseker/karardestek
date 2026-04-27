# LegalDoc Navigator: Hukuk Metni Analiz Agent’ı

LegalDoc Navigator, uzun hukuk metinlerinden (mevzuat, kanun, tüzük vb.) ilgili maddeleri bulan ve özet raporlar çıkaran gelişmiş bir RAG (Retrieval-Augmented Generation) ajanıdır.

## 🚀 4 Haftalık Proje Programı

### 📅 1. Hafta: Temel Yapı ve Veri Hazırlama (Şu anki Aşama)
- [x] Proje iskeletinin ve ortamın hazırlanması.
- [x] PDF metin çıkarma modülü (PyMuPDF / fitz).
- [x] Hukuk metinlerine özel parçalama (Recursive Character Text Splitter) stratejileri.
- [x] FAISS ile yerel vektör veri tabanı kurulumu.

### 📅 2. Hafta: Gelişmiş RAG ve Sorgu İşleme
- [x] Retrieval (Geri Getirme) mekanizmasının optimize edilmesi.
- [x] OpenAI / Anthropic veya yerel LLM entegrasyonu.
- [x] Query Expansion (Sorgu Genişletme) ve HyDE (Hypothetical Document Embeddings) teknikleri.

### 📅 3. Hafta: Yeniden Sıralama (Reranking) ve LangGraph
- [ ] Cross-Encoders kullanarak sonuçların yeniden sıralanması (Reranking).
- [ ] LangGraph ile durum bilgili (Stateful) ajan akışının tasarlanması.
- [ ] Self-Correction (Hata düzeltme) döngülerinin eklenmesi.

### 📅 4. Hafta: Özetleme, Raporlama ve Arayüz
- [ ] Mevzuat maddelerini analiz eden "Summary Report Generator" modülü.
- [ ] Streamlit ile kullanıcı dostu bir arayüz geliştirilmesi.
- [ ] Dokümantasyonun tamamlanması ve final testleri.

## 🛠️ Kullanılan Teknolojiler
- **LangChain & LangGraph**: Ajan mantığı ve iş akış yönetimi.
- **PyMuPDF**: PDF metin işleme.
- **FAISS**: Yüksek performanslı vektör araması.
- **Sentence-Transformers**: Metin temsilleri (Embeddings).
- **Python-dotenv**: Konfigürasyon yönetimi.

## 📦 Kurulum

1. Depoyu klonlayın:
   ```bash
   git clone <repo-url>
   cd legaldoc-navigator
   ```

2. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

3. `.env` dosyasını oluşturun ve API anahtarlarınızı ekleyin.

## 📖 Kullanım (1. Hafta)

`ingest.py` dosyasını çalıştırarak `data/` klasöründeki PDF'leri vektör veritabanına ekleyebilirsiniz:
```bash
python ingest.py
```
