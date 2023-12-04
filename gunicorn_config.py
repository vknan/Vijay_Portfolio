# gunicorn_config.py
# import myproject.settings.production
import multiprocessing
bind = "192.168.1.7:8000"
workers = multiprocessing.cpu_count() * 2 + 1
timeout = 120  # Set a higher timeout value (in seconds)
chdir = '/home/naresh-vijay-n/Vijay_Portfolio/myenv/bin/'
# gunicorn_config.py



