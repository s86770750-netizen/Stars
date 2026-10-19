import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import BotCommand, BotCommandScopeDefault, MenuButtonCommands

TOKEN = os.getenv("BOT_TOKEN")  # токен от @BotFather, задаётся в переменной окружения

TEXT = (
    '<tg-emoji emoji-id="5274099962655816924">❗️</tg-emoji> '
    "Бот перегружен. Пожалуйста, вернитесь позже — "
    "наши специалисты разберутся с проблемой."
)

COMMANDS = [
    BotCommand(command="start", description="Запустить бота"),
    BotCommand(command="profile", description="Профиль"),
]

dp = Dispatcher()


# Любая команда (/start, /profile, /что-угодно) и любое сообщение -> один и тот же текст
@dp.message()
async def any_message(message: types.Message):
    await message.answer(TEXT)


async def main():
    if not TOKEN:
        raise RuntimeError("Не задана переменная окружения BOT_TOKEN")

    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # Кнопка «Меню» рядом с полем ввода со списком команд
    await bot.set_my_commands(COMMANDS, scope=BotCommandScopeDefault())
    await bot.set_chat_menu_button(menu_button=MenuButtonCommands())

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
