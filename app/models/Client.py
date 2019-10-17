
class Client:
    _FIELDS_MAPPING = {
        'client_id': int,
        'nick_name': str,
        'first_name': str,
        'last_name': str,
        'middle_name': str,
        'gender': str,
        'birth_date': str,
        'email': str,
        'phone': str,
        'address': str,
        'city_id': int,
        'district_id': int
    }

    def __init__(self, client_id, nick_name, first_name, last_name, middle_name, gender, birth_date, email, phone, address, city_id, district_id):
        self.client_id = client_id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender
        self.birth_date = birth_date
        self.email = email
        self.phone = phone
        self.address = address
        self.city_id = city_id
        self.district_id = district_id

    @staticmethod
    # @classmethod
    def get_client_mock():
        return {
            'id': 51,
            "nick_name": 'vasyaPupKun',
            "first_name": 'Вася',
            "last_name": 'Пупкин',
            "middle_name": 'Иванович',
            "gender": 'man',
            "birth_date": '1951-03-09',
            "email": 'golubinaya@pochta.ru',
            "phone": '+84333777742',
            "address": 'Республики 145',
            "city_id": 23,
            "district_id": 445
        }

#
# def get_client_mock():
#     return None
