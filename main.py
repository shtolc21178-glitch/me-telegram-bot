import asyncio
from aiogram import Bot, Dispatcher, types
import yt_dlp
import os
TOKEN = os.getenv("TOKEN")  # беремо токен із Variables


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def download_video(message: types.Message):
    url = message.text.strip()
    if url.startswith("http"):
        await message.reply("⏳ Завантажую відео...")
        ydl_opts = {"outtmpl": "video.mp4"}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        await message.reply_video(open("video.mp4", "rb"))

async def main():
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())
