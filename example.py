import os
import asyncio
from flask import Flask, request
from aiogram.types import Update

from main import bot, process_update

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    update = Update.model_validate(request.json)
    asyncio.run(process_update(update))
    return "ok"

if __name__ == "__main__":
    print(">>> Flask started")
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )
