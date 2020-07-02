from dao import get_notif_categories, get_notif_category_id
from dao import get_notif_frequencies, get_notif_frequency_id
from dao import does_user_notification_exist, get_user_notification_id, get_plant_notifications
from dao import add_user_notification, update_user_notification, delete_user_notification
from dao import get_user_id_by_telegram_id, get_user_plants
from commands.keyboards import *
from commands.tg_commands import start
from telegram import Message
import datetime


def notifications_keyboard_handler(bot, update):
    chat_id = update.effective_message.chat_id
    text = update.message.text

    if text == NOTIF_LIST:
        bot.send_message(
            chat_id=chat_id,
            text='Секунду, собираем список ваших уведомлений.'
        )
        show_notifications(bot, update)
    elif text == ADD:
        bot.send_message(
            chat_id=chat_id,
            text='Напишите название растения, к которому вы хотите добавить уведомление.'
        )
        create_notification(bot, update)
    elif text == CHANGE:
        bot.send_message(
            chat_id=chat_id,
            text='Напишите название растения, к которому вы хотите поменять уведомление.'
        )
        update_notification(bot, update)
    elif text == DELETE:
        bot.send_message(
            chat_id=chat_id,
            text='Напишите название растения, у которого вы хотите удалить уведомление.'
        )
        delete_notification(bot, update)
    elif text == BACK:
        return start(bot, update)


def show_notifications(bot, update):
    pass


def create_notification(bot, update):
    pass


def update_notification(bot, update):
    pass


def delete_notification(bot, update):
    pass


def count_next_date(bot, update):
    pass


def send_notification(bot, update):
    pass