import os
from flask import Flask
import threading
import asyncio
from main import run_bot

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

if __name__ == "__main__":
    print(">>> Flask started")

    threading.Thread(
        target=lambda: asyncio.run(run_bot()),
        daemon=True
    ).start()

    app.run(host="0.0.0.0", port=10000)
