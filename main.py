from reader import extract_text_from_pdf 

def input():#calling the func so we can use the path and can generate the text in reader file
     
    pdf_path = input("Enter the path of the pdf file here to procced further : ")
    return pdf_path

text = (extract_text_from_pdf())

print("What do you want?")
print("1.A short 1 page summary")
print("2.A page with notes having bullet points")
choice = input("Choose 1 or 2 : ")
