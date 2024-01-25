import logging

from pyrogram import Client, filters
from pyrogram.types import Message,InlineKeyboardButton,InlineKeyboardMarkup
from pyrogram.enums import ParseMode

from config import (
    API_ID,
    API_HASH,
    BOT_TOKEN,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

app = Client(name="bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


reply_button = InlineKeyboardMarkup( 
                                 [ 
                                     [InlineKeyboardButton("👨‍💻 Developer", url="https://t.me/primeakash"), InlineKeyboardButton('📁 Source Code',url="https://github.com/botsgalaxy/telegram-file-id-bot")]
                                 ]
                             )


@app.on_message(filters.private & filters.command("start"))
async def start_handler(client: Client, message: Message):
    await message.reply_text("__🌱 I am alive.__\n\n**Made with ♥️ by 𝐏𝐫𝐢𝐦𝐞 𝐀𝐤𝐚𝐬𝐡 🇧🇩**", 
                             reply_markup= reply_button)


@app.on_message(filters.forwarded & filters.media)
async def media_id_handler(client, message: Message):
    media = getattr(message, message.media.value)
    await message.reply_text(
        f"<code> {media.file_id} </code>", parse_mode=ParseMode.HTML, quote=True
    )

@app.on_message()
async def all_message_handler(client:Client,message:Message):
    await message.reply_text("__✉️ To obtain a persistent file_id, please forward the media message from the desired chat to this bot. Sending the media directly to this chat will result in a file_id that only works within the context of this bot. If you have any further questions or need assistance, feel free to ask! 👍__",quote=True, reply_markup=reply_button)



app.run()
