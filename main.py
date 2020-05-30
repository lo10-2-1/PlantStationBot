'''Links for help:
https://github.com/python-telegram-bot/python-telegram-bot/blob/master/README.rst
Thanks for help in code (and some ideas):
https://github.com/ouhettur/boobsbot
https://github.com/dmakeienko/remind_me_bot
'''
from priv import TOKEN
from telegram.ext import Updater, CommandHandler
import logging
from commands.tg_commands import *


def main():
    updater = Updater(token=TOKEN, 
                        use_context=True)
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    helpme_handler = CommandHandler('info', info)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(helpme_handler)

    updater.start_polling()


if __name__ == '__main__':
    main()