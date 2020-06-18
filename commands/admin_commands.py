from dao import get_user_role, update_user_role
from dao import add_plant, update_plant
from commands.keyboards import TITLES
from telegram import Message


def set_user_role():
    '''Only for admin, role = 1
    Common users' role = 0'''
    pass


def add_plant_command(bot, update, args):
    chat_id = update.effective_message.chat_d
    user_role = get_user_role(chat_id)
    
    if user_role == 1:
        for 
    else:
        bot.send_message(
            chat_id=chat_id,
            text='Упс, только разработчик понимает эту команду'
        )


def update_plant_command(bot, update, args):
    chat_id = update.effective_message.chat_d
    user_role = get_user_role(chat_id)
    
    if user_role == 1:
        message=args.split('\n')

    else:
        bot.send_message(
            chat_id = chat_id,
            text = 'Упс, только разработчик понимает эту команду'
        )


def ask_admin(bot, update):
    chat_id = update.effective_message.chat_id
    text = update.message.text

    bot.send_message(
        chat_id=chat_id,
        text="Спасибо! Ваш вопрос отправлен."
    )
    bot.send_message(
        chat_id=354668710, 
        text="Вопрос от пользователя:\n{0}".format(text)
    )


def answer_to_user(bot, update, args):
    #add to main.py commands (as /answer)
    chat_id = update.effective_message.chat_d
    user_role = get_user_role(chat_id)
    
    if user_role == 1:
        user_id = args
        bot.send_message(
            chat_id=chat_id,
            text='Ответ на вопрос?'
        )
        send_answer(bot, update, user_id)
    else:
        bot.send_message(
            chat_id=chat_id,
            text='Упс, только разработчик понимает эту команду'
        )


def send_answer(bot, update, chat_id):
    text = update.message.text

    bot.send_message(
        chat_id=chat_id,
        text='Ответ на ваш вопрос:\n\n{0}'.format(text)
    )