from src.item import Item


class Phone(Item):
    """Класс для представления товара под категорией 'телефон'"""

    def __init__(self, name: str, price: float, quantity: int, sim_quantity: int):
        """Создание экземпляра класса Phone с атрибутами родительского класса Item"""
        super().__init__(name, price, quantity)
        self._sim_quantity = sim_quantity

    def __repr__(self):
        """Выводит наименование класса и атрибутами"""
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self._sim_quantity})"

    @property
    def sim_quantity(self):
        """Получает доступ к защищенному атрибуту (количество сим-карт)"""
        return self._sim_quantity

    @sim_quantity.setter
    def sim_quantity(self, number):
        """Вносит условие на количество сим-карт"""
        if number <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")
        self._sim_quantity = number
