from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot_app.bot import dp
from .data_fetcher import get_all_fields_api, get_config, get_images, filter_area, filter_size
from .functions import create_message
from .keyboards import main_keyboard, filter_keyboard
from .states import FilterStates


@dp.message_handler(commands="start")
async def get_hello_text(message: types.Message):
    data = await get_config()
    hello_text = ""
    for i in data:
        if i.get("title") == "приветствие":
            hello_text: str = i.get("value")
        else:
            await message.answer("Я бот с футбольными полями", reply_markup=main_keyboard)
            return None
    await message.answer(text=f"{hello_text}", reply_markup=main_keyboard)


@dp.message_handler(lambda m: m.text == "Все поля")
async def all_fields(message: types.Message):
    data = await get_all_fields_api()  # Get a data with all football fields from django. Returns a JSON
    images = await get_images()  # Get all images from django. Returns the absolute path of the filesа бл
    await create_message(data, images, message)


@dp.message_handler(lambda m: m.text == "Фильтры")
async def filter_handler(message: types.Message):
    await message.answer("Укажите фильтр", reply_markup=filter_keyboard)  # Choice a filter
    # Available filters are listed in the filter_keyboard
    await FilterStates.choice_filter.set()


@dp.message_handler(Text(equals="Назад в меню", ignore_case=True), state=["*"])
async def cancel_handler(message: types.Message, state: FSMContext):
    """This function handled all state and return you to main menu"""
    await state.finish()
    await message.answer(text="Возврат в меню", reply_markup=main_keyboard)


@dp.message_handler(state=FilterStates.choice_filter)
async def filter_state(message: types.Message, state: FSMContext):
    data = await get_all_fields_api()
    unique_data = []  # This list will hold unique data
    await message.answer("Результаты: ", reply_markup=main_keyboard)

    if message.text == "Адрес":
        addresses = InlineKeyboardMarkup()
        for i in data:

            if i.get("size") in unique_data:
                continue

            unique_data.append(i.get("size"))
            addresses.add(InlineKeyboardButton(i.get("address"), callback_data=f"address:{i.get('address')}"))
            # Add a button with value
        await message.answer("Введите фильтр", reply_markup=addresses)
        await state.finish()

    elif message.text == "Размер":
        sizes = InlineKeyboardMarkup()
        for i in data:

            if i.get("size") in unique_data:  # Screening out the same values
                continue

            unique_data.append(i.get("size"))
            sizes.add(InlineKeyboardButton(i.get("size"), callback_data=f"size:{i.get('size')}"))
            # Add a button with value
        await message.answer("Введите фильтр", reply_markup=sizes)
        await state.finish()
    else:
        # Continue if user not clicked the button
        await message.answer("Такого фильтра нет", reply_markup=filter_keyboard)
        await FilterStates.choice_filter.set()


@dp.callback_query_handler(lambda c: c.data.startswith("address:"))
async def callback_address(callback_data: types.CallbackQuery):
    await callback_data.answer("Успешно")  # Display a small your message
    data = await filter_area(callback_data.data.replace("address:", ""))
    images = await get_images()
    await create_message(data, images, callback_data.message)


@dp.callback_query_handler(lambda c: c.data.startswith("size:"))
async def callback_address(callback_data: types.CallbackQuery):
    await callback_data.answer("Успешно")  # Display a small your message
    data = await filter_size(callback_data.data.replace("size:", ""))
    images = await get_images()
    await create_message(data, images, callback_data.message)


@dp.message_handler()
async def other_handler(message: types.Message):
    """This handler handled all message who didn't make it into any of the handler"""
    await message.answer("Нет такой команды", reply_markup=main_keyboard)
