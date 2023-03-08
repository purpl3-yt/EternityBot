from pyrogram import Client, filters, types
from plugins.settings import modules_info
from config import prefix

@Client.on_message(filters.command('calc', prefixes=prefix) & filters.me)
async def calc_command(_: Client, msg: types.Message):
    await msg.edit('✅ <b>Answer: '+str(eval(' '.join(str(msg.text).split(' ')[1:])))+'</b>')

modules_info['calc'] = 'calculates things'