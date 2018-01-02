import logging

from os.path import basename
from logging.handlers import RotatingFileHandler


def init(settings):
    if settings.DEBUG:
        kwargs = {'level': logging.DEBUG}
    else:
        kwargs = {'format': '%(levelname)s:%(asctime)s:%(message)s',
                  'handlers': [RotatingFileHandler(settings.LOG_FILE,
                                                   maxBytes=200000,
                                                   backupCount=7)]}
    logging.basicConfig(**kwargs)


def get_logger(settings):
    return logging.getLogger(basename(settings.PROJECT_ROOT))
