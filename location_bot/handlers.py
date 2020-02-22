from telegram import Update, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import CallbackContext

from .loger import log_error
from location_bot.geopy_func import get_location_info

# BUTTONS -----------------------------------------------------
button_help = 'Help'
button_location = 'Location'
button_2_1 = 'Current'
button_2_2 = 'Forecast'
button_3_1 = 'Back'

# KEYBOARDS ---------------------------------------------------
KB_START = [
    [
        KeyboardButton(text=button_help),
        KeyboardButton(text=button_location, request_location=True)
    ],
]

KB_WEATHER = [
    [
        KeyboardButton(text=button_2_1),
        KeyboardButton(text=button_2_2)
    ],
    [
        KeyboardButton(text=button_3_1)
    ],
]

# MARKUPS -----------------------------------------------------
MRK_START = ReplyKeyboardMarkup(
    keyboard=KB_START,
    resize_keyboard=True,
)
MRK_WEATHER = ReplyKeyboardMarkup(
    keyboard=KB_WEATHER,
    resize_keyboard=True,
)


# HANDLERS ----------------------------------------------------
def start_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text="Здравия желаю.",
        reply_markup=MRK_START
    )


def button_help_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text="А геолокацией поделиться не желаете?",
        reply_markup=MRK_START
    )


def other_message_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text="Шо приуныли касатики?",
        reply_markup=MRK_START
    )


def location_message_handler(update: Update, context: CallbackContext):
    message = None
    if update.edited_message:
        message = update.edited_message
    else:
        message = update.message
    current_pos = (message.location.latitude, message.location.longitude)
    address = get_location_info(current_pos)
    if 'Самара' in address:
        mes = f'Твои координаты {current_pos}\nАдрес {address}\n\nЖил бы в нормальной стране, я бы точно адрес знал.\n\nВключай ВПН, мне нужен челендж!!!'
    else:
        mes = f'Твои координаты {current_pos}\nАдрес {address}'
    update.message.reply_text(
        text=mes,
        reply_markup=MRK_START
    )


# MAIN HANDLER ------------------------------------------------
@log_error
def message_handler(update: Update, context: CallbackContext):
    text = update.message.text
    if text == '/start':
        return start_handler(update, context)
    elif text == button_help:
        return button_help_handler(update, context)
    else:
        return other_message_handler(update, context)


def location_handler(update: Update, context: CallbackContext):
    return location_message_handler(update, context)
