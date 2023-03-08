from pyrogram import Client, filters, types
from plugins.settings import modules_info
from config import prefix
from utils import restart


@Client.on_message(filters.command('restart', prefixes=prefix) & filters.me)
async def restart_command(_: Client, msg: types.Message):
    await msg.edit('ℹ️ <b>Restarting...</b>')
    restart()

modules_info['restart'] = ['Restart UserBot']
