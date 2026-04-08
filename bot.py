import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

# ВСТАВЬ СВОЙ ТОКЕН ОТ BOTFATHER НИЖЕ (в кавычках)
TOKEN = "8557711491:AAEqTlV4X6pA_J6hN7tVGTf4695jFsD_kS4"
# ВСТАВЬ ССЫЛКУ ОТ VERCEL НИЖЕ (в кавычках)
WEB_APP_URL = "npx plugins add vercel/vercel-plugin"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    # Те самые удобные кнопки
    кнопки = [
        [InlineKeyboardButton(text="Заказать еду 🍔", web_app=WebAppInfo(url=WEB_APP_URL))],
        [InlineKeyboardButton(text="Профиль 👤", callback_data="profile")],
        [InlineKeyboardButton(text="Наши контакты 📞", callback_data="contacts")]
    ]
    клавиатура = InlineKeyboardMarkup(inline_keyboard=кнопки)
    
    await message.answer(
        f"Привет, {message.from_user.first_name}! 👋\nМы рады видеть тебя здесь. 🍕🍔🍣\n\nПожалуйста, выбери один из пунктов:",
        reply_markup=клавиатура
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
