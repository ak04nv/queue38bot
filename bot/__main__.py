import asyncio
from aiohttp import web

from config import logging, settings
from bot.main import create_bot


if __name__ == '__main__':
    logging.init(settings)
    bot = create_bot(settings.BOT_TOKEN)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bot.delete_webhook())

    if settings.DEBUG:
        bot.run(debug=True, reload=True)
    else:
        path = '/{}/'.format(settings.BOT_TOKEN)
        app = bot.create_webhook_app(path, loop)
        cert = open(settings.WEBHOOK_SSL_CERT, 'r')
        url = 'https://{}:{}{}'.format(settings.HOST, settings.PORT, path)
        loop.run_until_complete(bot.set_webhook(url, certificate=cert))
        web.run_app(app, host='127.0.0.1', port=5000)
