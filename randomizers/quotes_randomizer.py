from random import randint
from data.quotes import QUOTES_DICT
from data.quotes import AUTHORS


def get_random_quote_by_topic(topic):
    quotes_by_topic = QUOTES_DICT.get(topic)

    random_index = randint(0, len(quotes_by_topic) - 1)
    return quotes_by_topic[random_index]


def get_random_quote_by_author(author):
    quotes_by_author = []

    for quote in QUOTES_DICT:
        if quote.get("author") == author:
            quotes_by_author.append(quote)

    random_index = randint(0, len(quotes_by_author) - 1)
    return quotes_by_author[random_index]
