from utils.bot import dp
from aiogram.types import Message
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext

import utils.markups as nav

@dp.message_handler(state="*", commands='reset')
@dp.message_handler(Text(equals=['reset', 'сброс'], ignore_case=True), state="*")
async def cancel_handler(message: Message, state: FSMContext):
    """
    Позволяет пользователю сбросить запись 
    """
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.finish()

    await message.reply('Запись сброшена\nВыбери действие',reply_markup=nav.get_infoMenu())