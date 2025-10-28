from flask import Flask, request, render_template_string, jsonify
import joblib
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

log = []

model_path = os.path.join(os.path.dirname(__file__), "ML model", "spam_model.pkl")
model = joblib.load(model_path)

GROUPME_BOT_ID = os.getenv("GROUPME_BOT_ID")

# -------------------------
# ROUTE: Home dashboard
# -------------------------
@app.route('/')
def home():
    return render_template_string("""
        <h2>Spam Detection Dashboard</h2>
        <div id="log">
            {% for item in log %}
                <p><strong>Message:</strong> {{ item.message }}<br>
                   <strong>Prediction:</strong> {{ item.result }}</p>
                <hr>
            {% else %}
                <p>No messages yet.</p>
            {% endfor %}
        </div>

        <script>
        // Automatically refresh the log every 5 seconds
        setInterval(() => {
            fetch('/log')
                .then(response => response.json())
                .then(data => {
                    const logDiv = document.getElementById('log');
                    logDiv.innerHTML = '';
                    if (data.length === 0) {
                        logDiv.innerHTML = '<p>No messages yet.</p>';
                    } else {
                        data.reverse().forEach(item => {
                            const p = document.createElement('p');
                            p.innerHTML = `<strong>Message:</strong> ${item.message}<br><strong>Prediction:</strong> ${item.result}`;
                            logDiv.appendChild(p);
                            logDiv.appendChild(document.createElement('hr'));
                        });
                    }
                });
        }, 5000);
        </script>
    """, log=log[::-1])

# -------------------------
# ROUTE: Log API (for auto-refresh)
# -------------------------
@app.route('/log')
def get_log():
    return jsonify(log)


# -------------------------
# ROUTE: GroupMe webhook
# -------------------------
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