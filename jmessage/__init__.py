from .users import User
from .common import *
from .url import *
from .groups import Group
from .messages import Message
import logging

__all__ = [
    User,
    Group,
    Message,
    url,
    common
]

__version__ = '1.0.2'
VERSION = tuple(map(int,  __version__.split('.')))

# Silence urllib3 INFO logging by default

logging.getLogger(
    'requests.packages.urllib3.connectionpool').setLevel(logging.WARNING)
