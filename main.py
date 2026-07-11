import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
logging.basicConfig(level=logging.INFO)
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()
@dp.message(CommandStart())
async def cmd_start(message: types.Message):
 await message.answer("Привет! Я готоч к работе")
import asyncio

async def main():
 await dp.start_polling(bot)

if __name__ == "__main__":
 asyncio.run(main())
