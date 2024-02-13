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
    command(["سورس"])
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/0395107f7b3d1e6ddda9f.jpg",
        caption=f"""\nمرحبا بك عزيزي {message.from_user.mention} في قسم سورس ميوزك\nللتحدث مع مطور السورس اضغط علي الازرار بالاسفل👇""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙶𝚁𝙾̀𝚄𝙿", url=f"https://t.me/Q1_QU"), 
                 InlineKeyboardButton(
                   " ՏΌႮᎡᏟᎬ ᎡᎥΝΌ",       url=f"https://t.me/I1_35"), 
                 
             ],[ 
            InlineKeyboardButton(
                        "ألموع ـلم مـ ــيــ ــدؤ ســ ـــنــ ــدأل >3`", url=f"https://t.me/EU_ET"), 
                 
                ],

            ]

        ),

    )








@app.on_message(
    command(["مطور السورس","المبرمج","مبرمج"])
    
    
)
async def yas(client, message):
    usr = await client.get_chat("EU_ET")
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
    command(["ميدو"])
    
    
)
async def yas(client, message):
    usr = await client.get_chat("EU_ET")
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



