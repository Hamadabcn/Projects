from docx2pdf import convert
from pathlib import Path

# converting a docx file to pdf
docx_file = Path.home() / Path("OneDrive", "Escritorio", "word files", "academy_1.docx")

# changing the name of the pdf file and saving it on the desktop
pdf_file = Path.home() / Path("OneDrive", "Escritorio", "academy_1_converted.pdf")

# what if we want to convert several files from docx to pdf
multi_files = Path.home() / Path("OneDrive", "Escritorio", "word files/")  # / means all the files

# convert(docx_file, pdf_file)
convert(multi_files)
