from aiogram import types
from aiogram.types import ReplyKeyboardMarkup

def get_yes_no_kb() -> ReplyKeyboardMarkup:
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=3)
    btns_text = ('Yes!', 'No!')

    keyboard_markup.row(*(types.KeyboardButton(text) for text in btns_text))

    more_btns_text = (
        "I don't know",
        "Who am i?",
        "Where am i?",
        "Who is there?",
    )
    return keyboard_markup.add(*(types.KeyboardButton(text) for text in more_btns_text))