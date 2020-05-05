from db_classes import *
from sqlalchemy.orm import sessionmaker, load_only
from sqlalchemy import create_engine, and_
from config import logindb, passdb, dbhost, dbname
import datetime
from sqlalchemy.sql import func

engine = create_engine(
    f'sqlite://{logindb}:{passdb}@{dbhost}/{dbname}',
    echo=True)

Session = sessionmaker(bind=engine)
Session.configure(bind=engine)

session = Session()


def is_telegram_id_exists(telegram_id: int) -> bool:
    query = session.query(User) \
        .filter(User.telegram_id == telegram_id)
    return session.query(query.exists()).scalar()


def add_chat_by_telegram(telegram_id: int, name: str):
    session.add(User(telegram_id=telegram_id,
                     created_at=datetime.datetime.utcnow(),
                     chat_name=name
                     )
                )
    session.commit()


def add_user_by_telegram(telegram_id: int, first_name: str, last_name: str, login: str, language_code: str):
    session.add(User(telegram_id=telegram_id,
                     created_at=datetime.datetime.utcnow(),
                     first_name=first_name,
                     last_name=last_name,
                     login=login,
                     language_code=language_code
                     )
                )
    session.commit()


def find_user_id_by_telegram_id(telegram_id: int) -> int:
    user = session.query(User) \
        .filter(User.telegram_id == telegram_id) \
        .first()
    return user.id


def find_user_role(telegram_id: int) -> str:
    user = session.query(User) \
        .filter(User.telegram_id == telegram_id) \
        .first()
    return user.role