import os
import threading
import asyncio
import time
import requests
from flask import Flask
from main import run_bot

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

def start_bot():
    asyncio.run(run_bot())

def keep_alive():
    while True:
        try:
            requests.get("http://127.0.0.1:10000/")
            print(">>> Ping sent")
        except Exception as e:
            print(">>> Ping failed:", e)
        time.sleep(600)  # 10 minutes = 600 seconds

if __name__ == "__main__":
    print(">>> Flask started")

    threading.Thread(
        target=start_bot,
        daemon=True
    ).start()

    threading.Thread(
        target=keep_alive,
        daemon=True
    ).start()

    app.run(host="0.0.0.0", port=10000)
