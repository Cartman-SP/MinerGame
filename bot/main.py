from aiogram import Router, F, Bot, types
from aiogram.filters import Command
from aiogram.types import Message, PreCheckoutQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import Dispatcher
import asyncio
import logging

# Объект бота
bot = Bot(token='7233799288:AAF0WYqgm5H0pgL5t66nip78HQfBHxF8ThA')
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)
router = Router()

@dp.pre_checkout_query()
async def checkout_handler(checkout_query: PreCheckoutQuery):
    await checkout_query.answer(ok=True)

@dp.message(F.successful_payment)
async def star_payment(msg: Message, bot: Bot):
    await msg.answer(f"Id транзакции: {msg.successful_payment.telegram_payment_charge_id}")

@router.message(Command("start"))
async def start_command_handler(message: Message):
    user_language = message.from_user.language_code
    chats_url = {
        'uk':  'https://t.me/+RXe8EdjeWp9iODdi',
        'ru':  'https://t.me/+cPskObB_bTNjOTgy',
        'uz':  'https://t.me/+nY5ngmDOlmQ4OGVi'
        'ka'  'https://t.me/+VNNjtXc9379mMWYy'
        'en'  'https://t.me/+iyTLN7PksNVmYmJi'
        'hy'  'https://t.me/+V4CWk93cC89lNzgy'
        'kk'  'https://t.me/+ZIysQ0YFahI5Mzli'
        'es'  'https://t.me/+vpP9oiulLqE3ODgy'
        'tr'  'https://t.me/+rRdKUd7i9U5lYzcy'
        'hi'  'https://t.me/+U07GlOiVClZkZDRi'
    }
    url = chats_url[user_language]
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Открыть Игру 🎮", url="https://t.me/ylionminerbot/ylionminer")],
        [InlineKeyboardButton(text="Подписаться на Канал 🔔", url="https://t.me/ylionminer")],
        [InlineKeyboardButton(text="Присоединиться к Чату 📥", url=url)],
        [InlineKeyboardButton(text="Поддержка 👨🏻‍💻", url="https://t.me/supylionbot")],
    ])

    # Отправляем приветственное сообщение с клавиатурой
    await message.answer(
        "Добро пожаловать в YLION MINER! Теперь вы — обладатель своей собственной майнинг фермы.\n\n"
        "Качайте видеокарты, чтобы увеличивать производительность и поднимать прибыль. "
        "Оптимизируйте свои стратегии и участвуйте в увлекательных заданиях.",
        reply_markup=keyboard
    )

async def main():
    # Регистрация обработчиков
    dp.include_router(router)

    # Запуск поллинга
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main(), debug=True)
