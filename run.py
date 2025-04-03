import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from decouple import config 

from app.middlewares.keyboard import main_keyboard

BOT_TOKEN = '8006065455:AAHnCkRzXDjhkfeP_B2OCZkOPfebfIGoUhc'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_command(message: Message):
    await message.reply("Добро пожаловать!", reply_markup=main_keyboard)

async def main():
    await dp.start_polling(bot)

if __name__=='__main__':
    try:
        asyncio.run(main())
    except: KeyboardInterrupt('Bot is stopped')    
