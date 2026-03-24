import pdfplumber#a library that converts pdf into text
import os  


def extract_text_from_pdf(pdf_path):
    if not os.path.exists(pdf_path):
        print("File not founded ! please try again ")
        return None
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            extracted = page.extract_text()
            if extracted:# added becuase it will only add something when there is not none
                text += extracted

    return text


