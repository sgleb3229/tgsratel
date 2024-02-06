import asyncio
from pyrogram import Client, filters
  
api_id = 6
api_hash = 'eb06d4abfb49dc3eeb1aeb98ae0f581e'
app = Client("my_account", api_id=api_id, api_hash=api_hash)

print("TGsratel by @Vlk151")
meesage = input("сообщение: ")
chat_id = input("ид чата: ")
print("Введите в любом чате sratel start, чтобы насрать")

@app.on_message(filters.command("start", prefixes="sratel ") & filters.me)
def status(_, msg):
    while 2 > 1:
        app.send_message(chat_id, meesage)
   
app.run()