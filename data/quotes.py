from dataclasses import dataclass
import json


@dataclass
class Quote:
    id: int
    author: str
    text: str
    image_path: str = ''


with open('data/quotes.json', 'r') as file:
    quotes: dict[str, list[Quote]] = json.load(file)

print(quotes.get('Час ⏳')[1].get('Id'))
