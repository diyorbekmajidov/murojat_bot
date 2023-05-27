from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ParseMode,
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    Update,
)
from telegram.ext import (
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
    Dispatcher
)
from db import DB
db = DB('db.json')


def start(update: Update, context: CallbackContext):
    print('hi')
    first_name = update.message.from_user.first_name
    bot = context.bot
    chat_id = update.message.chat_id

    
    button = [  
        [ 'Murojaat qilish' ],
        [ "Ro'yhatdan o'tish" ]
    ]
    reply_markup = ReplyKeyboardMarkup(button, resize_keyboard=True)
    text = f"Assalomu alaykum {first_name}!\n\n"
    bot.send_message(chat_id=chat_id, text=text, reply_markup=reply_markup)
# user phone number

def last_name(update: Update, context: CallbackContext):
    bot = context.bot
    chat_id = update.message.chat_id
    username = update.message.from_user.username
    if db.get_user(chat_id) == None:
            
        db.add_user(chat_id,username)

        text = "Iltimos, ismingizni kiriting\n\n Masalan: Azizbek Jaliov"
        bot.send_message(chat_id=chat_id, text=text)
    else:
        text = "Siz allaqachon ro'yhatdan o'tgansiz!"
        bot.send_message(chat_id=chat_id, text=text)

def auth( update: Update, context: CallbackContext):
    bot = context.bot
    chat_id = update.message.chat_id
    admin_chat_id = 2057764615
    user =  db.get_user(chat_id)
    if user["first_name"]==None:
        db.update_user(chat_id, update.message.text)
        text = "Iltimos, telefon raqamingizni kiriting\n\n Masalan: +998 99 999 99 99"
        bot.send_message(chat_id=chat_id, text=text)

    elif user["phone_number"]==None:
        db.update_user(chat_id, phone_number=update.message.text)
        text = "Muaffaqiyatli ro'yhatdan o'tdingiz!"
        bot.send_message(chat_id=chat_id, text=text)

    else :
        text = update.message.text
        user =db.get_user(chat_id)
        username = user['username']
        first_name = user['first_name']
        phone_number = user['phone_number']

        text = f"Yangi murojaat yozing \n\n"
        bot.send_message(chat_id, text=text)
        text = f"Username: @{username}\n First name: {first_name}\n Phone number: {phone_number}\n\n Murojaat: {update.message.text}"
        bot.send_message(admin_chat_id, text=text)

def query_user(update: Update, context: CallbackContext):
    bot = context.bot
    # chat_id = update.message.chat_id
    chat_id = update.effective_chat.id
    user =  db.get_user(chat_id)
    if user:
        text = f"Assalomu alaykum {user['first_name']}!\n\n"
        text += f"Murojaatingizni yozing"
        bot.send_message(chat_id=chat_id, text=text)
    else:
        text = "Iltimos, ro'yhatdan o'ting\n\n"
        bot.send_message(chat_id=chat_id, text=text)

