from pyrogram import Client, filters, types
from plugins.settings import modules_info
from config import prefix
from utils import warn
import os


@Client.on_message(filters.command('terminal', prefixes=prefix) & filters.me)
async def terminal_command(_: Client, msg: types.Message):
    try:
        str(msg.text).split(' ')[1]
    except IndexError:
        await warn(msg, Client, 'Enter an command!')
        return None
    else:
        cmd = ' '.join(str(msg.text).split(' ')[1:])
        await msg.edit(f'⌨️ <b>Command: </b><code>{cmd}</code><b>...</b>')
        await msg.edit(f'⌨️ <b>Command: </b><code>{cmd}</code>\n<b>Output: </b>' + os.popen(cmd).read())

modules_info['terminal'] = ['Get output of command']
