from aiogram.types import ReplyKeyboardMarkup,InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def get_start_menu_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    text_and_data = [
        'Начать игру',
        'Статистика',
        'Играть с друзьями',
        'пшщриощвчаз'
    ]
    for i in text_and_data:
        kb.button(text=i)
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)

def get_yes_no_menu_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    text_and_data = [
        'Да',
        'Нет'
    ]
    for i in text_and_data:
        kb.button(text=i)
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)

def get_keyboard_fab() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    text_and_data = [
        ['Игрок1', 'player1'],
        ['Vs', 'nn'],
        ['Игрок2', 'player2'],
    ]
    for text, data in text_and_data:
        kb.button(text=text, callback_data=data)
    kb.adjust(3)
    return kb.as_markup()

