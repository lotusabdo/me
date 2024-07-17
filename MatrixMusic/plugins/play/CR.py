import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from MatrixMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from MatrixMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","★السورس★"])
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/30cf70b0716df18ddc950.jpg",
        caption=f"""\nمرحبا بك عزيزي {message.from_user.mention} في قسم سورس ميوزك\nللتحدث مع مطور السورس اضغط علي الازرار بالاسفل👇""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙶𝚁𝙾̀𝚄𝙿", url=f"https://t.me/as_o1"), 
                 InlineKeyboardButton(
                   " 𝙎𝙤𝙪𝙧𝙘𝙚 𝘼𝙡 𝙕𝙤𝙯",       url=f"https://t.me/Y_S_O0"), 
                 
             ],[ 
            InlineKeyboardButton(
                        "💴 زيَٰـُـٰٓـآدـ⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠ 𝗩𝗜𝗣׀𝑨𝑳𝒁𝑶𝒁ـ⁠⁠⁠⁠⁠⁠⁠", url=f"https://t.me/G_O_Z_L"), 
                 
                ],

            ]

        ),

    )








@app.on_message(
    command(["مطور السورس","★مطور السورس★","مبرمج"])
    
    
)
async def yas(client, message):
    usr = await client.get_chat("G_O_Z_L")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"𓏺 َِՏΌႮᎡᏟᎬ ᎡᎥΝΌ \n\n‍ ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\nՏΌႮᎡᏟᎬ ᎡᎥΝΌ", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["الزوز"])
    
    
)
async def yas(client, message):
    usr = await client.get_chat("G_O_Z_L")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"𓏺 َِՏΌႮᎡᏟᎬ ᎡᎥΝΌ .\n\n¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\nՏΌႮᎡᏟᎬ ᎡᎥΝΌ", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )



