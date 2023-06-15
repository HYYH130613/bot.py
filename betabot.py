import random
import asyncio
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Text, Command, IsSenderContact, ChatTypeFilter
from typing import Optional
from aiogram.types import ReplyKeyboardRemove,\
    ReplyKeyboardMarkup, KeyboardButton,\
    InlineKeyboardMarkup, InlineKeyboardButton
from config import TOKEN
import logging

possible_actions = ["✊", "✋", '✌']
data_w, data_d= 0, 0
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
user_data = []
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):

    kb = [
        [
            KeyboardButton(text='Начать игру'),
            KeyboardButton(text='Статистика'),

        ],
        [
            KeyboardButton(text="Играть с друзьями"),
            KeyboardButton(text='Настройки'),
        ],
        [   KeyboardButton(text='Донаты'),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="..."
    )
    await message.reply('Привет! Я бот для игры в камень ножницы бумага', reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == c)
async def cmd_play(message: types.Message):
    kb = [
        [
            KeyboardButton(text='✊'),
            KeyboardButton(text="✋"),
            KeyboardButton(text='✌'),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard= True,
        input_field_placeholder="камень, ножницы или бумага"
    )
    await message.answer(
                         "Сделайте выбор — камень, ножницы или бумага:",
                         reply_markup=keyboard
                         )

@dp.message_handler(lambda message: message.text == "✊" or message.text == "✋" or message.text == '✌')
async def get_choise(message: types.Message):
            global data_w, data_d
            computer_action = random.choice(possible_actions)
            user_action = message.text
            await message.answer(f"Вы выбрали {message.text}, компьютер выбрал {computer_action}.")
            if user_action == computer_action:
                await message.answer(f"Оба пользователя выбрали {user_action}. Ничья!!")
            elif user_action == "✊":
                if computer_action == '✌':
                    data_w+=1
                    await message.answer("Камень бьет ножницы! Вы победили!")
                else:
                    data_d+=1
                    await message.answer("Бумага оборачивает камень! Вы проиграли.")
            elif user_action == "✋":
                if computer_action == "✊":
                    data_w += 1
                    await message.answer("Бумага оборачивает камень! Вы победили!")
                else:
                    data_d += 1
                    await message.answer("Ножницы режут бумагу! Вы проиграли.")
            elif user_action == '✌':
                if computer_action == "✋":
                    data_w += 1
                    await message.answer("Ножницы режут бумагу! Вы победили!")
                else:
                    data_d += 1
                    await message.answer("Камень бьет ножницы! Вы проиграли.")

# class NumbersCallbackFactory(CallbackData, prefix="fabnum"):
#     action: str
#     value: Optional[int]
def get_keyboard_fab():
    text_and_data = [
        ['Игрок1', 'player1'],
        ['Vs', 'nn'],
        ['Игрок2', 'player2'],
    ]
    keyboard = InlineKeyboardMarkup(row_width=3)
    row_btns = (InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
    keyboard.row(*row_btns)
    return keyboard.add()

@dp.message_handler(chat_type=['group'],commands="star")
async def cmd_data(message: types.Message):
    text_and_data = [
        ['Игрок1', 'player1'],
        ['Vs', 'nn'],
        ['Игрок2', 'player2'],
    ]
    keyboard = InlineKeyboardMarkup(row_width=3)
    row_btns = (InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
    keyboard.row(*row_btns)
    await message.answer('Игрок1 против Игрок2', reply_markup=keyboard)

async def player1_text(message: types.Message, new_value: str):
    user_data.append(str(message.from_user.first_name))
    text_and_data = [
        [user_data[0], 'player1'],
        ['Vs', 'nn'],
        ['Игрок2', 'player2'],
    ]
    keyboard = InlineKeyboardMarkup(row_width=3)
    row_btns = (InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
    keyboard.row(*row_btns)
    await message.edit_text(new_value, reply_markup= keyboard)
    print(user_data)

async def player2_text(message: types.Message, new_value: str):
    text_and_data = [
        [user_data[0], 'player1'],
        ['Vs', 'nn'],
        [user_data[2], 'player2'],
    ]
    keyboard = InlineKeyboardMarkup(row_width=3)
    row_btns = (InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
    keyboard.row(*row_btns)
    await message.edit_text(new_value, reply_markup= keyboard)

@dp.callback_query_handler(text="player1")
async def cmd_data(query: types.CallbackQuery):
    user_data.append(str(query.from_user.first_name))
    await player1_text(query.message, f'{user_data[0]} против Игрока2')

@dp.callback_query_handler(text="player2")
async def cmd_data(query: types.CallbackQuery):
    user_data.append(str(query.from_user.first_name))
    await player2_text(query.message, f'{user_data[0]} против {user_data[2]}')

@dp.message_handler(lambda message: message.text == "Статистика")
async def cmd_data(message: types.Message):
    global data_w, data_d
    await message.answer(
        f"Победы: {data_w}"
        f"\nПроигрыши: {data_d}",
    )

@dp.message_handler(commands=['help'])
async def process_start_command(message: types.Message):
    await message.reply("Победитель определяется по следующим правилам:"
                        "\nБумага побеждает камень («бумага обёртывает камень»)."
                        "\nКамень побеждает ножницы («камень затупляет или ломает ножницы»)."
                        "\nНожницы побеждают бумагу («ножницы разрезают бумагу»)."
                        )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
