from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters.text import Text
from keyboards.for_questions import get_keyboard_fab
from aiogram.methods import edit_message_text

router = Router()
user_data = []

@router.message(Text('Играть с друзьями'))
async def cmd_data(message: Message):
    await message.answer('Игрок1 против Игрок2', reply_markup=get_keyboard_fab())

@router.callback_query(Text('player1'))
async def player1(callback_query: CallbackQuery):
    await callback_query.message.answer('проверка')

@router.callback_query(Text('player2'))
async def player1(callback_query: CallbackQuery):
    await callback_query.message.answer('проверка')

@router.callback_query(Text('player2'))
async def player1(callback_query: CallbackQuery):
    await callback_query.message.answer('броб')

# создание сессии подключение игры подключение временной базы данной или что то наподобиии разбор колбэком и фильтров

# async def player1_text(message: types.Message, new_value: str):
#     user_data.append(str(message.from_user.first_name))
#     text_and_data = [
#         [user_data[0], 'player1'],
#         ['Vs', 'nn'],
#         ['Игрок2', 'player2'],
#     ]
#     keyboard = InlineKeyboardMarkup(row_width=3)
#     row_btns = (InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
#     keyboard.row(*row_btns)
#     await message.edit_text(new_value, reply_markup= keyboard)
#     print(user_data)
#
# async def player2_text(message: types.Message, new_value: str):
#     text_and_data = [
#         [user_data[0], 'player1'],
#         ['Vs', 'nn'],
#         [user_data[2], 'player2'],
#     ]
#     keyboard = InlineKeyboardMarkup(row_width=3)
#     row_btns = (InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
#     keyboard.row(*row_btns)
#     await message.edit_text(new_value, reply_markup= keyboard)