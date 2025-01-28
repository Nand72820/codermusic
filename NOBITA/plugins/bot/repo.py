from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from NOBITA import app
from config import BOT_USERNAME
from NOBITA.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
✰ ʀᴇᴘᴏ ɪs ᴘʀɪᴠᴀᴛᴇ ʙʀᴏᴛʜᴇʀ
✰ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ʙᴜʏ ᴅᴍ
✰ || @Yo_Mysterious ||
✰ ʙᴏᴛ ʀᴜɴ ʟᴀɢ ғʀᴇᴇ ᴀɴᴅ 𝟸𝟺x𝟽
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("🍷 ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ 🍷", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("🐬 ʜᴇʟᴘ 🐬", url="https://t.me/Yo_Mysterious"),
          ],
               [
                InlineKeyboardButton("🍁 ᴛᴇᴀᴍ ɴʏ ᴄʀᴇᴀᴛɪᴏɴ 🍁", url=f"https://t.me/NYCreation_Chatzone"),
],
[
InlineKeyboardButton("🌿 ᴍᴀɪɴ ʙᴏᴛ 🌿", url=f"https://t.me/WynkMusicRobot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/2oj1vp.webp",
        caption=start_txt,
        reply_markup=reply_markup
    )
