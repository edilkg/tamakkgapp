import asyncio
import os
from aiohttp import web
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

# Данные
TOKEN = "8557711491:AAEqT1V4X6pA_J6hN7tVGTf4695jfSD_kS4"
WEB_APP_URL = "https://tamakkgapp.vercel.app/"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Команда /start
@dp.message(CommandStart())
async def start(message: types.Message):
    buttons = [
        [InlineKeyboardButton(text="Заказать еду 🍔", web_app=WebAppInfo(url=WEB_APP_URL))],
        [InlineKeyboardButton(text="Заказать доставку 🚀", web_app=WebAppInfo(url=WEB_APP_URL))],
        [InlineKeyboardButton(text="Профиль 👤", callback_data="profile")],
        [InlineKeyboardButton(text="Наши контакты 📞", callback_data="contacts")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    await message.answer(f"Привет, {message.from_user.first_name}! 👋\nВыбери пункт меню:", reply_markup=keyboard)

# Мини-веб-сервер для Render
async def handle(request):
    return web.Response(text="Bot is running!")

async def main():
    # Запускаем веб-сервер на порту, который даст Render
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", int(os.getenv("PORT", 8080)))
    
    # Запускаем сервер и бота одновременно
    await asyncio.gather(
        site.start(),
        dp.start_polling(bot)
    )

if __name__ == "__main__":
    asyncio.run(main())
