
from PyPDF2 import PdfReader
import docx


def pdf_to_text():
    pdf_file = "Application_Form_ Identity_certificate.pdf"
    text = ""
    with open(pdf_file, 'rb') as f:
        reader = PdfReader(f)
        for page_num in range(len(reader.pages)):
            page_txt = reader.pages[page_num].extract_text()
            text += page_txt
    return text

def pdf_to_docx(output_file):
    text = pdf_to_text()
    doc = docx.Document()
    doc.add_paragraph(text)
    doc.save(output_file)

output_docx_file = "first_docx.docx"

pdf_to_docx(output_docx_file)