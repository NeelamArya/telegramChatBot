import os
from boltiotai import openai
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Update

BOT_TOKEN = os.getenv("BOT_TOKEN")
BOLTIOTAI_API_KEY = os.getenv("BOLTIOTAI_API_KEY")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN not found")

if not BOLTIOTAI_API_KEY:
    raise ValueError("BOLTIOTAI_API_KEY not found")

openai.api_key = BOLTIOTAI_API_KEY

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command(commands=["start", "help"]))
async def welcome(message: types.Message):
    await message.reply("Hello! I am your smart bot 🤖\nHow can I help you?")

@dp.message()
async def gpt(message: types.Message):
    try:
        response = openai.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": message.text}]
        )

        reply = response["choices"][0]["message"]["content"].strip()
        await message.reply(reply)

    except Exception as e:
        await message.reply(f"⚠️ Error: {e}")


async def process_update(update: Update):
    await dp.feed_update(bot, update)
