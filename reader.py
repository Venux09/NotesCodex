import pdfplumber#a library that converts pdf into text



def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            extracted = page.extract_text()
            if extracted:# added becuase it will only add something when there is not none
                text += extracted

    return text


