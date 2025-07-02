import spacy

nlp = spacy.load('pt_core_news_sm')

def example_ner(text):
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]
