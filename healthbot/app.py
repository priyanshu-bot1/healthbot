from flask import Flask, request, jsonify, render_template
import requests
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")
API_URL = "https://api.groq.com/openai/v1/chat/completions"



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_question = request.json.get("question", "")

    

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "moonshotai/kimi-k2-instruct-0905",  # Any supported Groq model
        "messages": [
            {"role": "system", 
                "content": "You are a student-friendly and kids-friendly health bot."
                " Always answer in clear, short bullet points only. Avoid long paragraphs."
                " Make your responses easy to scan and direct. Answer must contains emojis too."
                " Answer only Health related questions. When some says Hii, Hello and whatever the starting greet him well. "
                "be frankly. don't forget about diseases if he doesn't mention other diseases name take it like he is talking about last diseases user mention"
                },
            {"role": "user", "content": user_question}
        ]
    }

    response = requests.post(API_URL, headers=headers, json=data)
    response_json = response.json()
    print("API Response:", response_json)

    if "choices" in response_json:
        answer = response_json["choices"][0]["message"]["content"]
    else:
        answer = "API Error: " + str(response_json)

    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
