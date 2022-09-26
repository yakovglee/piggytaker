from utils.bot import bot, dp
from aiogram import types
from aiogram.dispatcher import FSMContext, filters

from aiogram.dispatcher.filters import Text

import utils.FSM.state as FSMData

from datetime import datetime

import utils.markups as nav

Data = FSMData.Data

@dp.message_handler(Text(equals="Добавить \N{memo}"))
@dp.message_handler(commands='add')
async def start_to_add_record(message: types.Message):
    await Data.date.set()

    kb = nav.get_dateMenu()
    await message.answer("Выбери день", reply_markup=kb)


@dp.callback_query_handler(text_contains="date", state=[Data.date])
async def choice_date(call: types.CallbackQuery, state: FSMContext):
    date = call.data.split("_")[1]

    if date == 'now':
        async with state.proxy() as data:
            data['date'] = datetime.today().strftime("%d.%m.%Y")

        kb = nav.get_mainMenu()
        await call.message.edit_text("Выбери категорию", reply_markup=kb)

        await Data.next()
    
    else:
        await call.message.edit_text("Напиши дату в формате dd.mm")
    
@dp.message_handler(filters.Regexp(regexp=r"(([0-3]\d)\W([0-1][0-9]))"), state=[Data.date])
async def take_data(message: types.Message, state: FSMContext):

    year = datetime.today().year

    async with state.proxy() as data:
        data['date'] = message.text + "." + str(year)
        
    kb = nav.get_mainMenu()
    await message.answer("Выбери категорию", reply_markup=kb)

    await Data.next()


@dp.callback_query_handler(text_contains="main", state=[Data.categ])
async def choice_categ(call: types.CallbackQuery, state: FSMContext):
    
    category = call.data.split("_")[1]
    await call.message.edit_text("Что конкретно")

    async with state.proxy() as data:

        if category == "food":
            data['categ'] = "Еда"
            
            kb = nav.get_inlineMenu_food()
            await call.message.edit_reply_markup(kb)
        
        elif category == "trans":
            data['categ'] = "Транспорт"

            kb = nav.get_inlineMenu_trans()
            await call.message.edit_reply_markup(kb)

        elif category == "health":
            data['categ'] = "Здоровье"

            kb = nav.get_inlineMenu_health()
            await call.message.edit_reply_markup(kb)
        
        elif category == "house":
            data['categ'] = "Дом"
        
            kb = nav.get_inlineMenu_house()
            await call.message.edit_reply_markup(kb)
        
        elif category == "other":
            data['categ'] = "Другое"
        
            kb = nav.get_inlineMenu_other()
            await call.message.edit_reply_markup(kb)
    
    await Data.next()

@dp.callback_query_handler(Text(endswith="other"), state=[Data.subcateg])
async def take_subcateg_msg(call: types.CallbackQuery):
    await call.message.edit_text("Напиши категорию")


@dp.callback_query_handler(Text(startswith=['food', 'trans', 'health', 'house', 'other']), state=[Data.subcateg])
async def choice_subcateg(call: types.CallbackQuery, state: FSMContext):
    
    allias = {
        "food_dostavka": "Доставка",
        "food_rabota": "Работа",
        "food_magazin": "Магазин",
        "food_restoran": "Ресторан",
        "food_nezozh": "Не ЗОЖ",

        "trans_soc": "Социалка",
        "trans_metro": "Метро",
        "trans_taxi": "Такси",
        "trans_bileti": "Билеты",

        "health_medusl": "Медуслуги",
        "health_pill": "Лекарства",
        "health_gigiena": "Гигиена",
        "health_sport": "Спорт",
        "health_kosmetika": "Косметика",

        "house_arenda": "Аренда",
        "house_uborka": "Уборка",
        "house_intech": "ИнТех",
        "house_uyut": "Уют",

        "other_podpiska": "Подписка",
        "other_svyaz": "Связь",
        "other_look": "Одежда",
        "other_obuch": "Учеба",
        "other_razvlech": "Развлечения",
    }

    subcateg = call.data

    async with state.proxy() as data:
        data['subcateg'] = allias.get(subcateg)

    await Data.next()
    await call.message.edit_text(f"{data['categ']}:{data['subcateg']}\nЦена")


@dp.message_handler(state=[Data.subcateg])
async def take_subcateg_msg(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['subcateg'] = message.text.capitalize()

    await Data.next()

    await message.answer(f"{data['categ']}:{data['subcateg']}\nЦена")

@dp.message_handler(lambda message: not message.text.isdigit(), state=[Data.price])
async def process_age_invalid(message: types.Message):
 
    return await message.reply("Вводи только числа (через точку)")


@dp.message_handler(lambda message: message.text.isdigit(), state=[Data.price])
async def choice_subcateg_food(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text

    date = data['date']
    categ = data.get('categ')
    subcateg = data['subcateg']
    price = data['price']
    who = message.from_user.first_name

    await state.finish()

    await message.answer(
        f"Дата: {date}\nКатегория: {categ}\nПодкатегория: {subcateg}\nЦена: {price}\nПользватель: {who}",
        reply_markup=nav.get_infoMenu()
    )

    bot._google_table.insert(
        data=date,
        categ=categ,
        subcateg=subcateg,
        price=price,
        who=who
    )