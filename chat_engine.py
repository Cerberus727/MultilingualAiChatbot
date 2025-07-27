import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="AIzaSyAWUEI4u-WKPFyl-z9AKW6Pmn_YsY4nOhs")
model = genai.GenerativeModel("models/gemini-2.5-pro")
chat = model.start_chat(history=[])

def get_chat_response(prompt: str) -> str:
    response = chat.send_message(prompt, stream=True)
    output = ""
    for chunk in response:
        output += chunk.text
    return output
