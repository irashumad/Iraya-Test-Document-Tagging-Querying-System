# 📄 Intelligent Document Tagging & Querying System

##  Features
- Upload PDF documents  
- Extract text using OCR (Tesseract)  
- Store extracted data in SQL (SQLite)  
- Generate tags using HuggingFace (Zero-shot classification)  
- Query document content using AI-assisted retrieval  

---

## Tech Stack
- Python  
- Streamlit  
- HuggingFace Transformers  
- SQLite  
- Docker  

---

## ▶️ How to Run (Local)

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the application
```bash
python -m streamlit run app.py
```

### 3. Open in browser
```bash
http://localhost:8501
```

## 🐳 Docker

### 1. Build image
```bash
docker build -t irashumad/iraya-app:latest .
```

### 2. Run container
```bash
docker run -p 8503:8501 irashumad/iraya-app:latest
```

## 🗄 Database Schema

The system creates a SQL table with the following fields:

	•	id
	•	filename
	•	extracted_text
	•	generated_tags
	•	created_at

## 🤖 AI Components

Tag Generation
Uses HuggingFace zero-shot classification model to generate relevant tags

Question Answering
Uses retrieval-based approach to return relevant answers from document content

⸻

# 📌 Notes
	•	SQLite is used for simplicity (can be replaced with Azure SQL / AWS RDS)
	•	Designed to demonstrate full pipeline: OCR → Database → AI → Querying

⸻

👤 Author

Shahira
