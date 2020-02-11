from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove
from telegram import Update
from telegram import Bot
from telegram.ext import Updater
from telegram.ext import CallbackContext
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.utils.request import Request

from simple_bot.config import TG_TOKEN
from simple_bot.config import TG_API_URL

button_help = 'Help'


# logging function
# maybe should try to play with message format
def log_error(f):
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            print(f'Error: {e}')
            raise e

    return inner


def button_help_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text="Help!!!",
        reply_markup=ReplyKeyboardRemove()
    )


@log_error
def message_handler(update: Update, context: CallbackContext):
    text = update.message.text
    if text == button_help:
        return button_help_handler(update, context)

    reply_markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=button_help)
            ],
        ],
        resize_keyboard=True,
    )

    update.message.reply_text(
        text="Hi, send me some messages!",
        reply_markup=reply_markup
    )


def main():
    print('start')

    req = Request()
    bot = Bot(
        request=req,
        token=TG_TOKEN,
        base_url=TG_API_URL
    )
    updater = Updater(bot=bot, use_context=True)
    print(updater.bot.get_me())

    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))

    updater.start_polling()
    updater.idle()

    print('Finish')


if __name__ == '__main__':
    main()
