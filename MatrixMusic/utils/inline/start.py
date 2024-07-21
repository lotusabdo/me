from pyrogram.types import InlineKeyboardButton

import config
from MatrixMusic import app

def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك✅", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text="𝐆𝐑𝐎𝐔𝐏", url= "https://t.me/as_o1"),
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
        
        [
            InlineKeyboardButton(text="مٓ ـطؤر آلسؤرس", url= "https://t.me/G_O_Z_L"),
            InlineKeyboardButton(text="𝐆𝐑𝐎𝐔𝐏", url=f"https://t.me/as_o1"), 
        ],
        [
            
            InlineKeyboardButton(text="𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url=f"https://t.me/I1_35") , 
        ],
    ]
    return buttons
