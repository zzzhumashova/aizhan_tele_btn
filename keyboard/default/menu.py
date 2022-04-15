from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Director"),
            KeyboardButton(text="Mugalimder")
        ],
        [
            KeyboardButton(text="Mamandyqtar"),
            KeyboardButton(text="Gruppalar")
        ],
    ],
    resize_keyboard=True
)
