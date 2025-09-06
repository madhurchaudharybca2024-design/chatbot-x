# Initialize the ChatBot-X project

# Import necessary libraries
from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

# Import routes
from chatbot_x.routes import main_routes

# Register routes
app.register_blueprint(main_routes)

if __name__ == '__main__':
    app.run(debug=True)