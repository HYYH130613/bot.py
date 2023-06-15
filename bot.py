import asyncio
from aiogram import Bot, Dispatcher
from Handlers import questions, questions_for_chat_play

from config import TOKEN


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(questions.router)
    dp.include_router(questions_for_chat_play.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())