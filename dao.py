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


def change_user_role(user_id: int, role: int):
    pass


def is_plant_exists(plant_name: str) -> bool:
    pass


def get_plant_id_by_name(plant_name: str) -> int:
    pass


def get_plant(plant_id: int):
    pass


def add_plant(plant_name: str, description=None, light=None, temperature=None, watering=None, spraying=None, fertilizer=None, transfer=None, reproduction=None, photo_link=None):
    session.add(Plants(name=plant_name,
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


def update_plant(plant_id: int, plant_name=None, description=None, light=None, temperature=None, watering=None, spraying=None, fertilizer=None, transfer=None, reproduction=None, photo_link=None):
    pass


def is_user_plant_exists(user_id: int, plant_name: str) -> bool:
    pass


def get_user_plants(user_id: int):
    pass


def get_user_plant_id(user_id: int, plant_name: str) -> int:
    pass


def add_plant_to_user(user_id: int, plant_name: str, created: str):
    session.add(UsersPlants(user_id=user_id,
                     plant_name=plant_name,
                     created=created
                     )
                )
    session.commit()


def delete_user_plant(user_id: int, plant_name: str):
    pass


def get_notif_categories(user_id: int):
    pass


def get_notif_category_id(category: str) -> int:
    pass


def get_notif_frequencies(user_id: int):
    pass


def get_notif_frequency_id(frequency: str) -> int:
    pass


def is_user_notification_exists(user_plant_id: int, notif_category: int) -> bool:
    pass


def get_user_notification(user_plant_id: int):
    pass


def get_user_notification_id(user_plant_id: int, notif_category: int) -> int:
    pass


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