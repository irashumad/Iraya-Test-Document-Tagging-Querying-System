from transformers import pipeline
import streamlit as st

@st.cache_resource
def load_classifier():
    return pipeline(
        "zero-shot-classification",
        model="valhalla/distilbart-mnli-12-1"
    )

def generate_tags(text: str) -> str:
    text = text[:2000]

    candidate_labels = [
        "geoscience",
        "oil and gas",
        "data mining",
        "machine learning",
        "artificial intelligence",
        "document analysis",
        "OCR",
        "parameter extraction",
        "geological data",
        "reservoir properties",
        "formation pressure",
        "formation temperature",
        "fracture pressure",
        "drilling rate",
        "total organic carbon",
        "lithology",
        "technical documents",
        "big data",
        "basin analysis",
        "subsurface data"
    ]

    classifier = load_classifier()
    result = classifier(text, candidate_labels)
    top_tags = result["labels"][:10]

    return ", ".join(top_tags)