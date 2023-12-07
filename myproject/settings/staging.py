# myproject/settings/staging.py

from .base import *

# Override base settings for staging

DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1', 'navikonline.in', 'www.navikonline.in', '192.168.1.5', 'fe80::336f:ed6f:3485:4aeb']
