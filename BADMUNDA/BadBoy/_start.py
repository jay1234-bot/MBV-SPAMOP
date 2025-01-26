import platform

from pyrogram import Client
from pyrogram import __version__ as py_version
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from BADMUNDA.Config import *

from ..core.clients import *

# Define START_PIC
if START_PIC:
    START_PIC = START_PIC
else:
    START_PIC = "https://telegra.ph/file/6482940720892cb9a4479.jpg"


@Client.on_message(filters.command(["start"], prefixes=HANDLER))
async def _start(Badmunda: Client, message: Message):
    global START_MESSAGE

    # Fetch bot details
    my_detail = await Badmunda.get_me()
    my_mention = my_detail.mention

    # Define START_MESSAGE if not already defined
    if START_MESSAGE:
        START_MESSAGE = START_MESSAGE
    else:
        START_MESSAGE = (
            f"ʜᴇʏ💫 {message.from_user.mention}🌸\n"
            f"✥ ɪ ᴀᴍ {my_mention}\n\n"
            f"❖━━━━•❅•°•❈•°•❅•━━━━❖\n\n"
            f"✥ **__ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ__** = {py_version}\n"
            f"✥ **__ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ__** = {platform.python_version()}\n"
            f"❖━━━━•❅•°•❈•°•❅•━━━━❖"
        )

    # Buttons
    buttons = [
        [
            InlineKeyboardButton("♥ SUPPORT ♥", url="https://t.me/APNII_YAARI"),  # Replace with a valid URL
            InlineKeyboardButton("🎀 𝒟𝐸𝒱𝐸𝐿🌺𝒫𝐸𝑅 🎀", url="https://t.me/censored_politicsss"),  # Replace with a valid URL
        ]
    ]

    # Send the start message with photo and buttons
    if ".jpg" in START_PIC or ".png" in START_PIC:
        await Badmunda.send_photo(
            chat_id=message.chat.id,
            photo=START_PIC,
            caption=START_MESSAGE,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    else:
        await Badmunda.send_message(
            chat_id=message.chat.id,
            text=START_MESSAGE,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
