import requests
from flask import Flask, request
from os import environ

TOKEN = "7760117749:AAEx0P5e6SQvlAcK5k1XQsjQooB_j3d-VVQ"
WEBHOOK_URL = "https://u78j9-52f7aaceeb3a.herokuapp.com/webhook"

app = Flask(__name__)

# Set the webhook
def set_webhook():
    url = f"https://api.telegram.org/bot{TOKEN}/setWebhook"
    response = requests.post(url, json={"url": WEBHOOK_URL})
    return response.json()

# Handle incoming updates
@app.route("/webhook", methods=["POST"])
def webhook():
    update = request.json
    print(update)
    if "message" in update:
        chat_id = update["message"]["chat"]["id"]
        text = update["message"]["text"]
        send_message(chat_id, f"You said: {text}")
    return "ok", 200

# Send a message
def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

if __name__ == "__main__":
    set_webhook()  # Set webhook when script runs
    app.run(host="0.0.0.0", port=int(environ.get('PORT', '80')))
