from dao import get_user_role, update_user_role
from dao import does_telegram_id_exist, get_user_id_by_telegram_id, add_user_by_telegram
from dao import add_plant, update_plant, does_plant_exist, get_plant_id_by_title
from commands.keyboards import TITLES
from telegram import Message


def set_user_role(bot, update, args):
    '''Only for admin, role = 1
    Common users' role = 0'''
    chat_id = update.effective_message.chat_d
    text = update.message.text
    
    if user_role == 1:
        args = args.split('\n')
        telegram_id = args[0]
        user_role = args[1]
        if not does_telegram_id_exist(telegram_id):
            first_name = update.message.from_user.first_name
            last_name = update.message.from_user.last_name
            login = update.message.from_user.username
            add_user_by_telegram(telegram_id, first_name, last_name, login, user_role)
        else:
            user_id = get_user_id_by_telegram_id(telegram_id)
            update_user_role(user_id, user_role)
        bot.send_message(
            chat_id=chat_id,
            text='Статус пользователя обновлен.'
        )
    else:
        bot.send_message(
            chat_id=chat_id,
            text='Упс, только разработчик понимает эту команду'
        )


def add_plant_command(bot, update, args):
    chat_id = update.effective_message.chat_d
    text = update.message.text
    
    if user_role == 1:
        add_plant(args)
        bot.send_message(
            chat_id=chat_id,
            text='Растение {0} добавлено в базу данных.'.format(args)
        )
    else:
        bot.send_message(
            chat_id=chat_id,
            text='Упс, только разработчик понимает эту команду'
        )


def update_plant_command(bot, update, args):
    '''One command for all plants' characteristics
    '''
    chat_id = update.effective_message.chat_d
    text = update.message.text
    message = args.split('\n')
    plant = message[0]
    item = message[1]
    
    if user_role == 1:
        if does_plant_exist():
            result = update_plant_item(message)
            if type(result) == str:
                bot.send_message(
                chat_id = chat_id,
                text = result
            )
            else:
                bot.send_message(
                    chat_id = chat_id,
                    text = 'Раздел "{0}" растения "{1}" обновлен.'.format(item, plant)
                )
        else:
            bot.send_message(
                chat_id = chat_id,
                text = 'Растение "{0}" не найдено.'.format(plant)
            )
    else:
        bot.send_message(
            chat_id = chat_id,
            text = 'Упс, только разработчик понимает эту команду'
        )


def update_plant_item(item_list: list):
    plant = item_list[0]
    item = item_list[1]
    information = item_list[2]
    plant_id = get_plant_id_by_title(plant)

    if item = TITLES[NAME]:
        update_plant(plant_id, plant_title=information)
    elif item = TITLES[DESCRIPTION]:
        update_plant(plant_id, description=information)
    elif item = TITLES[LIGHT]:
        update_plant(plant_id, light=information)
    elif item = TITLES[TEMPERATURE]:
        update_plant(plant_id, temperature=information)
    elif item = TITLES[WATERING]:
        update_plant(plant_id, watering=information)
    elif item = TITLES[MOISTURE]:
        update_plant(plant_id, moisture=information)
    elif item = TITLES[FERTILIZER]:
        update_plant(plant_id, fertilizer=information)
    elif item = TITLES[TRANSFER]:
        update_plant(plant_id, transfer=information)
    elif item = TITLES[MORE_INFO]:
        update_plant(plant_id, more_info=information)
    elif item = TITLES[PHOTO_LINK]:
        update_plant(plant_id, photo_link=information)
    else:
        return 'Такого раздела нет.'


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