import os
from boltiotai import openai
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

BOT_TOKEN = os.environ.get("BOT_TOKEN", "").strip()
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN not found")

BOLT_API_KEY = os.environ.get("BOLTIOTAI_API_KEY", "").strip()
if not BOLT_API_KEY:
    raise ValueError("BOLTIOTAI_API_KEY not found")

openai.api_key = BOLT_API_KEY

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command(commands=["start", "help"]))
async def welcome(message: types.Message):
    await message.reply(
        "Hello! I am your smart bot.How can I help you?"
    )

@dp.message()
async def gpt(message: types.Message):
    try:
        response = openai.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message.text}
            ]
        )
        reply_text = response["choices"][0]["message"]["content"]
    except Exception as e:
        reply_text = f"Error: {e}"

    await message.reply(reply_text)


async def handle_update(update: dict):
    """
    This function will be called by Flask webhook
    """
    await dp.feed_webhook_update(bot, update)
