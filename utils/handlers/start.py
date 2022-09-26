from utils.bot import dp
from aiogram.types import Message

import utils.markups as nav

@dp.message_handler(commands=['start'])
async def send_welcome(message: Message):
    """
    Обработчик команды start
    """
    kb = nav.get_infoMenu()

    await message.answer(f"Привет, {message.from_user.first_name}\nВыбери действие", reply_markup=kb)

# @dp.message_handler()
# async def show_categories(message: Message:

#         await message.answer("Не могу помочь")