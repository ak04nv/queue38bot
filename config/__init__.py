from . import default as settings
from .logging import get_logger
from .database import get_database


db = get_database(settings)
logger = get_logger(settings)
