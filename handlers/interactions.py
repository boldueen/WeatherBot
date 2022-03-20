from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, CommandHelp


from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(msg: types.Message):
    await msg.answer(f"<b>👤 Привет, {msg.from_user.full_name}!</b>\n\n"
                     f"Я погодный бот, умею присылать погоду.\n"
                     f"Для помощи: /help")


@dp.message_handler(CommandHelp())
async def bot_help(msg: types.Message):
    text = ("<b>🗒 Список команд:</b>\n",
            "/help - Получить справку",
            "/start - Перезапустить бота"
            )

    await msg.answer("\n".join(text))