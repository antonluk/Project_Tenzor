
class Card:
    _FIELDS_MAPPING = {
        'nick_name': str,
        'items': list,
        'total_price': float,
        'address': str
    }

    def __init__(self, nick_name, items, address):
        self.nick_name = nick_name
        self.items = items
        self.address = address

    @property
    def total_price(self):
        total_price = 0
        for item in self.items:
            total_price += item.price
        return total_price
