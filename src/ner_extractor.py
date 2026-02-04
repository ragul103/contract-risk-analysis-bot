import spacy
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    nlp = spacy.blank("en")

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

