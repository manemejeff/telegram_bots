from telegram import Update, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import CallbackContext

from .loger import log_error
from .useless_web import get_random_url

# BUTTONS -----------------------------------------------------
button_help = 'Help'
button_site = 'Site'

# KEYBOARDS ---------------------------------------------------
KB_START = [
    [
        KeyboardButton(text=button_help),
        KeyboardButton(text=button_site)
    ],
]

# MARKUPS -----------------------------------------------------
MRK_START = ReplyKeyboardMarkup(
    keyboard=KB_START,
    resize_keyboard=True,
)


# HANDLERS ----------------------------------------------------
def button_help_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text="Bot is giving you links to the most useless websites ever.",
        reply_markup=MRK_START
    )


def button_site_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text=get_random_url(),
        reply_markup=MRK_START
    )


def other_messages_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='You can manage bot by using buttons',
        reply_markup=MRK_START
    )


# MAIN HANDLER ------------------------------------------------
@log_error
def message_handler(update: Update, context: CallbackContext):
    text = update.message.text
    if text == button_help or text == '/start':
        return button_help_handler(update, context)
    elif text == button_site:
        return button_site_handler(update, context)
    else:
        return other_messages_handler(update, context)
