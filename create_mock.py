import os
from fpdf import FPDF

def create_mock_pdf():
    os.makedirs("data", exist_ok=True)
    pdf = FPDF()
    pdf.add_page()
    # Add a font that supports Turkish characters - standard fonts often struggle, but we can try just ascii for test if needed
    # Actually, fpdf2 can handle utf-8 if we use a built in font like helvetica with some limits, or just write ascii text
    # Let's write mostly ascii/latin text that looks like Turkish
    pdf.set_font("helvetica", size=12)
    
    content = """
    Is Kanunu Madde 17:
    Is sozlesmesinin feshi durumunda ihbar tazminati soyle hesaplanir:
    a) Isi 6 aydan az surmus olan isci icin bildirim suresi 2 haftadir.
    b) Isi 6 aydan 1.5 yila kadar surmus olan isci icin bildirim suresi 4 haftadir.
    c) Isi 1.5 yildan 3 yila kadar surmus olan isci icin bildirim suresi 6 haftadir.
    d) Isi 3 yildan fazla surmus isci icin bildirim suresi 8 haftadir.
    Bu surelere uyulmadigi takdirde isveren ihbar tazminati odemekle yukumludur.
    """
    
    pdf.multi_cell(0, 10, text=content)
    pdf.output("data/mock_kanun.pdf")
    print("Mock PDF created at data/mock_kanun.pdf")

if __name__ == "__main__":
    create_mock_pdf()
