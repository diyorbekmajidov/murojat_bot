from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, MessageHandler, Filters, CommandHandler
from settings import TOKEN, URL

from handlers import (
    start,
    last_name,
    auth,
    query_user,
)

app = Flask(__name__)

bot = Bot(TOKEN)

@app.route('/', methods=['POST'])
def index():
    dp = Dispatcher(bot, None, workers=0)

    data = request.get_json(force=True)
    update = Update.de_json(data, bot)

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text("Ro'yhatdan o'tish"), last_name))

    dp.add_handler(MessageHandler(Filters.text("Murojaat qilish"), query_user))
    dp.add_handler(MessageHandler(Filters.text, auth))

    dp.process_update(update)
    return 'ok'


@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.set_webhook(URL)
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"
    

@app.route('/deletewebhook', methods=['GET', 'POST'])
def delete_webhook():
    s = bot.delete_webhook()
    if s:
        return "webhook delete ok"
    else:
        return "webhook delete failed"
