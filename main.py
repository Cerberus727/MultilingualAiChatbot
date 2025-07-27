from memory_store import SQLiteMemoryStore
from chat_engine import get_chat_response
from translator import detect_language, translate_to_english, translate_from_english
from document_analyzer.analyzer import analyze_document
import os

print("📚 Multilingual Chatbot with PDF Summarizer")
user_id = input("Enter your name or ID: ").strip()
memory = SQLiteMemoryStore()
chat_history = memory.get_memory(user_id)

if chat_history:
    print("\n🔁 Previous Conversation:")
    for role, msg in chat_history:
        print(f"{'You' if role == 'user' else 'Bot'}: {msg}")
    print()

print("✅ Type your message below (type 'exit' to quit, or use /clear, /search <word>, /summarize <path>)\n")

while True:
    user_input = input("You: ").strip()
    print("Bot: Thinking...", end="", flush=True)

    if user_input.lower() in ["exit", "quit"]:
        print("Chat ended. Goodbye! Memory Saved ✅")
        break

    if user_input.lower() == "/clear":
        memory.clear_history(user_id)
        print("🗑️ Chat history cleared")
        continue

    if user_input.lower().startswith("/search "):
        keyword = user_input.split(" ", 1)[-1]
        results = memory.search(user_id, keyword)
        if results:
            print("🔍 Matches:")
            for r in results:
                print("-", r)
        else:
            print("❌ No matches found.")
        continue

    if user_input.lower().startswith("/summarize "):
        file_path = user_input.split(" ", 1)[-1]
        if not os.path.exists(file_path):
            print("❌ File not found!")
            continue
        summary = analyze_document(file_path)
        print("📄 Summary:\n", summary)
        memory.add(user_id, "user", f"/summarize {file_path}")
        memory.add(user_id, "bot", summary)
        continue

    # Default Chat Flow
    try:
        user_lang = detect_language(user_input)
        needs_translation = user_lang != "en"
        input_english = translate_to_english(user_input) if needs_translation else user_input

        memory.add(user_id, "user", user_input)

        response_text = get_chat_response(input_english)
        final_response = translate_from_english(response_text, user_lang) if needs_translation else response_text

        print("Bot:", final_response)
        memory.add(user_id, "bot", final_response)

    except Exception as e:
        print("❌ Error:", e)
