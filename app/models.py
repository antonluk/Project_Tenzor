import datetime

from flask_appbuilder import Model
from sqlalchemy import Column, Date, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

mindate = datetime.date(datetime.MINYEAR, 1, 1)


class ContactGroup(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Gender(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Contact(Model):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False, index=True)
    address = Column(String(564), index=True)
    birthday = Column(Date, nullable=True)
    personal_phone = Column(String(20), index=True)
    personal_celphone = Column(String(20))
    contact_group_id = Column(Integer, ForeignKey("contact_group.id"), nullable=False)
    contact_group = relationship("ContactGroup")
    gender_id = Column(Integer, ForeignKey("gender.id"), nullable=False)
    gender = relationship("Gender")

    def __repr__(self):
        return self.name

    def month_year(self):
        date = self.birthday or mindate
        return datetime.datetime(date.year, date.month, 1) or mindate

    def year(self):
        date = self.birthday or mindate
        return datetime.datetime(date.year, 1, 1)


class Product(Model):
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(150), unique=True, nullable=False, index=True)
    price = Column(Integer, nullable=True)
    id_seller = Column(Integer, ForeignKey("seller.id"), nullable=False)
    seller = relationship("Seller")
    category = Column(String(50), nullable=True)
    count = Column(Float(10, 2), nullable=True)

    # TODO: Нужна автоматическая реляция на id продавца


class Seller(Model):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False, index=True)
    address = Column(String(500), nullable=False)
    inn = Column(Integer, unique=True, nullable=True)
    ogrn = Column(Integer, unique=True, nullable=True)

    def __repr__(self):
        return self.name


class Courier(Model):
    id = Column(Integer, primary_key=True, index=True)
    passport_data = Column(String(250), nullable=False)


class Order(Model):
    id = Column(Integer, primary_key=True, index=True)
    id_list_products = Column(Integer, primary_key=True)
    id_seller = Column(Integer, primary_key=True, index=True)
    state = Column(String, nullable=False)

    # def hash(self):


class Cart(Model):
    id_list_products = Column(Integer, primary_key=True)

    # def IsOrdered(self):