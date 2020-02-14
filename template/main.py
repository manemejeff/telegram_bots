from telegram import Bot
from telegram.ext import Updater, Filters, MessageHandler
from telegram.utils.request import Request

from .config import TG_TOKEN
from .config import TG_API_URL
from .handlers import message_handler


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
