import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

# Твой токен и ссылка (проверь, чтобы не было лишних пробелов)
TOKEN = "8557711491:AAEqTlV4X6pA_J6hN7tVGTf4695jFsD_kS4"
WEB_APP_URL = "https://tamakkgapp.vercel.app/"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    buttons = [
        [InlineKeyboardButton(text="Заказать еду 🍔", web_app=WebAppInfo(url=WEB_APP_URL))],
        [InlineKeyboardButton(text="Профиль 👤", callback_data="profile")],
        [InlineKeyboardButton(text="Наши контакты 📞", callback_data="contacts")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    
    await message.answer(
        f"Привет, {message.from_user.first_name}! 👋\nМы рады видеть тебя здесь. 🍕🍔🍣\n\nПожалуйста, выбери один из пунктов:",
        reply_markup=keyboard
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
