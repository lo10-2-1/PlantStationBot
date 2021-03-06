from db_classes import *
from sqlalchemy import Table, MetaData
from sqlalchemy.orm import sessionmaker, load_only
from sqlalchemy import create_engine, and_
from sqlalchemy.sql import func
import datetime
import json


def eng_cre():
    engine = create_engine('sqlite:///database.db', echo=True)
    meta = MetaData()
    Base.metadata.create_all(engine)
    return engine


def connect_db(engine):
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)

    session = Session()
    return session

engine = create_engine('sqlite:///database.db', echo=True)
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()
# engine = eng_cre()
# session = connect_db(engine)

class NotificationEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UsersNotifications):
            return obj.__dict__


def does_user_exist(telegram_id=False, login=False) -> bool:
    if telegram_id:
        query = session.query(Users) \
            .filter(Users.telegram_id == telegram_id)
    elif login:
        query = session.query(Users) \
            .filter(Users.login == login)
    return session.query(query.exists()).scalar()


def get_user_id_by_telegram_id(telegram_id: int) -> int:
    user = session.query(Users) \
        .filter(Users.telegram_id == telegram_id) \
        .first()
    return user.user_id


def get_telegram_id_by_login(login: str) -> int:
    user = session.query(Users) \
        .filter(Users.telegram_id == telegram_id) \
        .first()
    return user.login


def get_telegram_id_by_user_id(user_id: int) -> int:
    user = session.query(Users) \
        .filter(Users.user_id == user_id) \
        .first()
    return user.telegram_id


def get_user_role(telegram_id: int) -> int:
    user = session.query(Users) \
        .filter(Users.telegram_id == telegram_id) \
        .first()
    return user.role


def add_user_by_telegram(telegram_id: int, login: str, role = 0, first_name: str=None, last_name: str=None):
    session.add(Users(telegram_id=telegram_id,
                     first_name=first_name,
                     last_name=last_name,
                     login=login,
                     role=role
                     )
                )
    session.commit()


def update_user_role(user_id: int, role: int):
    session.query(Users) \
        .filter(Users.user_id == user_id) \
        .update({'role': role})
    session.commit()


def does_plant_exist(plant_title: str) -> bool:
    query = session.query(Plants) \
        .filter(Plants.name.ilike('%{}%'.format(plant_title)))
    return session.query(query.exists()).scalar()


def get_plant_id_by_title(plant_title: str) -> int:
    plant = session.query(Plants) \
        .filter(Plants.name.ilike('%{}%'.format(plant_title))) \
        .first()
    return plant.plant_id


def get_plant(plant_id: int):
    plant = session.query(Plants) \
        .filter(Plants.plant_id == plant_id) \
        .first()
    return plant


def add_plant(plant_title: str):
    session.add(Plants(name=plant_title))
    session.commit()


def update_plant(plant_id: int, plant_title=False, description=False, light=False, temperature=False, 
            watering=False, moisture=False, fertilizer=False, transfer=False, more_info=False, photo_link=False):
    update = [plant_title, description, light, temperature, 
            watering, moisture, fertilizer, transfer, more_info, photo_link]
    update_title = ['plant_title', 'description', 'light', 'temperature', 
            'watering', 'moisture', 'fertilizer', 'transfer', 'more_info', 'photo_link']
    for i in range(len(update)):
        if update[i]:
            session.query(Plants) \
            .filter(Plants.plant_id == plant_id) \
            .update({update_title[i]: update[i]})
    session.commit()


def does_user_plant_exist(user_id: int, plant_name: str) -> bool:
    query = session.query(UsersPlants) \
        .filter(UsersPlants.user_id == user_id, 
                UsersPlants.name.ilike('%{}%'.format(plant_name)))
    return session.query(query.exists()).scalar()


def get_user_plants(user_id: int):
    user_plants = session.query(UsersPlants) \
                .filter(UsersPlants.user_id == user_id) \
                .all()
    return user_plants


def get_user_plant_id(user_id: int, plant_name: str) -> int:
    user_plant_id = session.query(UsersPlants) \
        .filter(UsersPlants.user_id == user_id,
                UsersPlants.name.ilike('%{}%'.format(plant_name))) \
        .first()
    return user_plant_id.user_plant_id


def get_user_id_by_user_plant_id(user_plant_id: int) -> int:
    user = session.query(UsersPlants) \
        .filter(UsersPlants.user_plant_id == user_plant_id) \
        .first()
    return user.user_id


