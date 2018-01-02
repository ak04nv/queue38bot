import os
import pathlib

# Basic settings
DEBUG = False
PROJECT_ROOT = str(pathlib.Path(__file__).parent.parent)

ADMINS = ('ak04nv',)

BOT_TOKEN = ''
LOG_FILE = 'log/bot.log'

HOST = ''  # public IP address
PORT = 443
# Howto generate certificate
# $ openssl genrsa -out config/webhook_pkey.pem 2048
# $ openssl req -new -x509 -days 3650 -key config/webhook_pkey.pem -out config/webhook_cert.pem
# Common Name should contains public IP address
WEBHOOK_SSL_CERT = 'config/webhook_cert.pem'
WEBHOOK_SSL_PRIV = 'config/webhook_pkey.pem'

NS = {'ns2': 'http://idecs.nvg.ru/privateoffice/ws/types/'}
URL = 'https://dou.iro38.ru/external/complect-form/smev/numberinqueue'
REQUEST = '<soapenv:Envelope\
             xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"\
             xmlns:urn="urn:ru.gov.economy:standard.ws:complect"\
             xmlns:typ="http://idecs.nvg.ru/privateoffice/ws/types/">\
               <soapenv:Header/>\
               <soapenv:Body>\
                 <urn:getNumberInQueue>\
                   <request>\
                     <typ:ocato></typ:ocato>\
                     <typ:uid>{}</typ:uid>\
                   </request>\
                 </urn:getNumberInQueue>\
               </soapenv:Body>\
           </soapenv:Envelope>'

# MongoDB settings
DB_NAME = 'queue38'
DB_HOST = 'localhost'
DB_PORT = 27017
DB_MAX_POOL_SIZE = 300

# Settings for current machine
try:
    from settings import *
except ImportError:
    pass
