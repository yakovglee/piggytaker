from utils.bot import dp
from aiogram.types import Message

import utils.markups as nav

@dp.message_handler(commands=['start'])
async def send_welcome(message: Message):
    """
    Обработчик команды start
    """
    kb = nav.get_infoMenu()

    await message.answer(f"Привет, {message.from_user.first_name}\n\n\n{help_msg()}", reply_markup=kb)

@dp.message_handler(commands=['help'])
async def send_welcome(message: Message):

    await message.answer(f"{help_msg()}")

@dp.message_handler()
async def send_welcome(message: Message):

    kb = nav.get_infoMenu()

    await message.answer(f"Тебе может помочь следующее\n\n\n{help_msg()}", reply_markup=kb)


def help_msg():
    msg_add = f"Чтобы добавить запись введи команду \\add\nИли нажми на кнопку Добавить \N{memo}"
    msg_look = f"Чтобы посмотреть расходы введи команду \\look\nИли нажми на кнопку Посмотреть \N{open book}"

    msg = f"{msg_add}\n\n{msg_look}"

    return msg