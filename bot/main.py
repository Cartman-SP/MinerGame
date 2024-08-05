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

        user_id = update.message.from_user.id
        #response = requests.post(f"http://your-django-server/api/save-referral/", data={'user_id': user_id, 'referral_code': referral_code})
            keyboard = [[InlineKeyboardButton("Запустить WebApp", url=webapp_url)]]
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
