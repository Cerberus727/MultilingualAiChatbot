# document_analyzer/analyzer.py

from .extractor import extract_text
from .summarizer import summarize_text

def analyze_document(file_path):
    text = extract_text(file_path)
    if text.startswith("❌"):
        return text
    summary = summarize_text(text)
    return summary
