from aiogram.types import BotCommand

import logging

async def command(dp):
    await dp.bot.set_my_commands(
        [
            BotCommand("add", "Новая запись"),
            BotCommand("look", "Посмотреть"),
            BotCommand("reset", "Сброс")
        ]
    )


if __name__ == '__main__':
    from aiogram import executor
    from utils.handlers import dp

    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

    executor.start_polling(dp, skip_updates=True, on_startup=command)