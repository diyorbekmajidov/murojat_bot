from telegram import ReplyKeyboardMarkup, Update,Bot
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
    CallbackQueryHandler,
)

import handlers

TOKEN = f'6111650437:AAG7tY93uFLFSlyDZKUuvImQh-mXI42L9K0'
updater = Updater(TOKEN)

dp = updater.dispatcher

dp.add_handler(CommandHandler("start", handlers.start))
dp.add_handler(MessageHandler(Filters.text("Ro'yhatdan o'tish"), handlers.last_name))

dp.add_handler(MessageHandler(Filters.text("Murojaat qilish"), handlers.query_user))
dp.add_handler(MessageHandler(Filters.text, handlers.auth))
   

updater.start_polling()
updater.idle()
