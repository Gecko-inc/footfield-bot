from aiogram.dispatcher.filters.state import StatesGroup, State


class FilterStates(StatesGroup):
    choice_filter = State()
