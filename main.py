'''Links for help:
https://github.com/python-telegram-bot/python-telegram-bot/blob/master/README.rst
Thanks for help in code (and some ideas):
https://github.com/ouhettur/boobsbot
https://github.com/dmakeienko/remind_me_bot
'''
from commands.tg_commands import start, info, help_me, unknown
from commands.plant_commands import plant_inline_keyboard_handler
from commands.notifications_commands import send_notification
from commands.admin_commands import set_user_role, answer_to_user
from commands.admin_commands import add_plant_command, update_plant_command
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram.ext import MessageHandler, Filters
import logging
import os

TOKEN = os.environ.get("PLANTSTATIONBOT_TOKEN")

def main():
    updater = Updater(token=TOKEN)
    j = updater.job_queue
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
    dispatcher = updater.dispatcher

    # Start
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # Info
    info_handler = CommandHandler('info', info)
    dispatcher.add_handler(info_handler)

    # Help
    help_handler = CommandHandler('help', help_me)
    dispatcher.add_handler(help_handler)

    # Admin commands
    set_user_role_handler = CommandHandler('role', set_user_role)
    answer_to_user_handler = CommandHandler('answer', answer_to_user)
    add_plant_command_handler = CommandHandler('padd', add_plant_command)
    update_plant_command_handler = CommandHandler('pubdate', update_plant_command)
    dispatcher.add_handler(set_user_role_handler)
    dispatcher.add_handler(answer_to_user_handler)
    dispatcher.add_handler(add_plant_command_handler)
    dispatcher.add_handler(update_plant_command_handler)
    
    # Jobs
    j.run_repeating(send_notification, interval=60,  first=0)
    
    # Plants inline keyboard
    dispatcher.add_handler(CallbackQueryHandler(plant_inline_keyboard_handler))

    # Always should be last
    unknown_handler = MessageHandler(Filters.command, unknown)
    dispatcher.add_handler(unknown_handler)

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()


if __name__ == '__main__':
    main()