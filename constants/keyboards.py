from data.quotes import TOPICS, AUTHORS
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def create_keyboard(values_for_buttons: list[str]) -> ReplyKeyboardMarkup:
    buttons = [KeyboardButton(text=value) for value in values_for_buttons]

    buttons_row: list[KeyboardButton] = []
    buttons_rows: list[list[KeyboardButton]] = []

    for button in buttons:
        buttons_row.append(button)
        if len(buttons_row) == 2:
            buttons_rows.append(buttons_row)
            buttons_row = []

    if buttons_row:
        buttons_rows.append(buttons_row)

    return ReplyKeyboardMarkup(keyboard=buttons_rows, resize_keyboard=True)


topics_keyboard = create_keyboard(TOPICS)
authors_keyboard = create_keyboard(AUTHORS)
