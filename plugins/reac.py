from pyrogram import Client, filters, types, errors
from config import prefix
from utils import warn
from plugins.settings import modules_info


@Client.on_message(filters.command('reac', prefixes=prefix) & filters.me)
async def reac_com(_: Client, msg: types.Message):

    try:
        limit = str(msg.text).split(' ')[1]
    except IndexError:
        await warn(msg, Client, 'Введите лимит!')
        return None

    try:
        emoji = str(msg.text).split(' ')[2]
    except IndexError:
        emoji = '👍'

    try:
        chat = str(msg.text).split(' ')[3]
    except IndexError:
        chat = None

    chat_id = msg.chat.id
    await msg.delete()
    async for m in Client.get_chat_history(chat_id, int(limit)):
        try:
            await Client.send_reaction(chat_id, m.id, emoji)
        except errors.exceptions.bad_request_400.MessageNotModified:
            pass

modules_info['reac'] = ['Send reactions to the messages!']
