import logging
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = os.getenv("TOKEN")
URL_LEVEL_TRAVEL = "https://level.tpx.lv/shWiTpL2"
URL_YANDEX_TRAVEL = "https://yandex.tpx.lv/nzDf0OXJ"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

def get_main_menu():
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(
        InlineKeyboardButton(" Хочу в Таиланд", callback_data="select_dest"),
        InlineKeyboardButton(" Мечтаю о Бали", callback_data="select_dest"),
        InlineKeyboardButton(" Вьетнам/Другое", callback_data="select_dest")
    )
    return kb

def get_format_menu():
    kb = InlineKeyboardMarkup(row_width=1)
    kb.add(
        InlineKeyboardButton(" Хочу тур (Level.Travel)", callback_data="finish_lt"),
        InlineKeyboardButton(" Только отель (Яндекс)", callback_data="finish_ya")
    )
    return kb

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(
        "Привет!  Я твой личный тревел-консьерж.\n\n"
        "Помогу найти люкс по цене эконома. Куда летим?",
        reply_markup=get_main_menu()
    )

@dp.callback_query_handler(lambda c: c.data == 'select_dest')
async def process_dest(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        "Отличный выбор!  Как предпочитаешь отдыхать?",
        reply_markup=get_format_menu()
    )

@dp.callback_query_handler(lambda c: c.data.startswith('finish_'))
async def process_finish(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    
    text = (
        "Лови лучшие предложения! \n\n"
        "Бронируй сейчас, пока цена не выросла. Не забудь проверить промокоды в приложении!"
    )
    
    kb = InlineKeyboardMarkup(row_width=1)
    if callback_query.data == "finish_lt":
        kb.add(InlineKeyboardButton(" Смотреть Туры (Level.Travel)", url=URL_LEVEL_TRAVEL))
    else:
        kb.add(InlineKeyboardButton(" Найти Отель (Яндекс)", url=URL_YANDEX_TRAVEL))
        
    await bot.send_message(callback_query.from_user.id, text, reply_markup=kb)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
