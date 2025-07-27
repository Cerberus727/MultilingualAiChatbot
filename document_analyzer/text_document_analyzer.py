# document_analyzer/test_document_analyzer.py

from document_analyzer.analyzer import analyze_document

file_path = "sample.pdf"  # or "sample.docx"
print("📄 Analyzing:", file_path)
result = analyze_document(file_path)
print("📝 Summary:\n", result)
