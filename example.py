import os
import asyncio
from flask import Flask, request
from main import handle_update

app = Flask(__name__)

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

@app.route("/", methods=["GET"])
def home():
    return "Bot is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    update = request.get_json(force=True)

    loop.run_until_complete(handle_update(update))

    return "ok"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
