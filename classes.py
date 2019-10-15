class Client:
    _FIELDS_MAPPING = {
        'nickname': str,
        'firstname': str,
        'lastname': str,
        'gender': str,
        'birthdate': str,
        'email': str,
        'phone': str,
        'adress': str,
        'bonus': int
    }

    def __init__(self, nickname, firstname, lastname, gender, birthdate, email, phone, adress):
        self.nickname = nickname
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.birthdate = birthdate
        self.email = email
        self.phone = phone
        self.adress = adress
        self.bonus = 0


class Admin:
    pass


class Moderator:
    pass


class Courier:
    _FIELDS_MAPPING = {
        'firstname': str,
        'lastname': str,
        'email': str,
        'phone': str
    }

    def __init__(self, firstname, lastname, email, phone):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phone = phone


class Product:
    _FIELDS_MAPPING = {
        'type': str,
        'category': str,
        'name': str,
        'description': str,
        'price': float,
        'photo': str
    }

    def __init__(self, type, category, name, description, price, photo):
        self.type = type
        self.category = category
        self.name = name
        self.description = description
        self.price = price
        self.photo = photo


class Card:
    _FIELDS_MAPPING = {
        'nickname': str,
        'items': list,
        'total_price': float,
        'adress': str
    }

    def __init__(self, nickname, items, adress):
        self.nickname = nickname
        self.items = items
        self.adress = adress

    @property
    def total_price(self):
        total_price = 0
        for item in self.items:
            total_price += item.price
        return total_price


class DeliveryQueue:
    _FIELDS_MAPPING = {
        'items': list,
        'adress': str,
        'deliverytime': str,
        'courier_name': str,
        'courier_phone': str
    }

    def __init__(self, items, adress, deliverytime, courier_name, courier_phone):
        self.items = items
        self.adress = adress
        self.deliverytime = deliverytime
        self.courier_name = courier_name
        self.courier_phone = courier_phone
