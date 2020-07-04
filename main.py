'''Links for help:
https://github.com/python-telegram-bot/python-telegram-bot/blob/master/README.rst
Thanks for help in code (and some ideas):
https://github.com/ouhettur/boobsbot
https://github.com/dmakeienko/remind_me_bot
'''
from commands.tg_commands import start, info, help, unknown
from commands.plant_commands import plant_inline_keyboard_handler
from commands.notifications_commands import send_notification
from commands.admin_commands import set_user_role, answer_to_user
from commands.admin_commands import add_plant_command, update_plant_command
from telegram.ext import Updater, CommandHandler
import logging
import os

TOKEN = os.environ.get("PLANTSTATIONBOT_TOKEN")

def main():
    updater = Updater(token=TOKEN, use_context=True)
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
    help_handler = CommandHandler('help', help)
    dispatcher.add_handler(help_handler)

    #Callback for menu
    dispatcher.add_handler(CallbackQueryHandler(button))

    # Always should be last
    unknown_handler = MessageHandler(Filters.command, unknown)
    dispatcher.add_handler(unknown_handler)

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()


if __name__ == '__main__':
    main()

# Create Updater object and attach dispatcher to it
  updater = Updater(token=TOKEN)
  j = updater.job_queue
  dispatcher = updater.dispatcher
  # Add command handler to dispatcher

  # Start
  start_handler = CommandHandler('start', start)
  dispatcher.add_handler(start_handler)

  # Create Remind
  create_remind_handler = CommandHandler('remind', create_remind, pass_args=True)
  dispatcher.add_handler(create_remind_handler)
  
  # Create Remind for today
  create_remind_today_handler = CommandHandler(['today', 'ty', 'at' 'сегодня', 'cьогодні'], create_today, pass_args=True)
  dispatcher.add_handler(create_remind_today_handler)

  # Create Remind for tomorrow
  create_remind_tomorrow_handler = CommandHandler(['tomorrow', 'tw', 'завтра'], create_tomorrow, pass_args=True)
  dispatcher.add_handler(create_remind_tomorrow_handler)

  # List
  list_handler = CommandHandler('list', list_reminds, pass_args=True)
  dispatcher.add_handler(list_handler)

  # Jobs
  j.run_repeating(remind, interval=60,  first=0)
  j.run_repeating(remind_1, interval=60,  first=0)
  j.run_repeating(remind_2, interval=60,  first=0)
  j.run_repeating(check_expired, interval=60,  first=0)
  
  # Delete
  delete_handler = CommandHandler(['delete', 'rm'], delete_remind, pass_args=True)
  dispatcher.add_handler(delete_handler)

  # Done
  done_handler =  CommandHandler('done', close_remind, pass_args=True)
  dispatcher.add_handler(done_handler)

  # Update
  update_remind_handler = CommandHandler('update', update_remind, pass_args=True)
  dispatcher.add_handler(update_remind_handler)

  # Update
  postpone_remind_handler = CommandHandler(['postpone', 'snooze', 'pp'], postpone, pass_args=True)
  dispatcher.add_handler(postpone_remind_handler)

  # Feedback
  feedback_remind_handler = CommandHandler('feedback', feedback, pass_args=True)
  dispatcher.add_handler(feedback_remind_handler)
  
  # Help
  help_remind_handler = CommandHandler('help', help_remind)
  dispatcher.add_handler(help_remind_handler)
  
  # About
  about_remind_handler = CommandHandler('about', about)
  dispatcher.add_handler(about_remind_handler)
  
  

  # Always should be last
  unknown_handler = MessageHandler(Filters.command, unknown)
  dispatcher.add_handler(unknown_handler)

  