import spacy

def load_nlp():
    try:
        return spacy.load("en_core_web_sm")
    except Exception:
        return spacy.blank("en")

nlp = load_nlp()

def extract_entities(text):
    doc = nlp(text)

    entities = {
        "PARTY": [],
        "DATE": [],
        "MONEY": [],
        "GPE": []
    }

    for ent in doc.ents:
        if ent.label_ in entities:
            entities[ent.label_].append(ent.text)

    return entities
