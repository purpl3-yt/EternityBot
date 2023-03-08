from pyrogram import Client, filters, types
from plugins.settings import modules_info
from config import prefix
import os


@Client.on_message(filters.command('info', prefixes=prefix) & filters.me)
async def info_command(_: Client, msg: types.Message):
    await msg.edit(f'''
<b>🎲 EternityBot 🎲</b><b>
🔗 Prefix: «<code>{prefix}</code>»
💻 System: {'Windows 🪟' if os.name == 'nt' else 'Linux 🐧'}
</b>''')

modules_info['info'] = 'Get info about EternityBot!'
