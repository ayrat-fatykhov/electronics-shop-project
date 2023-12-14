"""Здесь надо написать тесты с использованием pytest для модуля item."""
import csv

import pytest

from settings import ITEMS_PATH, ITEMS_NOT_COLON_PATH, ITEMS_NO_FILE_PATH
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


def test_item_magic_pepr():
    item = Item("Видеокарта", 30000, 3)
    assert repr(item) == "Item('Видеокарта', 30000, 3)"


def test_item_magic_str():
    item = Item("Видеокарта", 30000, 3)
    assert str(item) == "Видеокарта"


def test_add():
    item = Item("Роутер TP-Link", 5000, 25)
    assert item + item == 50


def test_instantiate_csv_error():
    assert Item.instantiate_from_csv(ITEMS_NOT_COLON_PATH) == 'Файл item.csv поврежден'


def test_instantiate_from_csv_error():
    with pytest.raises(FileNotFoundError):
        with open(ITEMS_NO_FILE_PATH, encoding="windows-1251") as csvfile:
            item = csv.DictReader(csvfile)
