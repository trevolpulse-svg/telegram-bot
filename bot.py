import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="✈️ Найти тур")],
        [KeyboardButton(text="🏨 Найти отель")]
    ],
    resize_keyboard=True
)

@dp.message(F.text == "/start")
async def start(message: Message):
    await message.answer(
        "Привет 👋\nЯ помогу найти дешёвые туры 🔥",
        reply_markup=start_kb
    )

@dp.message(F.text == "✈️ Найти тур")
async def tour(message: Message):
    await message.answer("Вот лучшие туры 👇\nhttps://level.tpx.lv/shWiTpL2")

@dp.message(F.text == "🏨 Найти отель")
async def hotel(message: Message):
    await message.answer("Вот отели 👇\nhttps://travel.yandex.ru")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
