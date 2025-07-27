import os
import fitz
import docx
def extract_text_from_pdf(file_path):
    text=""
    try:
        with fitz.open(file_path)as doc:
            for page in doc:
                text+=page.get_text()
    except Exception as e:
        return f"Error reading PDF: {e}"
    return text.strip()
def extract_text_from_docx(file_path):
    try:
        doc=docx.Document(file_path)
        return "\n".join([para.text for para in
                          doc.paragraphs])
    except Exception as e:
        return f"Error reading  DOCX: {e}"
def extract_text(file_path):
    ext=os.path.splitext(file_path)[1].lower()
    if ext==".pdf":
        return extract_text_from_pdf(file_path)
    elif ext==".docx":
        return extract_text_from_docx(file_path)
    else:
        return "Unsupported file type...only PDFS and DOCX allowed"

