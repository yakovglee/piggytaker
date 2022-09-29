from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from utils.Sheets import GoogleTable


load_dotenv()
API_TOKEN = getenv('TOKEN')

class PiggyTaker(Bot):
    def __init__(self, token):
        super().__init__(token=token)
        self._google_table = GoogleTable()


bot = PiggyTaker(token=API_TOKEN)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)