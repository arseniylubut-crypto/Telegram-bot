import logging
import os
import asyncio
import aiohttp
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

logging.basicConfig(level=logging.INFO)
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

async def get_ai_response(prompt: str) -> str:
 api_key = os.getenv("OPENROUTER_API_KEY")
 url = "https://openrouter.ai/api/v1/chat/completions"
 headers = {
 "Authorization": f"Bearer {api_key}",
 "Content-Type": "application/json"
 }
 payload = {
 "model": "meta-llama/llama-3.3-70b-instruct",
 "messages": [{"role": "user", "content": prompt}]
 }

 async with aiohttp.ClientSession() as session:
 async with session.post(url, headers=headers, json=payload) as response:
 if response.status == 200:
 data = await response.json()
 return data['choices'][0]['message']['content']
 return "Ошибка при обращении к ИИ."

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
 await message.answer("Привет! Я готов к работе.")

@dp.message()
async def handle_message(message: types.Message):
 if message.text:
 response = await get_ai_response(message.text)
 await message.answer(response)

async def main():
 await dp.start_polling(bot)

if __name__ == "__main__":
 asyncio.run(main())
