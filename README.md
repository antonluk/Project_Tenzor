# Project_Tenzor
Сервис по агрегации кафе быстрого питания класса "Шаверма"(Шаурмечные) + кофе, в функцией доставки до дома.
Аналог Delivery club, но только для шаурмечных и кофейн.


CRUD по основным сущностям:

+ Пользователь
+ Продукт
+ Корзина
+ Очередь доставки
+ АдресДоставки

```
User
  Admin
  Moderator
  Courier
  Client
    type - тип пользователя(админ, модератор, курьер, клиент)
    name(nickName) - ник
    firstName - имя
    lastName - фамилия
    middleName - отчество
    gender - пол
    birthDate - день рождения
    email - почта
    phone - телефон
    address - дефолтный адрес доставки

Product - продукт
  type - тип продукта
  category - категория
  name - наименование
  description - описание
  count - кол-во на складе
  price - цена за еденицу
  photo - картинка продукта
  status - enable||disable

Card - корзина
  user - пользователь ID
  item - продукт ID
  name - название
  date - время покупки
  count - кол-во
  price - общая цена
  deliveryAddress - адрес доставки
  description - описание
  status - активно, доставленно, отменено

DeliveryQueue - очередь на доставку
  item - что 
  address - куда
  deliveryTime - время доставки
  courier - кто доставляет
  status - активно, доставленно, отменено

DeliveryAddress
  id
  cityId - id города
  districtId - id района
  street - улица
  houseNumber - номер дома
  courpus - корпус
  build - строение
  apartmentNumber - номер квартиры
  porch - подъезд

City
  id
  name
  districtId
  
District
  id
  cityId
  name

```
