"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_calculate_total_price():
    item = Item("Процессор", 10000, 2)
    assert item.calculate_total_price() == 20000


def test_apply_discount():
    item = Item("Наушники", 5000, 7)
    Item.pay_rate = 0.5
    item.apply_discount()
    assert item.price == 2500
