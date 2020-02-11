from telegram import Update, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import CallbackContext

from weather_bot.loger import log_error

# BUTTONS -----------------------------------------------------
button_help = 'Help'
button_weather = 'Weather'
button_weather_current = 'Current'
button_weather_forecast = 'Forecast'

# KEYBOARDS ---------------------------------------------------
KB_START = [
            [
                KeyboardButton(text=button_help),
                KeyboardButton(text=button_weather)
            ],
        ]

KB_WEATHER = [
            [
                KeyboardButton(text=button_weather_current),
                KeyboardButton(text=button_weather_forecast)
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


def button_help_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text="This bot is displaying current or forecast weather in Samara.",
        reply_markup=MRK_START
    )


def button_weather_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text="",
        reply_markup=MRK_WEATHER
    )


@log_error
def message_handler(update: Update, context: CallbackContext):
    text = update.message.text
    if text == button_help:
        return button_help_handler(update, context)
    if text ==button_weather:
        return button_weather_handler(update, context)

    update.message.reply_text(
        text='',
        reply_markup=MRK_START
    )