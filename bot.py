import os
from aiogram import Bot, Dispatcher, executor, types

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("🤖 Бот запущен и работает!")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(f"Ты написал: {message.text}")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
