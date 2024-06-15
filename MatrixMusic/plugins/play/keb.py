import asyncio
from pyrogram import Client, filters
from random import choice
from pyrogram import filters
from config import BANNED_USERS
from MatrixMusic import (Apple, Resso, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, Message, ChatJoinRequest


@app.on_message(filters.regex("^/Medo"), group=39)
async def cpanel(_, message: Message):             
        text = "🧑🏻‍✈️︙اهلا بك بك عزيزي العضو ♥️\n\n اليـكـ كيب الاعضاء الخاص بسورس ميدو"
        kep = ReplyKeyboardMarkup([
["المطور ", "مطور السورس"],
["صراحه","سورس"],
["كت"],
["قران","انمي"],
["غنيلي", "افاتار بنات"],
["متحركه","اذكار"],
["افاتار شباب"],
["نقشبندي","لو خيروك"],
["صوره","بوت"],
["الاوامر","تلاوات"],
["❎ ¦ حذف الكيبورد"]], resize_keyboard=True)
        await message.reply(
              text=text,
               reply_markup=kep,quote=True)

@app.on_message(filters.command(["❎ ¦ حذف الكيبورد"], ""))
async def upbkgt(client: Client, message: Message):
    await message.reply_text(
        text="""❎ ¦ تم حذف الكيبورد بنجاح""",
        reply_markup=ReplyKeyboardRemove()
    )

@app.on_message(filters.command(["❎ ¦ حذف الكيبورد"], ""))
async def upbkgt(client: Client, message: Message):
    await message.reply_text(
        text="""❎ ¦ تم حذف الكيبورد بنجاح""",
        reply_markup=ReplyKeyboardRemove()
    )

