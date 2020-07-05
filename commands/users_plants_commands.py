from dao import *
from commands.keyboards import *
from telegram import Message
import datetime


def user_plants_keyboard_handler(bot, update):
    chat_id = update.effective_message.chat_id
    text = update.message.text

    if text == MY_PLANTS:
        bot.send_message(
            chat_id=chat_id,
            text='Секунду, собираем список ваших растений.'
        )
        show_my_plants(bot, update)
    elif text == ADD:
        bot.send_message(
            chat_id=chat_id,
            text='Какое растение вы хотите добавить? Напишите название (и только его).'
        )
        add_my_plant(bot, update)
    elif text == CHANGE:
        bot.send_message(
            chat_id=chat_id,
            text='Название какого растения вы хотите изменить? Просьба написать название точно.'
        )
        change_plant_name(bot, update)
    elif text == DELETE:
        bot.send_message(
            chat_id=chat_id,
            text='''Какое растение вы хотите удалить?
            
            *Предупреждение:* вместе с растением удалятся все его уведомления''',
            parse_mode='Markdown'
        )
        delete_plant(bot, update)
    if text == BACK:
        import commands.tg_commands as tg
        return tg.start(bot, update)


def show_my_plants(bot, update):
    chat_id = update.effective_message.chat_id

    user_id = get_user_id_by_telegram_id(chat_id)
    try:
        user_plants_list = get_user_plants(user_id)
        message_text = 'Ваши растения на данный момент:'
        for plant_name in user_plants_list:
            message_text += '\n• {0}'.format(plant_name.name)
        bot.send_message(
            chat_id=chat_id,
            text=message_text
        )
    except:
        bot.send_message(
            chat_id=chat_id,
            text='Упс, кажется, у вас нет растений. Но их всегда можно добавить.'
        )


def add_my_plant(bot, update):
    chat_id = update.effective_message.chat_id
    text = update.message.text

    user_id = get_user_id_by_telegram_id(chat_id)
    created = datetime.datetime.now()
    add_plant_to_user(user_id, text, created)
    bot.send_message(
            chat_id=chat_id,
            text='''Растение успешно добавлено в базу данных. Теперь вы можете добавлять к нему уведомления.
            
            Если вы написали название вашего растения неправильно, просто измените его с помощью соответствующей команды.'''
        )


def change_plant_name(bot, update):
    chat_id = update.effective_message.chat_id
    text = update.message.text

    user_id = get_user_id_by_telegram_id(chat_id)
    if does_user_plant_exist(user_id, text):
        user_plant_id = get_user_plant_id(user_id, text)
        bot.send_message(
            chat_id=chat_id,
            text='Напишите новое название растения "{0}"'.format(text)
        )
        new_plant_name(bot, update, user_plant_id)
    else:
        bot.send_message(
            chat_id=chat_id,
            text='Такое растение не найдено. Попробуйте еще раз.'
        )


def new_plant_name(bot, update, user_plant_id):
    chat_id = update.effective_message.chat_id
    text = update.message.text

    update_user_plant_name(user_plant_id, text)
    bot.send_message(
            chat_id=chat_id,
            text='Название успешно отредактировано.'
        )


def delete_plant(bot, update):
    chat_id = update.effective_message.chat_id
    text = update.message.text

    user_id = get_user_id_by_telegram_id(chat_id)
    if does_user_plant_exist(user_id, text):
        user_plant_id = get_user_plant_id(user_id, text)
        plant_notifications = get_plant_notifications(user_plant_id)
        for notification in plant_notifications:
            delete_user_notification(notification.notific_id)
        bot.send_message(
            chat_id=chat_id,
            text='Растение "{0}" и его уведомления успешно удалены'.format(text)
        )
    else:
        bot.send_message(
            chat_id=chat_id,
            text='Такое растение не найдено. Попробуйте еще раз.'
        )