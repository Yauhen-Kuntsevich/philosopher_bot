from dataclasses import dataclass
import json


@dataclass
class Quote:
    id: int
    author: str
    text: str
    image_path: str = ""


with open("data/quotes.json", "r") as file:
    QUOTES: dict[str, list[Quote]] = json.load(file)


def get_authors():
    authors = []
    for quote in QUOTES:
        authors.append(quote.get("author"))

    return authors


TOPICS = QUOTES.keys()
AUTHORS = get_authors()
