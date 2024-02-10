import os
import csv

class InstantiateCSVError(Exception):
    pass


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError()

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = int(self.price * self.quantity)
        return total_price

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
        return self.price


    @classmethod
    def instantiate_from_csv(cls):

        if not os.path.join(os.path.dirname(__file__), 'items.csv'):
            raise FileNotFoundError("Отсутствует файл item.csv")
        else:
            cls.all.clear()
        path = os.path.join(os.path.dirname(__file__), 'items.csv')
        with open(path, 'r', newline='\n', encoding='UTF-8') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            if item['name'] not in items or item['price'] not in items or item['quantity'] not in items:
                raise InstantiateCSVError("Файл item.csv поврежден")
            else:
                print(cls(name=item.get('name'),
                          price=item.get('price'),
                          quantity=item.get('quantity')))

    @staticmethod
    def string_to_number(string):
        return int(float(string))