def get_plant_name_by_user_plant_id(user_plant_id: int) -> int:
    user = session.query(UsersPlants) \
        .filter(UsersPlants.user_plant_id == user_plant_id) \
        .first()
    return user.name


def add_plant_to_user(user_id: int, plant_name: str, created: str):
    session.add(UsersPlants(user_id=user_id,
                     plant_name=plant_name,
                     created=created
                     )
                )
    session.commit()


def update_user_plant_name(user_plant_id: int, new_plant_title: str):
    session.query(UsersPlants) \
            .filter(UsersPlants.user_plant_id == user_plant_id) \
            .update({'name': new_plant_title})
    session.commit()


def delete_user_plant(user_id: int, plant_name: str):
    session.query(UsersPlants) \
        .filter(UsersPlants.user_id == user_id, 
                UsersPlants.name.ilike('%{}%'.format(plant_name))) \
        .delete(synchronize_session=False)
    session.commit()


def get_notif_categories():
    notif_categories = session.query(NotificationCategory.category) \
        .order_by(NotificationCategory.id) \
        .all()
    return notif_categories


def get_category_id(category: str) -> int:
    notif_category_id = session.query(NotificationCategory) \
        .filter(NotificationCategory.category.ilike('%{}%'.format(category))) \
        .first()
    return notif_category_id.id


def get_category_by_id(category_id: str) -> int:
    notif_category = session.query(NotificationCategory) \
        .filter(NotificationCategory.id == category_id) \
        .first()
    return notif_category


def get_notif_frequencies():
    notif_frequencies = session.query(NotificationFrequency.frequency) \
        .order_by(NotificationFrequency.id) \
        .all()
    return notif_frequencies


def get_frequency_id(frequency: str) -> int:
    notif_frequency_id = session.query(NotificationFrequency) \
        .filter(NotificationFrequency.frequency.ilike('%{}%'.format(frequency))) \
        .first()
    return notif_frequency_id.id


def get_frequency_by_id(frequency_id: str) -> int:
    notif_frequency = session.query(NotificationFrequency) \
        .filter(NotificationFrequency.id == frequency_id) \
        .first()
    return notif_frequency


def does_user_notification_exist(user_plant_id: int, category: int) -> bool:
    query = session.query(UsersNotifications) \
        .filter(UsersNotifications.user_plant_id == user_plant_id, 
                UsersNotifications.category.ilike('%{}%'.format(category)))
    return session.query(query.exists()).scalar()


def get_plant_notifications(user_plant_id: int):
    user_notifications = session.query(UsersNotifications) \
        .filter(UsersNotifications.user_plant_id == user_plant_id) \
        .all()
    return user_notifications


def get_user_notification_id(user_plant_id: int, category_id: int) -> int:
    user_notification_id = session.query(UsersNotifications) \
        .filter(UsersNotifications.user_plant_id == user_plant_id, 
                UsersNotifications.category_id == category_id) \
        .first()
    return user_notification_id.notific_id


def get_current_notification():
    current_date = datetime.datetime.now().strftime('%d.%m.%Y')
    current_time = datetime.datetime.now().strftime('%H:%M')
    notification = session.query(UsersNotifications) \
        .filter(UsersNotifications.time == current_time,
                UsersNotifications.next_date == current_date) \
        .all()
    notification_j = json.loads(json.dumps(notification, cls=NotificationEncoder, indent=4))
    if notification_j:
        return notification_j


def add_user_notification(user_plant_id: int, category_id: int, frequency_id: int, time: str, first_date: str):
    next_date = first_date
    session.add(UsersNotifications(user_plant_id=user_plant_id,
                     category=category_id,
                     frequency=frequency_id,
                     time=time,
                     first_date=first_date,
                     next_date=next_date
                     )
                )
    session.commit()


def update_user_notification(notific_id: int, frequency_id=False, time=False, first_date=False):
    update = [frequency_id, time, first_date, first_date]
    update_title = ['frequency', 'time', 'first_date', 'next_date']
    for i in range(len(update)):
        if update[i]:
            session.query(UsersNotifications) \
            .filter(UsersNotifications.notific_id == notific_id) \
            .update({update_title[i]: update[i]})
    session.commit()


def delete_user_notification(notific_id: int):
    session.query(UsersNotifications) \
        .filter(UsersNotifications.notific_id == notific_id) \
        .delete(synchronize_session=False)
    session.commit()