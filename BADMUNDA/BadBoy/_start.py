import platform

from pyrogram import Client
from pyrogram import __version__ as py_version
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, Message

from BADMUNDA.Config import *

from ..core.clients import *

if START_PIC:
    START_PIC = START_PIC
else:
    START_PIC = "https://telegra.ph/file/6482940720892cb9a4479.jpg"


@Client.on_message(filters.command(["start"], prefixes=HANDLER))
async def _start(Badmunda: Client, message: Message):
    global START_MESSAGE
    my_detail = await Badmunda.get_me()
    my_mention = my_detail.mention
    if START_MESSAGE:
        START_MESSAGE = START_MESSAGE
    else:
        START_MESSAGE = (
            f"ʜᴇʏ💫 {message.from_user.mention}🌸\n"
            f"✥ ɪ ᴀᴍ {my_mention}\n\n"
            f"❖━━━━•❅•°•❈•°•❅•━━━━❖\n\n"
            f"✥ **__ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ__** = {py_version}\n"
            f"✥ **__ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ__** = {platform.python_version()}\n"
            f"✥ **__ʙᴏᴛsᴘᴀᴍ ᴠᴇʀsɪᴏɴ__** = {version}\n\n"
            f"❖━━━━•❅•°•❈•°•❅•━━━━❖"
        )

    # Define buttons
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Help", callback_data="help"),
                InlineKeyboardButton("About", callback_data="about"),
            ],
            [
                InlineKeyboardButton("Join Us", url="https://t.me/your_channel"),
            ],
        ]
    )
    
 # Check if START_PIC is valid and send the message
    if ".jpg" in START_PIC or ".png" in START_PIC:
        for i in range(1, 26):
            lol = globals().get(f"Client{i}")
            if lol is not None:
                await lol.send_photo(
                    message.chat.id,
                    START_PIC,
                    caption=START_MESSAGE,
                    reply_markup=keyboard = InlineKeyboardButton("Join Us", url="https://t.me/your_channel"), # Add the buttons here
                )
    else:
        await message.reply_text(START_MESSAGE, reply_markup=keyboard)
