
class Courier:
    _FIELDS_MAPPING = {
        'first_name': str,
        'last_name': str,
        'email': str,
        'phone': str
    }

    def __init__(self, first_name, last_name, email, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
