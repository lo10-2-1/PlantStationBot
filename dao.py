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


def add_user_by_telegram(telegram_id: int, first_name: str, last_name: str, login: str, role = 0):
    session.add(Users(telegram_id=telegram_id,
                     first_name=first_name,
                     last_name=last_name,
                     login=login,
                     role=role
                     )
                )
    session.commit()


def find_user_id_by_telegram_id(telegram_id: int) -> int:
    user = session.query(Users) \
        .filter(Users.telegram_id == telegram_id) \
        .first()
    return user.user_id


def find_user_role(telegram_id: int) -> str:
    user = session.query(Users) \
        .filter(Users.telegram_id == telegram_id) \
        .first()
    return user.role