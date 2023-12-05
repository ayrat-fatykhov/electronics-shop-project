from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, sim_quantity: int):
        super().__init__(name, price, quantity)
        self._sim_quantity = sim_quantity

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self._sim_quantity})"

    @property
    def sim_quantity(self):
        return self._sim_quantity

    @sim_quantity.setter
    def sim_quantity(self, number):
        if number <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")
        self._sim_quantity = number
