from .bot import Bot
from .commands import register_commands


def create_bot(token):
    bot = Bot(token)
    register_commands(bot)
    return bot
