from pyrogram import idle
from pyrogram import Client as Bot
from Shizy.Modules.cache.clientbot import run
from Shizy.config import API_ID, API_HASH, BOT_TOKEN

    
bot = Bot(
    ":Shizy:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Shizy/Plugins")
)

bot.start()
run()
idle()
