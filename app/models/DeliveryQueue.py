
class DeliveryQueue:
    _FIELDS_MAPPING = {
        'items': list,
        'address': str,
        'delivery_time': str,
        'courier_name': str,
        'courier_phone': str
    }

    def __init__(self, items, address, delivery_time, courier_name, courier_phone):
        self.items = items
        self.address = address
        self.delivery_time = delivery_time
        self.courier_name = courier_name
        self.courier_phone = courier_phone
