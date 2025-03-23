import os
from PyPDF2 import PdfReader
from pdf2image import convert_from_path

def pdf_to_image(pdf_file, output_dir):
    images = []
    with open(pdf_file, 'rb') as f:
        reader = PdfReader(f)
        for page_num, _ in enumerate(reader.pages):
            # convert each pdf pages to image
            img_path = os.path.join(output_dir, f"page_{page_num}.png")
            images.append(img_path)
    return images

pdf_file = "Application_Form_ Identity_certificate.pdf"
output_dir = "output_images"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

pdf_to_image(pdf_file, output_dir)