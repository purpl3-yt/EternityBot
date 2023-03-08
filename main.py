from config import api_id, api_hash
from pyrogram import Client
from utils import restart
import os
import sys
# imports


def configure():
    os.chdir(sys.path[0])

    if not os.path.isfile('config.py'):
        with open('config.py', 'w') as cfg:
            cfg.write("api_id = 123\napi_hash = '123'\nprefix = '.'")

        restart()


configure()

if api_id == '123' and api_hash == '123':
    print('Please change api_id and api_hash in config.py!')
    quit()

Client = Client(
    'EternityBot',
    api_id,
    api_hash,
    plugins=dict(
        root="plugins")).run()
