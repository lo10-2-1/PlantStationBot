from dao import *
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
        show_my_notifications(bot, update)
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


def show_my_notifications(bot, update):
    chat_id = update.effective_message.chat_id

    user_id = get_user_id_by_telegram_id(chat_id)
    user_plants_list = get_user_plants(user_id)
    notifications_list = []
    for plant_id in user_plants_list:
        notifications_list.append(get_plant_notifications(user_plants_list.user_plant_id))
    message_text = 'Ваши уведомления на данный момент на данный момент:'
    for i in range(len(user_plants_list)):
        message_text += '\nУ растения {0}:'.format(user_plants_list[i].name)
        for plant in range(notifications_list[i]):
            message_text += '\nКатегория {0}, частота {1}, следующее уведомление {2}, {3}.' \
                            .format(notifications_list[i].notif_category,
                            notifications_list[i].notif_frequency,
                            notifications_list[i].time,
                            notifications_list[i].next_date)
    bot.send_message(
        chat_id=chat_id,
        text=message_text
    )


def create_notification(bot, update):
    pass


def update_notification(bot, update):
    pass


def delete_notification(bot, update):
    pass


def send_notification(bot, job):
    if get_current_notification():
        for notif in get_current_notification():
            category = get_category_by_id(notif['notif_category'])
            plant_name = get_plant_name_by_user_plant_id(notif['user_plant_id'])
            notification = 'Пора {0} растение {1}! Давай-давай, время не ждет!' \
                            .format(category.actions, plant_name)

            user_id = get_user_id_by_user_plant_id(notif['user_plant_id'])
            telegram_id = get_telegram_id_by_user_id(user_id)
            bot.send_message(chat_id=telegram_id, text=notification)

            count_next_date(notif)
    else:
        return


def count_next_date(notification):
    notific_id = notification.notific_id
    date = notification.next_date

    frequency = get_frequency_by_id(notification.notif_frequency)
    day_plus = frequency.day_plus
    month_plus = frequency.month_plus
    year_plus = frequency.year_plus

    date_list = date.split(sep='.')
    date_list = map(int, date_list)
    next_date = datetime.date(date_list[0]+day_plus, 
                            date_list[1]+month_plus, 
                            date_list[2]+year_plus) \
                        .strftime('%d.%m.%Y')
    update_user_notification(notific_id, next_date=next_date)