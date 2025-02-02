# -*- coding: utf-8 -*-
"""text_extraction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17sVHa-9kwzLDfyovcPzwe2tddBHxMBOf
"""

!pip install PyPDF2
import PyPDF2
from google.colab import files

# Upload the PDF file
uploaded = files.upload()
pdf_file = list(uploaded.keys())[0]  # Get the uploaded file name

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text() + "\n"
    return text

# Extract text from PDF and print it
pdf_text = extract_text_from_pdf(pdf_file)
print("\n🔹 Extracted Text:\n", pdf_text)