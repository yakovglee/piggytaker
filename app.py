from aiogram.types import BotCommand

async def command(dp):
    await dp.bot.set_my_commands(
        [
            BotCommand("start", "Новая запись"),
            BotCommand("reset", "Сброс")
        ]
    )

if __name__ == '__main__':
    from aiogram import executor
    from utils.handlers import dp

    executor.start_polling(dp, skip_updates=True, on_startup=command)