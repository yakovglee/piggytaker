from utils.bot import dp, bot
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Text

import utils.markups as nav

@dp.message_handler(Text(equals="Посмотреть \N{open book}"))
@dp.message_handler(commands='look')
async def start_to_add_record(message: Message):

    kb = nav.get_lookupMenu()
    await message.answer("Выбери день", reply_markup=kb)


@dp.callback_query_handler(Text(equals=['lookup_yest']))
async def get_data_yest(call: CallbackQuery):

    data = bot._google_table.get_data('B4', 'C4')

    await call.message.edit_text(
        f'Расходы за вчера {data[0]}\n{data[1]}'
    )


@dp.callback_query_handler(Text(equals=['lookup_now']))
async def get_data_now(call: CallbackQuery):
    data = bot._google_table.get_data('B5', 'C5')

    await call.message.edit_text(
        f'Расходы за сегодня {data[0]}\n{data[1]}'
    )


@dp.callback_query_handler(Text(equals=['lookup_monthnow']))
async def get_data_monthnow(call: CallbackQuery):
    data = bot._google_table.get_data('B3', 'C3')

    await call.message.edit_text(
        f'Расходы за текущий месяц\n{data[1]}'
    )


@dp.callback_query_handler(Text(equals=['lookup_monthyest']))
async def get_data_monthyest(call: CallbackQuery):
    data = bot._google_table.get_data('B2', 'C2')

    await call.message.edit_text(
        f'Расходы за прошлый месяц\n{data[1]}'
    )