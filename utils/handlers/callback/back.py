from utils.bot import dp
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram import types

import utils.markups as nav

from utils.handlers.callback.callback import Counter 


@dp.message_handler(state='*', commands='reset')
@dp.message_handler(Text(equals='reset', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    """
    Позволяет пользователю сбросить запись 
    """
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.finish()

    await message.reply('Запись сброшена\nВыбери действие',reply_markup=nav.get_infoMenu())


@dp.callback_query_handler(text='btnback', state="*")
async def back(call: types.CallbackQuery, state: FSMContext):

    async with state.proxy() as data:
        data['counter'] -= 1
    
    if data['counter'] == 0:
        await state.finish()
        await call.message.delete()

        await nav.back_to_Menu(call, "info")

        await call.answer()

    elif data['counter'] == 1:
        await state.reset_state(with_data=False)
        await nav.back_to_Menu(call, "data", "Выбери день")
    
    elif data['counter'] == 2:
        await state.reset_state(with_data=False)
        await nav.back_to_Menu(call, "main", "Выбери действие")