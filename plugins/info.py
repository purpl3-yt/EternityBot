from pyrogram import Client, filters, types
from plugins.settings import modules_info
from config import prefix
import os


@Client.on_message(filters.command('info', prefixes=prefix) & filters.me)
async def info_command(_: Client, msg: types.Message):
    await msg.edit(f'''
<b>๐ฒ EternityBot ๐ฒ</b><b>
๐ Prefix: ยซ<code>{prefix}</code>ยป
๐ป System: {'Windows ๐ช' if os.name == 'nt' else 'Linux ๐ง'}
</b>''')

modules_info['info'] = 'Get info about EternityBot!'
