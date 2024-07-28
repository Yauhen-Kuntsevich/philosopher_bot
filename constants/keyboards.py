from data.quotes import topics 
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def get_topics_keyboard() -> ReplyKeyboardMarkup:    
    topics_buttons = [KeyboardButton(text=topic) for topic in topics]

    topics_buttons_row: list[KeyboardButton] = []
    topics_buttons_rows: list[list[KeyboardButton]] = []

    for button in topics_buttons:
        topics_buttons_row.append(button)
        if len(topics_buttons_row) == 2:
            topics_buttons_rows.append(topics_buttons_row)
            topics_buttons_row = []

    if topics_buttons_row:
        topics_buttons_rows.append(topics_buttons_row)
    
    return ReplyKeyboardMarkup(
        keyboard=topics_buttons_rows,
        resize_keyboard=True
    )


topics_keyboard = get_topics_keyboard()
