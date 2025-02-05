from fastapi import FastAPI
from scraper import fetch_prices
from database import save_price_data, get_price_history
from twilio.rest import Client
import os

app = FastAPI()

# Twilio WhatsApp Setup
TWILIO_ACCOUNT_SID = "your_twilio_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth"
TWILIO_WHATSAPP_NUMBER = "whatsapp:+14155238886"
MY_WHATSAPP_NUMBER = "whatsapp:+91XXXXXXXXXX"

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.get("/")
def home():
    return {"message": "Grocery Price Comparison API is live!"}

@app.post("/compare-prices")
def compare_prices(grocery_list: list[str], chat_id: str = None, platform: str = "whatsapp"):
    prices = fetch_prices(grocery_list)
    save_price_data(prices)
    message = format_price_message(prices)

    if platform == "whatsapp":
        client.messages.create(from_=TWILIO_WHATSAPP_NUMBER, body=message, to=MY_WHATSAPP_NUMBER)
    elif platform == "telegram":
        send_telegram_message(chat_id, message)

    return {"message": "Comparison sent!"}

def format_price_message(prices):
    msg = "🛒 *Grocery Price Comparison* 🛒\n\n"
    for item, details in prices.items():
        msg += f"✅ *{item}*: {details['price']} ({details['store']})\n"
    return msg
