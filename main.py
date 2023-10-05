import pdfplumber as pp

with pp.open("pdf-prueba.pdf") as book:
    for page_no, page in enumerate(book.pages, start=1):
        print(f"{page_no = }")
        data = page.extract_text()
        print(data.strip())
        print("-" * 100)