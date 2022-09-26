from cmath import inf
from distutils.log import info
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


def get_infoMenu() -> ReplyKeyboardMarkup:

    infoMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)

    btnInfo = [
        KeyboardButton("Добавить \N{memo}"),
        KeyboardButton("Посмотреть \N{open book}")
    ]

    return infoMenu.add(*btnInfo)


def get_dateMenu() -> InlineKeyboardMarkup:

    dateMenu = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)

    btnDate = [
        InlineKeyboardButton("Сегодня", callback_data="date_now"),
        InlineKeyboardButton("Другая", callback_data="date_dr")
    ]

    return _create_markups(dateMenu, btnDate)

def get_mainMenu() -> InlineKeyboardMarkup:

    mainMenu = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)

    btn_mainMenu = [
        InlineKeyboardButton("Еда \U0001F60B", callback_data='main_food'), 
        InlineKeyboardButton("Транспорт \U0001F698", callback_data='main_trans'),
        InlineKeyboardButton("Здоровье \N{green heart}", callback_data='main_health'),
        InlineKeyboardButton("Дом \U0001F3E0", callback_data='main_house'),     
    ]

    return _create_markups(mainMenu, btn_mainMenu, add_other=True, type='main')


def get_lookupMenu() -> InlineKeyboardMarkup:

    lookupMenu = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)

    btn_lookup = [
        InlineKeyboardButton("Вчера", callback_data='lookup_yest'), 
        InlineKeyboardButton("Сегодня", callback_data='lookup_now'),
        InlineKeyboardButton("Пр. месяц", callback_data='lookup_monthyest'),
        InlineKeyboardButton("Тк. месяц", callback_data='lookup_monthnow'),
    ]

    return _create_markups(lookupMenu, btn_lookup)


def get_inlineMenu_food() -> InlineKeyboardMarkup:

    inlineMenu_food = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)

    btn_inlineMenu_food = [
        InlineKeyboardButton("Доставка \U0001F3C3", callback_data='food_dostavka'),
        InlineKeyboardButton("Работа \U0001F9D1", callback_data='food_rabota'),
        InlineKeyboardButton("Магазин \U0001F6D2", callback_data='food_magazin'),
        InlineKeyboardButton("Ресторан \U0001F468 ", callback_data='food_restoran'),
        InlineKeyboardButton("Не ЗОЖ \U0001F369 ", callback_data='food_nezozh'),
    ]

    return _create_markups(inlineMenu_food, btn_inlineMenu_food, add_other=True, type='food')


def get_inlineMenu_trans() -> InlineKeyboardMarkup:

    inlineMenu_trans = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)

    btn_inlineMenu_trans= [
        InlineKeyboardButton("Социалка \U0001F4C6", callback_data='trans_soc'),
        InlineKeyboardButton("Метро \U0001F687", callback_data='trans_metro'),
        InlineKeyboardButton("Такси \N{taxi}", callback_data='trans_taxi'),
        InlineKeyboardButton("Билеты \U0001F39F", callback_data='trans_bileti'),
    ]

    return _create_markups(inlineMenu_trans, btn_inlineMenu_trans, add_other=True, type='trans')


def get_inlineMenu_health() -> InlineKeyboardMarkup:

    inlineMenu_health = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)

    btn_inlineMenu_health = [
        InlineKeyboardButton("Медуслуги \U0001FA7A", callback_data='health_medusl'),
        InlineKeyboardButton("Лекарства \N{pill}", callback_data='health_pill'),
        InlineKeyboardButton("Гигиена \U0001F9FB", callback_data='health_gigiena'),
        InlineKeyboardButton("Спорт \U0001F4AA", callback_data='health_sport'),
        InlineKeyboardButton("Косметика \U0001F9F4", callback_data='health_kosmetika'),
    ]

    return _create_markups(inlineMenu_health , btn_inlineMenu_health, add_other=True, type='health')


def get_inlineMenu_house() -> InlineKeyboardMarkup:

    inlineMenu_house = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)

    btn_inlineMenu_house = [
        InlineKeyboardButton("Аренда \U0001F4B0", callback_data='house_arenda'),
        InlineKeyboardButton("Уборка \U0001F9F9", callback_data='house_uborka'),
        InlineKeyboardButton("ИнТех \U0001F50C", callback_data='house_intech'),
        InlineKeyboardButton("Уют \U0001FA94", callback_data='house_uyut'),
    ]

    return _create_markups(inlineMenu_house , btn_inlineMenu_house, add_other=True, type='house')


def get_inlineMenu_other() -> InlineKeyboardMarkup:

    inlineMenu_other = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)

    btn_inlineMenu_other = [
        InlineKeyboardButton("Подписка \U0001F4B3", callback_data='other_podpiska'),
        InlineKeyboardButton("Связь \U0001F4DE", callback_data='other_svyaz'),
        InlineKeyboardButton("Лук \U0001F457", callback_data='other_look'),
        InlineKeyboardButton("Обучение \U0001F4DA", callback_data='other_obuch'),
        InlineKeyboardButton("Развлечение \U0001F389", callback_data='other_razvlech'),	
    ]

    return _create_markups(inlineMenu_other, btn_inlineMenu_other, add_other=True, type='other')


def _create_markups(kb, btn, add_other=False, type='other'):
    if not add_other:
        return kb.add(*btn)

    else:
        cb = f'{type}_other'
        btnOther = InlineKeyboardButton("Другое \U0001F635 ", callback_data=cb) 
        return kb.add(*btn, btnOther)


async def back_to_Menu(call: CallbackQuery, menu, text=None):

    if menu == 'info':
        kb = get_infoMenu()
        await call.message.answer("Что нужно сделать?", reply_markup=kb)
        return
    
    if menu == 'main':
        kb = get_mainMenu()
    
    if menu == 'data':
        kb = get_dateMenu()
    
    await call.message.edit_text(text)
    await call.message.edit_reply_markup(kb)