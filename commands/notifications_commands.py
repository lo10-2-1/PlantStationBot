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
            text='Эта команда добавляет уведомление к одному растению в одной из категорий: полив, опрыскивание, удобрение и пересадка. Чтобы начать, напишите название растения, к которому вы хотите добавить уведомление.'
        )
        start_notification_command(bot, update, ADD)
    elif text == CHANGE:
        bot.send_message(
            chat_id=chat_id,
            text='Эта команда меняет время и частоту уведомления у одного вашего растения в одной из категорий: полив, опрыскивание, удобрение и пересадка. Чтобы начать, напишите название растения, у которого вы хотите поменять уведомление.'
        )
        start_notification_command(bot, update, CHANGE)
    elif text == DELETE:
        bot.send_message(
            chat_id=chat_id,
            text='Эта команда удаляет уведомление у одного растения в одной из категорий: полив, опрыскивание, удобрение и пересадка. Чтобы начать, напишите название растения, у которого вы хотите удалить уведомление.'
        )
        start_notification_command(bot, update, DELETE)
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
                            .format(notifications_list[i].category,
                            notifications_list[i].frequency,
                            notifications_list[i].time,
                            notifications_list[i].next_date)
    bot.send_message(
        chat_id=chat_id,
        text=message_text
    )


def start_notification_command(bot, update, keyword):
    chat_id = update.effective_message.chat_id
    plant_name = update.message.text

    bot.send_message(
        chat_id=chat_id,
        text='Напишите название категории: полив, опрыскивание, удобрение и пересадка.'
    )
    set_category(bot, update, keyword, plant_name)


def set_category(bot, update, keyword, plant_name):
    chat_id = update.effective_message.chat_id
    category = update.message.text

    if keyword == ADD or keyword == CHANGE:
        bot.send_message(
            chat_id=chat_id,
            text='Напишите время уведомления в формате ЧЧ:ММ.'
        )
        set_time(bot, update, keyword, plant_name, category)
    elif keyword == DELETE:
        bot.send_message(
            chat_id=chat_id,
            text='Удаляем уведомление у растения {0} в категории {1}.'.format(plant_name, category)
        )
        delete_notification(bot, update, chat_id, plant_name, category)


def set_time(bot, update, keyword, plant_name, category):
    chat_id = update.effective_message.chat_id
    time = update.message.text
    wrong_time = 'Кажется, вы ввели время в неправильном формате. Попробуйте еще раз.'

    check_time = time.split(sep=':')
    if len(check_time[0]) <= 2:
        try:
            check_time = map(int, check_time)
            frequency_list = get_notif_frequencies()
            message = 'Теперь нужно написать, как часто вы хотите написать уведомления? Выберите один вариант из списка:'
            for freq in frequency_list:
                message += '\n• {}'.format(freq.frequency)
            bot.send_message(
                    chat_id=chat_id,
                    text=message
                )   
            set_frequency(bot, update, keyword, plant_name, category, time)
        except TypeError:
            bot.send_message(
                chat_id=chat_id,
                text=wrong_time
            )
    else:
        bot.send_message(
            chat_id=chat_id,
            text=wrong_time
        )


def set_frequency(bot, update, keyword, plant_name, category, time):
    pass


def create_notification(bot, update, plant_name, category, time, frequency, first_date):
    pass


def update_notification(bot, update, plant_name, category, time, frequency, first_date):
    pass


def delete_notification(bot, update, telegram_id, plant_name, category):
    user_id = get_user_id_by_telegram_id(telegram_id)
    user_plant_id = get_user_plant_id(user_id, plant_name)

    if does_user_notification_exist(user_plant_id):
        notification_id = get_user_notification_id(user_plant_id, category)
        delete_user_notification(notification_id)
        bot.send_message(
            chat_id=telegram_id,
            text='Уведомление успешно удалено.'
        )
    else:
        bot.send_message(
            chat_id=telegram_id,
            text='Такого уведомления у вас нет. Попробуйте еще раз.'
        )


def send_notification(bot, job):
    if get_current_notification():
        for notif in get_current_notification():
            category = get_category_by_id(notif['category'])
            plant_name = get_plant_name_by_user_plant_id(notif['user_plant_id'])
            notification = 'Пора {0} растение {1}! Время не ждет!' \
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

    frequency = get_frequency_by_id(notification.frequency)
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