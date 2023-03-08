from pyrogram import Client, filters, types
from plugins.settings import modules_info
from config import prefix

@Client.on_message(filters.command('doxbin', prefixes=prefix) & filters.all)
async def doxbin_command(_: Client, msg: types.Message):
    await msg.reply('<b>Жди себя на доксбин</b>')

modules_info['doxbin'] = 'Meme about site doxbin'