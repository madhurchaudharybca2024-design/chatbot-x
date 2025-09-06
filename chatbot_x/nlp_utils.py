import spacy
from transformers import pipeline

nlp = spacy.load("en_core_web_sm")
sentiment_analyzer = pipeline("sentiment-analysis")

def detect_intent(message):
    doc = nlp(message.lower())
    if any(token.lemma_ in ["hello", "hi", "hey"] for token in doc):
        return "greeting"
    if "order" in message and "status" in message:
        return "order_status"
    if "refund" in message:
        return "refund"
    if any(token.lemma_ in ["bye", "goodbye"] for token in doc):
        return "goodbye"
    return "unknown"

def extract_entities(message):
    doc = nlp(message)
    order_number = None
    for ent in doc.ents:
        if ent.label_ == "CARDINAL":
            order_number = ent.text
    return {"order_number": order_number}

def analyze_sentiment(message):
    result = sentiment_analyzer(message)
    return result[0]["label"]