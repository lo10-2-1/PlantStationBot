from db_classes import *
from sqlalchemy.orm import sessionmaker, load_only
from sqlalchemy import create_engine, and_
import datetime
from sqlalchemy.sql import func

engine = create_engine('sqlite://database.db', echo=True)

Session = sessionmaker(bind=engine)
Session.configure(bind=engine)

session = Session()


def is_telegram_id_exists(telegram_id: int) -> bool:
    query = session.query(Users) \
        .filter(Users.telegram_id == telegram_id)
    return session.query(query.exists()).scalar()


def get_user_id_by_telegram_id(telegram_id: int) -> int:
    user = session.query(Users) \
        .filter(Users.telegram_id == telegram_id) \
        .first()
    return user.user_id


def get_user_role(telegram_id: int) -> int:
    user = session.query(Users) \
        .filter(Users.telegram_id == telegram_id) \
        .first()
    return user.role


def add_user_by_telegram(telegram_id: int, first_name: str, last_name: str, login: str, role = 0):
    session.add(Users(telegram_id=telegram_id,
                     first_name=first_name,
                     last_name=last_name,
                     login=login,
                     role=role
                     )
                )
    session.commit()


def update_user_role(user_id: int, role: int):
    pass


def is_plant_exists(plant_title: str) -> bool:
    query = session.query(Plants) \
        .filter(Plants.name.ilike('%{}%'.format(plant_title)))
    return session.query(query.exists()).scalar()


def get_plant_id_by_title(plant_title: str) -> int:
    plant = session.query(Plants) \
        .filter(Plants.name.ilike('%{}%'.format(plant_title))) \
        .first()
    return plant.plant_id


def get_plant(plant_id: int):
    plant_all = session.query(Plants) \
        .filter(Plants.plant_id == plant_id) \
        .first()
    return plant_all


def add_plant(plant_title: str, description=None, light=None, temperature=None, watering=None, spraying=None, fertilizer=None, transfer=None, reproduction=None, photo_link=None):
    session.add(Plants(name=plant_title,
                     description=description,
                     light=light,
                     temperature=temperature,
                     watering=watering,
                     spraying=spraying,
                     fertilizer=fertilizer,
                     transfer=transfer,
                     reproduction=reproduction,
                     photo=photo_link
                     )
                )
    session.commit()


def update_plant(plant_id: int, plant_title=None, description=None, light=None, temperature=None, watering=None, spraying=None, fertilizer=None, transfer=None, reproduction=None, photo_link=None):
    pass


def is_user_plant_exists(user_id: int, plant_name: str) -> bool:
    query = session.query(UsersPlants) \
        .filter(UsersPlants.user_id == user_id, 
                UsersPlants.name.ilike('%{}%'.format(plant_name)))
    return session.query(query.exists()).scalar()


def get_user_plants(user_id: int):
    user_plant = session.query(UsersPlants) \
        .filter(UsersPlants.user_id == user_id) \
        .all()
    return user_plant


def get_user_plant_id(user_id: int, plant_name: str) -> int:
    user_plant_id = session.query(UsersPlants) \
        .filter(UsersPlants.user_id == user_id,
                UsersPlants.name.ilike('%{}%'.format(plant_name))) \
        .first()
    return user_plant_id


def add_plant_to_user(user_id: int, plant_name: str, created: str):
    session.add(UsersPlants(user_id=user_id,
                     plant_name=plant_name,
                     created=created
                     )
                )
    session.commit()


def delete_user_plant(user_id: int, plant_name: str):
    pass


def get_notif_categories():
    notif_categories = session.query(NotificationCategory.category) \
        .order_by(NotificationCategory.id) \
        .all()
    return notif_categories


def get_notif_category_id(category: str) -> int:
    notif_category_id = session.query(NotificationCategory) \
        .filter(NotificationCategory.category.ilike('%{}%'.format(category))) \
        .first()
    return notif_category_id.id


def get_notif_frequencies(user_id: int):
    notif_frequencies = session.query(NotificationFrequency.frequency) \
        .order_by(NotificationFrequency.id) \
        .all()
    return notif_frequencies


def get_notif_frequency_id(frequency: str) -> int:
    notif_frequency_id = session.query(NotificationFrequency) \
        .filter(NotificationFrequency.frequency.ilike('%{}%'.format(frequency))) \
        .first()
    return notif_frequency_id.id


def is_user_notification_exists(user_plant_id: int, notif_category: int) -> bool:
    query = session.query(UsersNotifications) \
        .filter(UsersNotifications.user_plant_id == user_plant_id, 
                UsersNotifications.notif_category.ilike('%{}%'.format(notif_category)))
    return session.query(query.exists()).scalar()


def get_user_notifications(user_plant_id: int):
    user_notifications = session.query(UsersNotifications) \
        .filter(UsersNotifications.user_plant_id == user_plant_id) \
        .all()
    return user_notifications


def get_user_notification_id(user_plant_id: int, notif_category: int) -> int:
    user_notification_id = session.query(UsersNotifications) \
        .filter(UsersNotifications.user_plant_id == user_plant_id, 
                UsersNotifications.notif_category.ilike('%{}%'.format(notif_category))) \
        .first()
    return user_notification_id


def add_user_notification(user_plant_id: int, notif_category: int, notif_frequency: int, time: str, first_date: str):
    session.add(UsersNotifications(user_plant_id=user_plant_id,
                     notif_category=notif_category,
                     notif_frequency=notif_frequency,
                     time=time,
                     first_date=first_date
                     )
                )
    session.commit()


def update_user_notification(notific_id: int, notif_frequency=None, time=None, first_date=None, next_date=None):
    pass


def delete_user_notification(notific_id: int):
    pass