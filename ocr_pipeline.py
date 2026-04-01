
from pdf2image import convert_from_path
import pytesseract
import re
import os

def clean_text(text: str) -> str:
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def extract_text_from_pdf(file_path):
    text = ""

    try:
        if os.name == "nt":
            pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
            images = convert_from_path(
                file_path,
                poppler_path=r"C:\poppler\Library\bin"
            )
        else:
            images = convert_from_path(file_path)

        for img in images:
            page_text = pytesseract.image_to_string(img)
            text += page_text + "\n"

        text = clean_text(text)

    except Exception as e:
        print(f"Error during OCR extraction: {e}")

    return text