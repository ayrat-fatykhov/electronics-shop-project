import csv


class InstantiateCSVError(Exception):

    def __init__(self, message):
        self.message = message


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

    def __repr__(self) -> str:
        """Показывает данные для отладки"""
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        """Показывет данные для пользователя"""
        return self.__name

    def __add__(self, other):
        """Складывает экземпляры класса по количеству товара в магазине"""
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        return None

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, short_name):
        self.__name = short_name[:10]

    @classmethod
    def instantiate_from_csv(cls, item_path: str) -> None:
        """
        Инициализируют экземпляры класса Item данными из файла src/items.csv
        """
        cls.all.clear()
        try:
            with open(item_path, encoding="windows-1251") as file:
                data = csv.DictReader(file)
                items = list(data)
                if len(items[0]) != 3:
                    raise InstantiateCSVError("Файл item.csv поврежден")
                else:
                    for item in items:
                        Item(
                            name=item['name'],
                            price=float(item['price']),
                            quantity=int(item['quantity'])
                        )
        except FileNotFoundError:
            print("Отсутствует файл item.csv")
        except InstantiateCSVError as ex:
            print(ex.message)
            return ex.message

    @staticmethod
    def string_to_number(number) -> int:
        """
        Возвращает число из числа-строки
        """
        return int(float(number))
