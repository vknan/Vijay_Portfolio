# gunicorn_config.py
# import myproject.settings.production
import multiprocessing
bind = "192.168.1.3"
workers = multiprocessing.cpu_count() * 2 + 1
timeout = 120  # Set a higher timeout value (in seconds)
chdir = '/home/naresh-vijay-n/Vijay_Portfolio/Vijay_Portfolio/myproject'
# gunicorn_config.py



