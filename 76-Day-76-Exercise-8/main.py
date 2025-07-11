# Write a program to manipulate pdf files using pyPDF. Your programs should be able to merge multiple pdf files into a single pdf. You are welcome to add more functionalities
# pypdf is a free and open-source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files. It can also add custom data, viewing options, and passwords to PDF files. pypdf can retrieve text and metadata from PDFs as well.
import os
from pypdf import PdfWriter
print(os.getcwd())
cur=os.getcwd()
cur=cur+"/76-Day-76-Exercise-8"
os.chdir(cur)
# os.path.join(cur,"76-Day-76-Exercise-8")
# print(cur)
print(os.getcwd())
merger = PdfWriter()

for pdf in ["Program_1.pdf", "Program_2.pdf"]:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()