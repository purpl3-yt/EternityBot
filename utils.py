from pyrogram import Client, types
from asyncio import sleep
from os import execl
import platform
import sys

bold = lambda text: '<b>'+text+'</b>'
code = lambda text: '<code>'+text+'</code>'

async def warn(msg: types.Message, client: Client, warn_text: str, error = True):
    if error:
        await msg.edit('⛔️ '+bold(warn_text))
        await sleep(3)
        await msg.delete()
        
    elif not error:
        await msg.edit('ℹ️ '+bold(warn_text))
        await sleep(3)
        await msg.delete()

def restart():
    if str(platform.system()).lower() == 'linux':
        execl(sys.executable, 'python', 'main.py')
    elif str(platform.system()).lower() == 'windows':
        execl(sys.executable, 'python', 'main.py')
    exit()