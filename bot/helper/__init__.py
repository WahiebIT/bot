from pyrogram import Client, filters

from decouple import config

api = 19
hash = "af0b19d19"
bot = "521:AAGT1m2nXVNB-rPoEgJe0Q8T0"
owner = "675889933"
group = "-619312469"
block = "1 2"
try:
    api = config("api", cast=int)
    hash = config("hash")
    bot = config("bot")
    owner = str(config("owner", default="1 2")).split()
    group = config("group")

    block = str(config("Block", default="1 2")).split()
except:
    print("error config")
app = Client("bot", api_id=api, api_hash=hash, bot_token=bot)
download_dir = "download"
codec_dir = "codec"
