from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext
import requests
import os

# Получите токен вашего бота от BotFather
TOKEN = '6705532890:AAG7x2iBNy9GdCLZWqqNF1LunZtev7_yOmA'

async def start(update: Update, context: CallbackContext) -> None:
    # Получите параметр startapp из команды
    args = context.args
    if args:
        referral_code = args[0]

        # Генерация ссылки для запуска WebApp с реферальным кодом
        webapp_url = f"https://your-webapp.com/?referral={referral_code}"
        
        # Сохранение реферального кода на сервере
        user_id = update.message.from_user.id
        response = requests.post(f"http://your-django-server/api/save-referral/", data={'user_id': user_id, 'referral_code': referral_code})
        
        # Отправьте пользователю ответное сообщение
        if response.status_code == 200:
            keyboard = [[InlineKeyboardButton("Запустить WebApp", url=webapp_url)]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await update.message.reply_text(f"Привет! Вы используете реферальный код: {referral_code}.", reply_markup=reply_markup)
        else:
            await update.message.reply_text("Произошла ошибка при сохранении реферального кода.")

def main() -> None:
    """Start the bot."""
    application = Application.builder().token(TOKEN).build()
    
    # Зарегистрируйте обработчик команды /start
    application.add_handler(CommandHandler("start", start))
    
    # Запустите бота
    application.run_polling()

if __name__ == '__main__':
    main()
