from aiogram.types import ReplyKeyboardMarkup

main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
main_keyboard.add("Все поля")
main_keyboard.add("Фильтры")

filter_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
filter_keyboard.add("Адрес")
filter_keyboard.add("Размер")
filter_keyboard.add("Назад в меню")
