import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command
from loader import dp

from utils.state import WeatherState as WS


# Set weather state if no args
@dp.message_handler(Command(['weather', 'погода']))
async def test(msg: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(types.KeyboardButton('🗺️ Отправить геопозицию', request_location=True))
    await msg.answer(text="Прикрепите геопозицию", reply_markup=keyboard)
    await WS.location.set()


# Get answer for weather state
@dp.message_handler(content_types=[types.ContentType.LOCATION], state=WS.location)
async def location(msg: types.Message, state: FSMContext):
    await msg.answer(msg.location)
    await state.finish()

# # Отправлена геопозиция
# @dp.message_handler(content_types=[types.ContentType.LOCATION])
# async def weather_by_location(message: types.Message):
#     location = {
#         'lat': message.location['latitude'],
#         'lng': message.location['longitude']
#     }
#     await message.reply(text="\n".join(location), reply_markup=types.ReplyKeyboardRemove())
