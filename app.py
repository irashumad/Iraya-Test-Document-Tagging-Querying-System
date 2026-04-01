import streamlit as st
from db import create_table, fetch_latest_document, insert_document, update_tags_by_id
from ocr_pipeline import extract_text_from_pdf
from tagger import generate_tags
from qa_engine import answer_question

st.set_page_config(page_title="Document Tagging & Querying System", layout="wide")

st.title("📄 Intelligent Document Tagging & Querying System")
st.markdown("---")

create_table()

uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file is not None:
    st.write(f"Selected file: {uploaded_file.name}")

    if st.button("Process PDF"):
        try:
            with open("temp.pdf", "wb") as f:
                f.write(uploaded_file.read())

            with st.spinner("Extracting text from PDF..."):
                text = extract_text_from_pdf("temp.pdf")

            if not text:
                st.error("No text could be extracted from the uploaded PDF.")
            else:
                doc_id = insert_document(uploaded_file.name, text)

                with st.spinner("Generating tags..."):
                    tags = generate_tags(text)

                update_tags_by_id(doc_id, tags)

                st.success("File processed, tagged, and saved to database.")
                st.rerun()

        except Exception as e:
            st.error(f"Upload failed: {e}")

document = fetch_latest_document()

if document:
    doc_id, filename, extracted_text, generated_tags, created_at = document

    st.subheader("📌 Document Record from SQL")
    st.write(f"**ID:** {doc_id}")
    st.write(f"**Filename:** {filename}")
    st.write(f"**Created At:** {created_at}")

    st.markdown("### 🏷 Generated Tags")
    st.success(generated_tags if generated_tags else "No tags generated yet.")

    st.markdown("### 📄 Extracted Text")
    st.text_area("OCR Text", extracted_text, height=300)

    st.subheader("Ask a Question")
    user_query = st.text_input("Enter a question about the document:")

    if st.button("Search / Query"):
        if user_query.strip():
            try:
                with st.spinner("Generating answer using HuggingFace model..."):
                    answer = answer_question(user_query, extracted_text)

                st.markdown("### 🔍 Answer")
                st.caption("Answer generated from SQL-stored document text using HuggingFace")
                st.info(answer)
            except Exception as e:
                st.error(f"Question answering failed: {e}")
        else:
            st.warning("Please enter a question.")
else:
    st.warning("No document found in the database. Please upload and process a PDF first.")