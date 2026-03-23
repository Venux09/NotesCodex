import pdfplumber#a library that converts pdf into text
from main import input


def extract_text_from_pdf(input):
    with pdfplumber.open(input) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
            return text


