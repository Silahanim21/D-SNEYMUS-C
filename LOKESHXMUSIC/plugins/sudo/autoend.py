from pyrogram import filters
from pyrogram.types import Message

from LOKESHXMUSIC import app
from LOKESHXMUSIC.misc import SUDOERS
from LOKESHXMUSIC.utils.database import autoend_off, autoend_on


@app.on_message(filters.command("autoend") & SUDOERS)
async def auto_end_stream(_, message: Message):
    usage = "KULLANICI :</b>\n\n/autoend [ᴇɴᴀʙʟᴇ | ᴅɪsᴀʙʟᴇ]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip().lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "» akışı otomatik sonlandır etkin.\n asistan irade otomatik olarak ayrılmak birkaç dakika sonra kimse dinlemediğinde görüntülü sohbet ."
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("» akışı otomatik sonlandır engelli .")
    else:
        await message.reply_text(usage)
