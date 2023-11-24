"""Здесь надо написать тесты с использованием pytest для модуля item."""
from settings import ITEMS_PATH
from src.item import Item


def test_instance_storage():
    item = Item("Оперативка", 2000, 5)
    assert Item.all == [item]


def test_calculate_total_price():
    item = Item("Процессор", 10000, 2)
    assert item.calculate_total_price() == 20000


def test_apply_discount():
    item = Item("Наушники", 5000, 7)
    Item.pay_rate = 0.5
    item.apply_discount()
    assert item.price == 2500


def test_instantiate_from_csv():
    Item.instantiate_from_csv(ITEMS_PATH)
    assert Item.all[0].name == "Смартфон"
    assert Item.all[0].price == 100.0
    assert Item.all[0].quantity == 1


def test_string_to_number():
    assert Item.string_to_number('3') == 3
