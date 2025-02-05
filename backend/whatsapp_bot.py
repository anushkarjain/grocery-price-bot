from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    incoming_msg = request.values.get("Body", "").lower()
    grocery_list = incoming_msg.split(",")

    response = requests.post("http://127.0.0.1:8000/compare-prices", json={"grocery_list": grocery_list})
    message = response.json()["message"]

    reply = MessagingResponse()
    reply.message(message)
    return str(reply)

if __name__ == "__main__":
    app.run(port=5000)
