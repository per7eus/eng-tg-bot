from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

remove_button = ReplyKeyboardRemove()

show_ru_message = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Показать перевод", callback_data="show_ru_message")]])
show_en_message = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Вернуться на английский", callback_data="show_en_message")]])