from pyrogram import Client, filters, types, errors
from config import prefix
from utils import text_animation
from asyncio import sleep
from plugins.settings import modules_info


@Client.on_message(filters.command('type', prefixes=prefix) & filters.me)
async def type_com(_, msg: types.Message):
    orig_text = msg.text.split(' ', maxsplit=1)[1]

    for i in text_animation(orig_text):
        try:
            await msg.edit(i)
        except errors.FloodWait as wait:
            await sleep(wait)
        await sleep(0.05)

modules_info['type'] = ['Makes typewriter animation']
