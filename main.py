import asyncio
import logging

from aiogram import Bot
from aiogram import Dispatcher
from aiogram.types import Message, BotCommand
from aiogram.filters import Command, CommandStart

from constants.bot_token import BOT_TOKEN
from constants.philosopher_bot_commands import BOT_COMMANDS
from constants.messages import START_MESSAGE
from constants.keyboards import topics_keyboard, authors_keyboard

from data.quotes import AUTHORS, TOPICS

from randomizers.quotes_randomizer import (
    get_random_quote_by_author,
    get_random_quote_by_topic,
)


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


bot_commands = [
    BotCommand(command="/help", description="Як я працую?"),
]


@dp.message(CommandStart())
async def handle_start(message: Message):
    await message.answer(
        text=f"Вітанкі, {message.from_user.full_name}!\n\n{START_MESSAGE}",
        parse_mode="HTML",
    )


@dp.message(Command("topic"))
async def handle_topic(message: Message):
    await message.answer(
        text="На якую тэму табе хочацца атрымаць цытату?",
        reply_markup=topics_keyboard,
    )


@dp.message(lambda message: message.text in TOPICS)
async def handle_topic_choice(message: Message):
    random_quote = get_random_quote_by_topic(message.text)
    await message.answer(
        text=f"{random_quote.get('text')}\n\n<b>{random_quote.get('author')}</b>",
        parse_mode="HTML",
    )


@dp.message(Command("philosopher"))
async def handle_philosopher(message: Message):
    await message.answer(
        text="Цытату якога філосафа табе хацелася б атрымаць?",
        reply_markup=authors_keyboard,
    )


@dp.message(lambda message: message.text in AUTHORS)
async def handle_author_choice(message: Message):
    random_quote = get_random_quote_by_author(message.text)
    await message.answer(
        text=f"{random_quote.get('text')}\n\n<b>{random_quote.get('author')}</b>",
        parse_mode="HTML",
    )


@dp.message(Command("works"))
async def handle_works(message: Message):
    pass


@dp.message(Command("help"))
async def handle_help(message: Message):
    pass


async def main():
    logging.basicConfig(level=logging.DEBUG)

    await bot.set_my_commands(BOT_COMMANDS)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
