
class Product:
    _FIELDS_MAPPING = {
        'type': str,
        'category': str,
        'name': str,
        'description': str,
        'price': float,
        'photo': str
    }

    def __init__(self, product_type, category, name, description, price, photo):
        self.type = product_type
        self.category = category
        self.name = name
        self.description = description
        self.price = price
        self.photo = photo
