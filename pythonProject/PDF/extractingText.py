import PyPDF2
from pathlib import Path

pdfFileObj = open(Path.home() / Path("OneDrive", "Escritorio", 'pdf_test.pdf'), 'rb')  # 'rb' read binary
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# to get how many pages the document has
print(pdfReader.numPages)  # .numPages will get the total number of pages the document has

# know what if we want to read the first page
pageObj = pdfReader.getPage(1)  # this chooses which page to read (index 0)
print(pageObj.extractText())  # .extractText to make it easier to read

pdfFileObj.close()  # good practice to close the files
