import aiohttp
import xml.etree.ElementTree as etree

from io import StringIO
from config import logger, settings


async def get_queue(number):
    data = await fetch_data(settings.URL,
                            settings.REQUEST.format(number),
                            {'content-type': 'text/xml; charset="UTF-8'})
    return parse_data(data) if data else None


def parse(el):
    r = (el.find('ns2:characteristicName', settings.NS).text,
         el.find('ns2:characteristic', settings.NS).text)
    return ': '.join(r)


def parse_data(data):
    tree = etree.parse(StringIO(data))

    err = tree.find('.//ns2:error', settings.NS)
    if err is not None:
        return err.text

    l = []
    for x in tree.findall('.//ns2:any', settings.NS):
        l.append(parse(x))
    return '\n'.join(l)


async def fetch_data(url, data, headers):
    '''Helper for fetch data from url'''
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data, headers=headers) as resp:
            if resp.status == 200:
                return await resp.text()
            logger.warn('Fetch data status failed. URL: {}, args: {},\
                         status: {}'.format(url, params, resp.status))
    return None
