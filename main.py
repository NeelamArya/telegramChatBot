import os
import asyncio
from boltiotai import openai
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

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
    await message.reply("Hello! I am your smart bot. How can I help you?")

@dp.message()
async def gpt(message: types.Message):
    try:
        response = openai.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": message.text}]
        )
        await message.reply(response["choices"][0]["message"]["content"].strip())
    except Exception as e:
        await message.reply(f"Error: {e}")

async def run_bot():
    print(">>> Bot polling started")
    await dp.start_polling(bot)

# 👇 THIS is the magic
if __name__ == "__main__":
    # If running on Replit → start bot directly
    if os.getenv("RENDER") != "true":
        asyncio.run(run_bot())
