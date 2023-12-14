# myproject/settings/staging.py

from .base import *

# Override base settings for staging

DEBUG = False
ALLOWED_HOSTS = ['*']
