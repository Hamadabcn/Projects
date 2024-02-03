from pdf2docx import Converter
from pathlib import Path

# from a pdf file to a Word document
pdf_file = Path.home() / Path("OneDrive", "Escritorio", "article", "article.pdf")
docx_file = Path.home() / Path("OneDrive", "Escritorio", "article_converted.docx")

# convert pdf to docx
cv = Converter(pdf_file)
# cv.convert(docx_file)      # all pages by default
cv.convert(docx_file, start=2, end=6)  # convert from the second page and the third (it will not convert page 6)
cv.close()
