from pyrogram import Client, filters, types
from config import prefix
from plugins.settings import modules_info

@Client.on_message(filters.command('help', prefixes=prefix) & filters.me)
async def help_command(_: Client, msg: types.Message):
    try:cmd = str(msg.text).split(' ')[1]
    except IndexError:
        help_text = '''
<b>EternityBot Modules: </b>

'''

        for cmd in list(modules_info.keys()):
            help_text+='⚙️  '+'<code>'+prefix+f'{cmd}</code>\n'

        await msg.edit(help_text)
        
    else:
        if cmd.startswith(prefix):
            cmd_info = cmd[1:]
        else:cmd_info = cmd

        await msg.edit(f'''
🔧 Command: <code>{cmd}</code> - <b>{cmd_info}</b>''')