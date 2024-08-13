from aiogram import Router, F, Bot, types
from aiogram.filters import Command
from aiogram.types import Message, PreCheckoutQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import Dispatcher
import asyncio
import logging
from aiogram import Router, F, Bot, types
from aiogram.filters import Command
from aiogram.types import Message, PreCheckoutQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import Dispatcher
import asyncio
import logging
import mysql.connector

# Конфигурация
API_TOKEN = '7079394719:AAHWyslDgeCfWSYnrJ9VvCZDOP5jt9qAeJM'
AUTHORIZED_USER_ID = 5881427442  # ID пользователя, который имеет право на рассылку

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
router = Router()
logging.basicConfig(level=logging.INFO)

# Словарь для хранения состояния активных рассылок
active_broadcasts = {}

# Объект бота
bot = Bot(token='7079394719:AAHWyslDgeCfWSYnrJ9VvCZDOP5jt9qAeJM')
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
        'uk': 'https://t.me/+RXe8EdjeWp9iODdi',
        'ru': 'https://t.me/+cPskObB_bTNjOTgy',
        'uz': 'https://t.me/+nY5ngmDOlmQ4OGVi',
        'ka': 'https://t.me/+VNNjtXc9379mMWYy',
        'en': 'https://t.me/+iyTLN7PksNVmYmJi',
        'hy': 'https://t.me/+V4CWk93cC89lNzgy',
        'kk': 'https://t.me/+ZIysQ0YFahI5Mzli',
        'es': 'https://t.me/+vpP9oiulLqE3ODgy',
        'tr': 'https://t.me/+rRdKUd7i9U5lYzcy',
        'hi': 'https://t.me/+U07GlOiVClZkZDRi'
    }
    url = chats_url.get(user_language, chats_url['en'])  # Значение по умолчанию

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

# Обработка команды /send
@router.message(Command("send"))
async def send_command_handler(message: Message):
    if message.from_user.id != AUTHORIZED_USER_ID:
        await message.answer("У вас нет прав для выполнения этой команды.")
        return

    # Запрашиваем текст сообщения для рассылки
    await message.answer("Введите ваше сообщение для рассылки:")

    # Сохраняем состояние активной рассылки
    active_broadcasts[message.from_user.id] = {'status': 'awaiting_message'}

# Обработка текстовых сообщений (после команды /send)
@router.message()
async def handle_broadcast_message(message: Message):
    if message.from_user.id not in active_broadcasts or active_broadcasts[message.from_user.id]['status'] != 'awaiting_message':
        return

    broadcast_message = message.text
    await message.answer("Рассылка начата.")

    # Получаем список всех пользователей с доступом из базы данных
    users_with_access = await get_users_with_access()

    # Отправляем сообщение всем пользователям
    for user_id in users_with_access:
        try:
            await bot.send_message(user_id, broadcast_message)
        except Exception as e:
            logging.error(f"Ошибка при отправке сообщения пользователю {user_id}: {e}")

    # Завершаем активную рассылку
    del active_broadcasts[message.from_user.id]

# Асинхронная функция для получения пользователей с доступом из базы данных
async def get_users_with_access():
    try:
        connection = mysql.connector.connect(
            user='django',
            password='zY7S1iof7dw&',
            host='localhost',
            database='mydatabase'
        )
        cursor = connection.cursor()
        cursor.execute("SELECT user_id FROM mainapp_telegramuser")
        users = cursor.fetchall()
        cursor.close()
        connection.close()
        return [user_id[0] for user_id in users]
    except mysql.connector.Error as err:
        logging.error(f"Ошибка подключения к базе данных: {err}")
        return []

async def main():
    # Регистрация обработчиков
    dp.include_router(router)

    # Запуск поллинга
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main(), debug=True)