# ChatBot-X

**ChatBot-X** is an advanced NLP-powered Python chatbot for customer support automation.

## Features

- Intent detection (greetings, order status, refunds, etc.)
- Entity extraction (order numbers)
- Sentiment analysis (using Transformers)
- FAQ fallback for common queries
- Web-based chat interface (Flask)
- Easily extensible

## Usage

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python -m chatbot_x.main
```

Open your browser at `http://localhost:5000` to use the web chat.

## Project Structure

- `chatbot_x/main.py` - Entry point & web chat
- `chatbot_x/nlp_utils.py` - NLP utilities (intent/entity/sentiment)
- `chatbot_x/chat_engine.py` - Chatbot logic
- `chatbot_x/customer_support_data.py` - Support data

## Requirements

- Python 3.7+

## Installation

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

## License

MIT