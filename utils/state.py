from aiogram.dispatcher.filters.state import StatesGroup, State


class WeatherState(StatesGroup):
    location = State()
    # Q1 = State()
    # Q2 = State()
