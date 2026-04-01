

from ocr_pipeline import extract_text_from_pdf
from db import create_table, insert_document, fetch_document_by_filename, update_tags
from tagger import generate_tags

def main():
    file_path = "data/2022-Sustainable-data-mining.pdf"

    print("Starting OCR extraction...")

    text = extract_text_from_pdf(file_path)

    if text:
        print("OCR extraction successful!\n")

        create_table()
        insert_document(file_path, text)

        print("Saved extracted text to database!")

        db_text = fetch_document_by_filename(file_path)
        tags = generate_tags(db_text)

        update_tags(file_path, tags)

        print("Generated tags:")
        print(tags)

    else:
        print("No text extracted.")

if __name__ == "__main__":
    main()