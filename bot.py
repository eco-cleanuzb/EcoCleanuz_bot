import logging
import asyncio
from aiogram import Bot, Dispatcher, types

TOKEN = "7508960084:AAG1crsAryR6p01x0ZnNU18GYirGd-XRDnE"  # Shu yerga tokeningizni qo'ying

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Start komandasi
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer("Assalomu alaykum! 'Eco Clean Uzbekistan' botiga xush kelibsiz! Xizmatlarimiz bilan tanishing:")

# Xizmatlar ro‘yxati
@dp.message_handler(commands=["services"])
async def services_command(message: types.Message):
    text = "📌 Bizning xizmatlar:\n\n"
    text += "✅ Uy tozalash - 30$\n"
    text += "✅ Ofis tozalash - 50$\n"
    text += "✅ Deraza yuvish - 5$\n\n"
    text += "Buyurtma berish uchun biz bilan bog‘laning: @admin_username"
    await message.answer(text)

# Buyurtma berish
@dp.message_handler(commands=["order"])
async def order_command(message: types.Message):
    await message.answer("Buyurtma berish uchun telefon raqamingizni va manzilingizni yuboring.")

# Ishga tushirish
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
