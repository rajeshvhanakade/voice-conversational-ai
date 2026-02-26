# app/tools/pdf_reader.py

import os
import PyPDF2

PDF_DIR = "data/documents"

def run(filename: str):
    path = os.path.join(PDF_DIR, filename)

    if not os.path.exists(path):
        return f"PDF '{filename}' not found."

    text = ""

    with open(path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() + "\n"

    return text[:1000]  # return first 1000 chars only