import asyncio
import os
from aiohttp import web
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

# МЫ ОЧИЩАЕМ ТОКЕН ОТ ЛИШНИХ ПРОБЕЛОВ ПРЯМО В КОДЕ
RAW_TOKEN = "8557711491:AAEqTlV4X6pA_J6hN7tVGTf4695jFsD_kS4"
TOKEN = RAW_TOKEN.strip() 
WEB_APP_URL = "https://tamakkgapp.vercel.app/"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    buttons = [
        [InlineKeyboardButton(text="Заказать еду 🍔", web_app=WebAppInfo(url=WEB_APP_URL))],
        [InlineKeyboardButton(text="Заказать доставку 🚀", web_app=WebAppInfo(url=WEB_APP_URL))],
        [InlineKeyboardButton(text="Профиль 👤", callback_data="profile")],
        [InlineKeyboardButton(text="Наши контакты 📞", callback_data="contacts")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    await message.answer(f"Привет! 👋\nВыбери пункт меню:", reply_markup=keyboard)

async def handle(request):
    return web.Response(text="Bot is active")

async def main():
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.getenv("PORT", 8080))
    site = web.TCPSite(runner, "0.0.0.0", port)
    
    await asyncio.gather(site.start(), dp.start_polling(bot))

if __name__ == "__main__":
    asyncio.run(main())
