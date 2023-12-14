import pytest

from src.phone import Phone


def test_repr():
    phone = Phone("Pixel 8", 100_000, 10, 1)
    assert repr(phone) == "Phone('Pixel 8', 100000, 10, 1)"


def test_sim_quantity_negative():
    """
    Тест проверяет, возвращается ли ошибка при не корректно переданных данных.
    """
    phone = Phone("Pixel 8", 100_000, 10, 1)
    with pytest.raises(ValueError) as err:
        phone.sim_quantity = 0.1
