from dataclasses import dataclass
import json


@dataclass
class Quote:
    id: int
    author: str
    text: str
    image_path: str = ""


with open("data/quotes.json", "r") as file:
    QUOTES_DICT: dict[str, list[Quote]] = json.load(file)


def get_authors():
    authors = []

    for topic in QUOTES_DICT.keys():
        for quote in QUOTES_DICT.get(topic):
            authors.append(quote.get("author"))

    return authors


TOPICS = QUOTES_DICT.keys()
AUTHORS = get_authors()
