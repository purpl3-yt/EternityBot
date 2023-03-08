from pyrogram import Client, filters, types
from plugins.settings import modules_info
from config import prefix
from utils import warn

@Client.on_message(filters.command('del', prefixes=prefix) & filters.me)
async def del_command(_: Client, msg: types.Message):
    if msg.reply_to_message != None:
        await Client.delete_messages(_, msg.chat.id, msg.reply_to_message_id)
        await msg.delete()
    else:
        await warn(msg, Client, 'Вы должны ответить на сообщение!')

modules_info['del'] = 'Delete message'