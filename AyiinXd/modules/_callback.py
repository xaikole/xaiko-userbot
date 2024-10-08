import random
import re
from telethon import Button, events
from telethon.tl.types import InputWebDocument

from config import var
from AyiinXd import Ayiin, bot, ibuild_keyboard, paginate_help

BTN_URL_REGEX = re.compile(r"(\[([^\[]+?)\]\<buttonurl:(?:/{0,2})(.+?)(:same)?\>)")
dugmeler = var.CMD_HELP
logoyins = random.choice([
    "https://telegra.ph/file/9f8e73d387f25b7f27ce5.jpg",
    "https://telegra.ph/file/c935d34b48e45fba22b03.jpg",
    "https://telegra.ph/file/392f69c8717c91b1e8a3b.jpg",
    "https://telegra.ph/file/4c5b756dd13d7a88c866b.jpg",
])

main_help_button = [
    [Button.inline("•• Pʟᴜɢɪɴ ••", data="reopen"), Button.inline("Mᴇɴᴜ Vᴄ ••", data="inline_yins")],
    [Button.inline("⚙️ Aʟᴀᴛ Pᴇᴍɪʟɪᴋ", data="yins_langs"), Button.url("Pᴇɴɢᴀᴛᴜʀᴀɴ ⚙️", url=f"t.me/{var.BOT_USERNAME}?start=")],
    [Button.inline("•• Kᴇᴍʙᴀʟɪ ••", data="close")]
]

@bot.on(events.callbackquery.CallbackQuery(data=re.compile(rb"reopen")))
async def on_plug_in_callback_query_handler(event):
    user = await Ayiin.get_me()
    uid = user.id
    owner = user.first_name
    if event.query.user_id == uid or event.query.user_id in var.SUDO_USERS:
        buttons = paginate_help(0, dugmeler, "helpme")
        text = f"**✨ ᴀʏɪɪɴ-ᴜsᴇʀʙᴏᴛ ɪɴʟɪɴᴇ ᴍᴇɴᴜ ✨**\n\n⍟ **ᴅᴇᴘʟᴏʏ :** •[{var.HOSTED_ON}]•\n⍟ **ᴏᴡɴᴇʀ** {owner}\n⍟ **ᴊᴜᴍʟᴀʜ :** {len(dugmeler)} **Modules**"
        await event.edit(text, file=logoyins, buttons=buttons, link_preview=False)
    else:
        await event.answer(f"Kamu Tidak diizinkan, ini Userbot Milik {owner}", cache_time=0, alert=True)

@bot.on(events.InlineQuery)
async def inline_handler(event):
    query = event.text
    user = await Ayiin.get_me()
    uid = user.id
    botusername = (await event.client.get_me()).username

    if event.query.user_id == uid and query.startswith("@AyiinChats"):
        buttons = paginate_help(0, dugmeler, "helpme")
        result = event.builder.photo(
            file=logoyins,
            link_preview=False,
            text=f"**✨ ᴀʏɪɪɴ-ᴜsᴇʀʙᴏᴛ ɪɴʟɪɴᴇ ᴍᴇɴᴜ ✨**\n\n⍟ **ᴅᴇᴘʟᴏʏ :** •[{var.HOSTED_ON}]•\n⍟ **ᴏᴡɴᴇʀ :** {user.first_name}\n⍟ **ᴊᴜᴍʟᴀʜ :** {len(dugmeler)} **Modules**",
            buttons=main_help_button
        )
        await event.answer([result], switch_pm="👥 USERBOT PORTAL", switch_pm_param="start")

@bot.on(events.CallbackQuery(data=re.compile(rb"helpme_next\((.+?)\)")))
async def on_help_next_handler(event):
    user = await Ayiin.get_me()
    uid = user.id
    if event.query.user_id == uid or event.query.user_id in var.SUDO_USERS:
        current_page = int(event.data_match.group(1).decode("UTF-8"))
        buttons = paginate_help(current_page + 1, dugmeler, "helpme")
        await event.edit(buttons=buttons)

@bot.on(events.CallbackQuery(data=re.compile(rb"helpme_close\((.+?)\)")))
async def on_help_close_handler(event):
    user = await Ayiin.get_me()
    uid = user.id
    if event.query.user_id == uid or event.query.user_id in var.SUDO_USERS:
        await event.edit(file=logoyins, link_preview=True, buttons=main_help_button)

@bot.on(events.CallbackQuery(data=b"inline_yins"))
async def about_handler(event):
    user = await Ayiin.get_me()
    uid = user.id
    if event.query.user_id == uid or event.query.user_id in var.SUDO_USERS:
        await event.edit(
            f"•Menu• - Voice chat group untuk [{user.first_name}](tg://user?id={uid})",
            buttons=[
                [Button.inline("⍟ ᴠᴄ ᴘʟᴜɢɪɴ ⍟", data="vcplugin"), Button.inline("⍟ ᴠᴄ ᴛᴏᴏʟs ⍟", data="vctools")],
                [Button.inline("ʙᴀᴄᴋ", data="gcback")]
            ]
        )
    else:
        await event.answer("❌ DISCLAIMER ❌\n\nAnda Tidak Mempunyai Hak Untuk Menekan Tombol Button Ini", cache_time=0, alert=True)
