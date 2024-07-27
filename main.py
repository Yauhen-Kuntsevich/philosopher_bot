import asyncio
import logging

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from aiogram.filters import CommandStart

from bot_token import BOT_TOKEN
from messages import START_MESSAGE


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(
        text=f'Вітанкі, {message.from_user.full_name}!\n\n{START_MESSAGE}',
        parse_mode='HTML'
    )


async def main():
    logging.basicConfig(level=logging.DEBUG)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
