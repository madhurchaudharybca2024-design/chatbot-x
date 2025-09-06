from chatbot_x.nlp_utils import detect_intent, extract_entities, analyze_sentiment
from chatbot_x.customer_support_data import FAQ_DATA

class ChatEngine:
    def __init__(self):
        self.context = {}

    def get_response(self, message):
        intent = detect_intent(message)
        entities = extract_entities(message)
        sentiment = analyze_sentiment(message)
        if intent == "greeting":
            return "Hello! How can I assist you today?"
        elif intent == "order_status":
            if entities["order_number"]:
                return f"Your order #{entities['order_number']} is being processed. (Sentiment: {sentiment})"
            return "Can you provide your order number?"
        elif intent == "refund":
            return "I'm here to help with refunds. Can you provide your order number?"
        elif intent == "goodbye":
            return "Thank you for contacting support. Have a great day!"
        else:
            for q, a in FAQ_DATA.items():
                if q in message.lower():
                    return a
            return f"I'm sorry, I didn't understand that. Could you please rephrase? (Sentiment: {sentiment})"