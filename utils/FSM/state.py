from aiogram.dispatcher.filters.state import State, StatesGroup

class Counter(StatesGroup):
    counter = State()

class Data(StatesGroup):
    date = State()
    categ = State()
    subcateg = State()
    price = State()

class DataPlus(StatesGroup):
    date = State()
    price = State()