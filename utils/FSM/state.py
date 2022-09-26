from aiogram.dispatcher.filters.state import State, StatesGroup

class Data(StatesGroup):
    date = State()
    categ = State()
    subcateg = State()
    price = State()