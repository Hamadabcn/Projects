from PyPDF2 import PdfFileWriter as w
from pathlib import Path
import PyPDF2

pdf = w()
file = open(Path.home() / Path("OneDrive", "Escritorio", 'pdf_file.pdf'), 'wb')  # 'wb' write binary

# this is to create how many pages the pdf file contains (using a for loop)
for i in range(5):
    pdf.addBlankPage(219, 297)   # A4 size paper dimension
pdf.write(file)

# copy from a file to a file we need file.writer and file.reader
pdfFile = open(Path.home() / Path("OneDrive", "Escritorio", 'pdf_test.pdf'), 'rb')  # 'rb' read binary
pdfReader = PyPDF2.PdfFileReader(pdfFile)

# now using a for loop we are going to say which and how many pages you want to copy
for pageNum in range(pdfReader.numPages):  # this specifies the number of pages to copy
    pageObj = pdfReader.getPage(pageNum)
    pdf.addPage(pageObj)

pdf.write(file)

file.close()  # we should always remember to close the files
