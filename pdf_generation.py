#file that generate pdf of notes and summary 

from fpdf import FPDF

#super easy way to generate the pdf
def pdf_generation(result):

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=12)# using too set font size 
    pdf.multi_cell(0,10,result)# i am using multi cell instead cell to seprate each line and look clean
    pdf.output("notes.pdf")


