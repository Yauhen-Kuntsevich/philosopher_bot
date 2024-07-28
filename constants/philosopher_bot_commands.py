from aiogram.types import BotCommand


BOT_COMMANDS = [
    BotCommand(command='/topic', description='Цытата паводле тэмы'),
    BotCommand(command='/philosopher', description='Цытата паводле філосафа'),
    BotCommand(command='/bio', description='Біяграфія філосафа / філасафіні'),
    BotCommand(command='/works', description='Філасофскі must read'),
    BotCommand(command='/help', description='Як я працую?'),
]
