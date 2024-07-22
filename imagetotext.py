import pytesseract
import os
from PIL import Image
import pandas as pd
import openpyxl

pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def convert_excel():
    img=Image.open("kuppuraj anna project.png")
    text=pytesseract.image_to_string(img)
    lines=text.split("\n")
    df=pd.DataFrame(lines,columns=["Text"])
    df.to_excel("Professor_details.xlsx",index=False)
    print("Text extracted sucessfull")

convert_excel()













#pdf file to excel file................
'''
import pandas as pd
import tabula

def convert_pdf_to_excel(pdf_file, excel_file):
    # Extract tables from PDF using tabula-py
    tables = tabula.read_pdf(pdf_file, pages='all', multiple_tables=True)
    
    # Concatenate all tables into a single DataFrame
    df = pd.concat(tables)
    
    # Save DataFrame to Excel
    df.to_excel(excel_file, index=False)
    print("PDF converted to Excel successfully.")

# Example usage:
pdf_file = "input.pdf"
excel_file = "output.xlsx"
convert_pdf_to_excel(pdf_file, excel_file)
'''

#html file to pdf file.................