from pyrogram.types import InlineKeyboardButton

import config
from MatrixMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك✅", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text="𝙶𝚁𝙾̀𝚄𝙿", url= "https://t.me/Q1_QU"),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك✅",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="اوامــــر الـــبـــوت📚", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="مطور البوت", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="𝙶𝚁𝙾̀𝚄𝙿", url=f"https://t.me/Q1_QU"), 
        ],
        [
            InlineKeyboardButton(text="مطور السورس", url=f"https://t.me/EU_ET"), 
            InlineKeyboardButton(text="𝚂́𝙾𝚄𝚁𝙲𝙴 𝚁𝙸𝙽𝙾", url=f"https://t.me/I1_35") , 
        ],
    ]
    return buttons
