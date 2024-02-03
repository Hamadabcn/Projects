import PyPDF2, os
from pathlib import Path

pdfFiles = []
for filename in os.listdir(Path.home() / Path("OneDrive", "Escritorio", 'article')):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)

pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

for filename in pdfFiles:
    pdfFileObj = open(Path.home() / Path("OneDrive", "Escritorio", 'article', filename), 'rb')  # read binary
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

pdfOutPut = open(Path.home() / Path("OneDrive", "Escritorio", 'article', 'article.pdf'), 'wb')  # write binary
pdfWriter.write(pdfOutPut)
pdfOutPut.close()
