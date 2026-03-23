from reader import extract_text_from_pdf
from ai_engine import generate_output

def file_path():#calling the func so we can use the path and can generate the text in reader file
     
    pdf_path = input("Enter the path of the pdf file here to procced further : ")
    return pdf_path




print("What do you want?")
print("1.A short 1 page summary")
print("2.A page with notes having bullet points")
choice = input("Choose 1 or 2 : ")


path = file_path()
text = extract_text_from_pdf(path)

result = generate_output(choice,text)


print("TEXT:", text)
print("CHOICE:", choice)
result = generate_output(text, choice)
print("RESULT:", result)
