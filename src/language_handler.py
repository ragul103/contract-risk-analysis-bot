from langdetect import detect

def detect_language(text):
    try:
        return detect(text)
    except:
        return "en"

def normalize_text(text):
    lang = detect_language(text)

    if lang == "hi":
        # placeholder: later use LLM for translation
        normalized_text = text  # assume English for now
    else:
        normalized_text = text

    return {
        "language": lang,
        "normalized_text": normalized_text
    }
