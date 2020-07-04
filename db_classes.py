from sqlalchemy import Column, Integer, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy_repr import RepresentableBase

Base = declarative_base(cls=RepresentableBase)


class Users(Base):
    __tablename__ = 'Users'
    user_id = Column(Integer, primary_key=True, unique=True)
    telegram_id = Column(Integer)
    first_name = Column(Text)
    last_name = Column(Text)
    login = Column(Text)
    role = Column(Integer)


class Plants(Base):
    __tablename__ = 'Plants'
    plant_id = Column(Integer, primary_key=True, unique=True)
    name = Column(Text)
    description = Column(Text)
    light = Column(Text)
    temperature = Column(Text)
    watering = Column(Text)
    moisture = Column(Text)
    fertilizer = Column(Text)
    transfer = Column(Text)
    more_info = Column(Text)
    photo = Column(Text)


class UsersPlants(Base):
    __tablename__ = 'UsersPlants'
    user_plant_id = Column(Integer, primary_key=True, unique=True)
    user_id = Column(Integer, ForeignKey('Users.user_id'))
    name = Column(Text)
    created = Column(Text)
    users = relationship(Users)


class NotificationCategory(Base):
    __tablename__ = 'NotificationCategory'
    id = Column(Integer, primary_key=True, unique=True)
    category = Column(Text)
    actions = Column(Text)


class NotificationFrequency(Base):
    __tablename__ = 'NotificationFrequency'
    id = Column(Integer, primary_key=True, unique=True)
    frequency = Column(Text)
    day_plus = Column(Integer)
    month_plus = Column(Integer)
    year_plus = Column(Integer)


class UsersNotifications(Base):
    __tablename__ = 'UsersNotifications'
    notific_id = Column(Integer, primary_key=True, unique=True)
    user_plant_id = Column(Integer, ForeignKey('UsersPlants.user_plant_id'))
    category = Column(Integer, ForeignKey('NotificationCategory.id'))
    frequency = Column(Integer, ForeignKey('NotificationFrequency.id'))
    time = Column(Text)
    first_date = Column(Text)
    next_date = Column(Text)
    usersplants = relationship(UsersPlants)
    notificationcategory = relationship(NotificationCategory)
    notificationfrequency = relationship(NotificationFrequency)