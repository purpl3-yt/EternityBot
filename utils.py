from pyrogram import Client, types
from asyncio import sleep
from os import execl
import platform
import sys
import random


def bold(text): return '<b>' + text + '</b>'
def code(text): return '<code>' + text + '</code>'


async def warn(msg: types.Message, client: Client, warn_text: str, error=True):
    if error:
        await msg.edit('⛔️ ' + bold(warn_text))
        await sleep(3)
        await msg.delete()

    elif not error:
        await msg.edit('ℹ️ ' + bold(warn_text))
        await sleep(3)
        await msg.delete()


def restart():
    if str(platform.system()).lower() == 'linux':
        execl(sys.executable, 'python', 'main.py')
    elif str(platform.system()).lower() == 'windows':
        execl(sys.executable, 'python', 'main.py')
    exit()


def text_animation(text):
    symbols = ['*', '@', '#', '$', '%', '^', '&', '&']
    temp = text
    temp += temp[:1]
    shif = []
    for i in range(1, len(temp) + 1):
        shif.append(random.choice(symbols))
    steps = []
    phrase = []
    for i in range(1, int(len(temp)) + 1):
        phrase.append(temp[i - 1:i])
    x = 0
    for i in phrase:
        shif.pop(x)
        str = ''.join(shif)
        steps.append(str)
        shif.insert(x, i)
        str = ''.join(shif)
        x += 1
    return steps
