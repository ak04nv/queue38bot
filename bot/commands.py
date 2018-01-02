from config import db, settings
from datetime import timedelta

from bot.utils import get_queue

help_msg = '''
Использование:
/help - Вывод справки
/queue - Задать номер заявки
/check - Проверить номер очереди
'''


def register_commands(bot):
    '''Registering commands'''
    for cmd in ('help', 'start', 'queue', 'check'):
        bot.add_command('/{}'.format(cmd), eval(cmd))


async def help(chat, msg):
    return await chat.send_text(help_msg)


async def start(chat, msg):
    d = ({'id': chat.id},
         {'$set': {'username': chat.sender.get('username', ''),
                   'fullname': '{first_name} {last_name}'
                   .format(**chat.sender)}})
    await db.chats.find_one_and_update(*d, upsert=True)
    return await chat.send_text(help_msg)


async def check(chat, match):
    d = await db.chats.find_one({'id': chat.id})
    if 'queue' not in d:
        msg = 'Номер заявки не установлен. Используйте команду /queue'
    else:
        msg = await get_queue(d['queue']) or \
            'Ошибка при проверке. Попробуйте позже.'
    return await chat.send_text(msg)


async def queue(chat, match):
    number = chat.message.get('text', '').lstrip('/queue').strip()
    if not number:
        chat.bot.set_next_step(chat, queue)
        msg = 'Введите номер заявки (состоит из 16 цифр)'
    else:
        clean_number = ''.join([x for x in number if x.isdigit()])
        if len(clean_number) == 16:
            msg = 'Номер сохранён. Для проверки используйте команду /check'
            cond = ({'id': chat.id},
                    {'$set': {'queue': clean_number}})
            await db.chats.find_one_and_update(*cond, upsert=True)
        else:
            msg = 'Неверный номер заявки. Проверьте правильность.'
    return await chat.send_text(msg)
