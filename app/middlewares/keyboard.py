from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Приход 💰')],
    [KeyboardButton(text='Уход 💸')], 
    [KeyboardButton(text='Продукты 🍎')],
    [KeyboardButton(text='Категории 📊')]
], resize_keyboard=True)