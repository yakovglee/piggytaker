from cgitb import reset
from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from Sheets import GoogleTable

from aiogram import types

load_dotenv()
API_TOKEN = getenv('TOKEN')

class PiggyTaker(Bot):
    def __init__(self, token):
        super().__init__(token=token)
        self._google_table = GoogleTable()


bot = PiggyTaker(token=API_TOKEN)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    
    await message.answer('Hi')

if __name__ == '__main__':
    from aiogram import executor
    
    executor.start_polling(dp, skip_updates=True)