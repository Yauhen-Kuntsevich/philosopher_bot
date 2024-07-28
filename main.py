import asyncio
import logging

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from aiogram.filters import Command, CommandStart

from constants.bot_token import BOT_TOKEN
from constants.philosopher_bot_commands import BOT_COMMANDS
from constants.messages import START_MESSAGE
from constants.keyboards import topics_keyboard

from data.quotes import topics

from randomizers.quotes_randomizer import get_random_quote_by_topic


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


bot_commands = [
    types.BotCommand(command='/help', description='Як я працую?'),
]



@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(
        text=f'Вітанкі, {message.from_user.full_name}!\n\n{START_MESSAGE}',
        parse_mode='HTML'
    )


@dp.message(Command('topic'))
async def handle_topic(message: types.Message):
    await message.answer(
        text='На якую тэму табе хочацца атрымаць цытату?',
        reply_markup=topics_keyboard
    )


@dp.message(Command('works'))
async def handle_works(message: types.Message):
    pass


@dp.message(Command('help'))
async def handle_help(message: types.Message):
    pass


@dp.message()
async def handle_topic_choice(message: types):
    if message.text in topics:
        random_quote = get_random_quote_by_topic(message.text)

    await message.answer(
        text=f'{random_quote.get('text')}\n\n<b>{random_quote.get('author')}</b>',
        parse_mode='HTML'
    )


async def main():
    logging.basicConfig(level=logging.DEBUG)
    
    await bot.set_my_commands(BOT_COMMANDS)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
