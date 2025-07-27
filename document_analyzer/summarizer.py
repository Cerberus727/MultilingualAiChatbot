# document_analyzer/summarizer.py

import google.generativeai as genai

genai.configure(api_key="AIzaSyAWUEI4u-WKPFyl-z9AKW6Pmn_YsY4nOhs")  # Replace securely using .env later

model = genai.GenerativeModel("models/gemini-2.5-pro")

def summarize_text(text, max_tokens=500):
    try:
        prompt = f"Summarize the following document:\n\n{text[:4000]}"
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌ Error summarizing: {e}"

