from random import randint
from data.quotes import QUOTES


def get_random_quote_by_topic(topic):
    quotes_by_topic = QUOTES.get(topic)

    random_index = randint(1, len(quotes_by_topic) - 1)
    return quotes_by_topic[random_index]
