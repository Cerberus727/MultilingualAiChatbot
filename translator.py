from googletrans import Translator

translator = Translator()

def detect_language(text):
    result = translator.detect(text)
    return result.lang

def translate_to_english(text):
    result = translator.translate(text, dest='en')
    return result.text

def translate_from_english(text, target_lang):
    result = translator.translate(text, dest=target_lang)
    return result.text
