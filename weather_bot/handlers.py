from telegram import Update, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import CallbackContext

from weather_bot.loger import log_error
from weather_bot.weather_requests import get_current_weather, get_forecast_weather

# BUTTONS -----------------------------------------------------
button_help = 'Help'
button_weather = 'Weather'
button_weather_current = 'Current'
button_weather_forecast = 'Forecast'
button_weather_back = 'Back'

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
    [
        KeyboardButton(text=button_weather_back)
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
def button_help_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text="This bot is displaying current or forecast weather in Samara.",
        reply_markup=MRK_START
    )


def button_weather_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text="Here you can view current or forecast weather in Samara.",
        reply_markup=MRK_WEATHER
    )


def button_weather_current_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text=get_current_weather(),
        reply_markup=MRK_WEATHER
    )


def button_weather_forecast_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text=get_forecast_weather(),
        reply_markup=MRK_WEATHER
    )


def button_weather_back_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text="This bot is displaying current or forecast weather in Samara.",
        reply_markup=MRK_START
    )

# MAIN HANDLER ------------------------------------------------
@log_error
def message_handler(update: Update, context: CallbackContext):
    text = update.message.text
    if text == button_help:
        return button_help_handler(update, context)
    if text == button_weather:
        return button_weather_handler(update, context)
    if text == button_weather_current:
        return button_weather_current_handler(update, context)
    if text == button_weather_forecast:
        return button_weather_forecast_handler(update, context)
    if text == button_weather_back:
        return button_weather_back_handler(update, context)

    update.message.reply_text(
        text='',
        reply_markup=MRK_START
    )
