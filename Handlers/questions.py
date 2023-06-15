from aiogram import Router
from aiogram.filters import Command
from aiogram.filters.text import Text
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from keyboards.for_questions import get_start_menu_kb, get_yes_no_menu_kb
import random

router = Router()

possible_actions = ["✊", "✋", '✌']

@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer('Привет! Я бот для игры в камень ножницы бумага', reply_markup=get_start_menu_kb())


@router.message(lambda message: message.text == "Начать игру" or message.text == "Да")
async def answer_yes(message: Message):
    kb = [
        [
            KeyboardButton(text='✊'),
            KeyboardButton(text="✋"),
            KeyboardButton(text='✌'),
        ],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="камень, ножницы или бумага"
    )
    await message.answer(
        "Сделайте выбор — камень, ножницы или бумага:",
        reply_markup=keyboard
    )

@router.message(lambda message: message.text == "✊" or message.text == "✋" or message.text == '✌')
async def get_choise(message: Message):
        # global data_w, data_d
        computer_action = random.choice(possible_actions)
        user_action = message.text
        while True:
            await message.answer(f"Вы выбрали {message.text}, компьютер выбрал {computer_action}.")
            if user_action == computer_action:
                await message.answer(f"Оба пользователя выбрали {user_action}. Ничья!!")
            elif user_action == "✊":
                if computer_action == '✌':
                        # data_w += 1
                    await message.answer("Камень бьет ножницы! Вы победили!")
                else:
                        # data_d += 1
                    await message.answer("Бумага оборачивает камень! Вы проиграли.")
            elif user_action == "✋":
                if computer_action == "✊":
                        # data_w += 1
                    await message.answer("Бумага оборачивает камень! Вы победили!")
                else:
                        # data_d += 1
                    await message.answer("Ножницы режут бумагу! Вы проиграли.")
            elif user_action == '✌':
                if computer_action == "✋":
                        # data_w += 1
                    await message.answer("Ножницы режут бумагу! Вы победили!")
                else:
                        # data_d += 1
                    await message.answer("Камень бьет ножницы! Вы проиграли.")
            break
        await message.answer('Продолжать?', reply_markup=get_yes_no_menu_kb())

@router.message(Text(text='Нет'))
async def answer_no(message: Message):
    await message.answer(
        'пон пока!'
    )

