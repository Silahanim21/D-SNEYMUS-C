from pyrogram import filters
from pyrogram.types import Message
from unidecode import unidecode

from LOKESHXMUSIC import app
from LOKESHXMUSIC.misc import SUDOERS
from LOKESHXMUSIC.utils.database import (
    get_active_chats,
    get_active_video_chats,
    remove_active_chat,
    remove_active_video_chat,
)


@app.on_message(filters.command(["aktifses", "aktifsesli"]) & SUDOERS)
async def activevc(_, message: Message):
    mystic = await message.reply_text("👉 AKTİF SESLİ SOHBETLER ALINMA LISTESI...")
    served_chats = await get_active_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except:
            await remove_active_chat(x)
            continue
        try:
            if (await app.get_chat(x)).username:
                user = (await app.get_chat(x)).username
                text += f"<b>{j + 1}.</b> <a href=https://t.me/{user}>{unidecode(title).upper()}</a> [<code>{x}</code>]\n"
            else:
                text += (
                    f"<b>{j + 1}.</b> {unidecode(title).upper()} [<code>{x}</code>]\n"
                )
            j += 1
        except:
            continue
    if not text:
        await mystic.edit_text(f" 👉 AKTİF SESLİ SOHBET YOK  {app.mention}.")
    else:
        await mystic.edit_text(
           f"<b> 👉ŞU ANDA AKTİF SESLİ SOHBETLERİN LİSTESİ  :</b>\n\n{text}",
            disable_web_page_preview=True,
        )


@app.on_message(filters.command(["aktifvideo", "akdivvide"]) & SUDOERS)
async def activevi_(_, message: Message):
    mystic = await message.reply_text("👉 AKTİF GÖRÜNTÜLÜ SOHBET LİSTESİ ALINMA..")
    served_chats = await get_active_video_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except:
            await remove_active_video_chat(x)
            continue
        try:
            if (await app.get_chat(x)).username:
                user = (await app.get_chat(x)).username
                text += f"<b>{j + 1}.</b> <a href=https://t.me/{user}>{unidecode(title).upper()}</a> [<code>{x}</code>]\n"
            else:
                text += (
                    f"<b>{j + 1}.</b> {unidecode(title).upper()} [<code>{x}</code>]\n"
                )
            j += 1
        except:
            continue
    if not text:
        await mystic.edit_text(f"👉 AKTİF GÖRÜNTÜLÜ SOHBET YOK  {app.mention}.")
    else:
        await mystic.edit_text(
          f"<b>»ŞU ANDA AKTİF GÖRÜNTÜLÜ SOHBETLERİN LİSTESİ :</b>\n\n{text}",
            disable_web_page_preview=True,
        )
