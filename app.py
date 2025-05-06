from flask import Flask, request, render_template_string
import joblib
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
log = []

@app.route('/')
def home():
    return render_template_string("""
        <h2> Spam Detection Dashboard</h2>
        {% for item in log %}
            <p><strong>Message:</strong> {{ item.message }}<br>
               <strong>Prediction:</strong> {{ item.result }}</p>
            <hr>
        {% else %}
            <p>No messages yet.</p>
        {% endfor %}
    """, log=log[::-1])

# build a solid relative path wherever this script is run
model_path = os.path.join(os.path.dirname(__file__), "ML model", "spam_model.pkl")
model = joblib.load(model_path)

@app.route('/groupme', methods=['POST'])
def groupme_webhook():
    try:
        data = request.get_json()
        message = data.get("text", "")
        if message:
            prediction = model.predict([message])[0]
            result = "Spam" if prediction == 1 else "Ham"
            if prediction == 1:
                print(f"Spam detected: {message}")
            else:
                print(f"Not a spam: {message}")
            log.append({"message": message, "result": result})
        return "OK", 200
    except Exception as e:  
        print(f"Error: {e}")
        return "Internal Server Error", 500

if __name__ == "__main__":
    app.run()