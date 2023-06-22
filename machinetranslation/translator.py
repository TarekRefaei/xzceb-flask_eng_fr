"""python3"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """Function printing python version."""
    memory_translator = MyMemoryTranslator(source="english",target="french")
    french_text = memory_translator.translate(english_text.strip())
    return french_text

def french_to_english(french_text):
    """Function printing python version."""
    memory_translator = MyMemoryTranslator(source="french",target="english")
    english_text = memory_translator.translate(french_text.strip())
    return english_text
