from langchain_google_genai import ChatGoogleGenerativeAI
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
load_dotenv()
llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7,google_api_key=os.getenv("Google_API_KEY"))

print("hey, iam ur chatbot")

def get_bot_response(user_input):
    user_input = user_input.lower()
    if user_input in ["exit", "quit"]:
        print("Chatbot: Goodbye!")
        return "Goodbye"
    else:
        response=llm.invoke(user_input)
        return response.content.strip()
@app.route("/", methods=['GET'])
def home():
    return "Welcome to the Chatbot API! Send a POST request to /chat with your message."
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get('message', '')
    response=get_bot_response(user_input)
    print("response from bot: ", response)
    return jsonify({'response': response})

if __name__ == '__main__':
     app.run(host="0.0.0.0", port=5000, debug=True)