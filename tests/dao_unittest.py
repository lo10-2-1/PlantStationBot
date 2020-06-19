import unittest
import datetime
from dao import *
from tests.test_constants import *


def test_does_telegram_id_exist():
    user_1 = does_telegram_id_exist(USER_2[0])
    user_2 = does_telegram_id_exist(2438757923547)
    assert user_1 == True
    assert user_2 == False


def test_get_user_id_by_telegram_id():
    user_id = get_user_id_by_telegram_id(USER_2[0])
    assert user_id == 1


def test_get_user_role():
    user_role = get_user_role(USER_2[0])
    assert user_role == 1


def test_add_user_by_telegram():
    add_user_by_telegram(USER_1[0], USER_1[1])
    add_user_by_telegram(USER_2[0], USER_2[1], USER_2[2], USER_2[3], USER_2[4])


def test_update_user_role():
    update_user_role(2, 1)


def test_does_plant_exist():
    plant_1 = does_plant_exist('Фиалка')
    plant_2 = does_plant_exist('роза')
    plant_3 = does_plant_exist('елка')
    assert plant_1 == True
    assert plant_2 == True
    assert plant_3 == False


def test_get_plant_id_by_title():
    plant_1 = get_plant_id_by_title('Фиалка')
    plant_2 = get_plant_id_by_title('роза')
    assert plant_1 == 1
    assert plant_2 == 2


def test_get_plant():
    plant = get_plant(1)
    assert plant == PLANT_1


def test_add_plant():
    add_plant('Кипарис')
    add_plant('Барбарис')


def test_update_plant():
    update_plant(1, moisture='Нет, не смей')
    update_plant(2, fertilizer='Накорми меня')


def test_does_user_plant_exist():
    user_plant_1 = does_user_plant_exist(1, 'Фиалка раз')
    user_plant_2 = does_user_plant_exist(1, 'фиалка два')
    user_plant_3 = does_user_plant_exist(1, 'елка раз')
    assert user_plant_1 == True
    assert user_plant_2 == True
    assert user_plant_3 == False


def test_get_user_plants():
    user_plants = get_user_plants(1)
    assert user_plants == USERS_PLANTS


def test_get_user_plant_id():
    user_plant_id_1 = does_user_plant_exist(1, 'Фиалка раз')
    user_plant_id_2 = does_user_plant_exist(1, 'фиалка два')
    assert user_plant_id_1 == 1
    assert user_plant_id_2 == 2


def test_add_plant_to_user():
    add_plant_to_user(2, 'Фикус Георгий', str(datetime.datetime.now()))
    add_plant_to_user(2, 'Елощка', str(datetime.datetime.now()))


def test_delete_user_plant():
    delete_user_plant(2, 'Фикус Георгий')
    delete_user_plant(2, 'Елощка')


def test_get_notif_categories():
    notif_categories = get_notif_categories()
    assert notif_categories == CATEGORIES


def test_get_notif_category_id():
    category_id_1 = get_notif_category_id('Опрыскивание')
    category_id_2 = get_notif_category_id('пересадка')
    assert category_id_1 == 2
    assert category_id_2 == 4


def test_get_notif_frequencies():
    notif_frequencies = get_notif_frequencies()
    assert notif_frequencies == FREQUENCIES


def test_get_notif_frequency_id():
    frequency_id_1 = get_notif_category_id('Раз в неделю')
    frequency_id_2 = get_notif_category_id('каждый день')
    assert frequency_id_1 == 4
    assert frequency_id_2 == 1


def test_does_user_notification_exist():
    user_notif_1 = does_user_notification_exist(1, 1)
    user_notif_2 = does_user_notification_exist(1, 3)
    assert user_notif_1 == True
    assert user_notif_2 == False


def test_get_user_notifications():
    user_notif = get_user_notifications(1)
    assert user_notif == NOTIFICATION_1


def test_get_user_notification_id():
    user_notif_1 = get_user_notification_id(1, 1)
    user_notif_2 = get_user_notification_id(2, 3)
    assert user_notif_1 == 1
    assert user_notif_2 == 2


def test_add_user_notification():
    add_user_notification(2, 2, 5, '12:00', '26.05.2020')


def test_update_user_notification():
    update_user_notification(3, 1, '14:00', next_date='28.05.2020')


def test_delete_user_notification():
    delete_user_notification(3)