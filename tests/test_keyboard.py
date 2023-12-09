from src.keyboard import Keyboard


def test_language():
    item = Keyboard("Asus", 1000, 20)
    assert item.language == 'EN'


def test_change_lang():
    item = Keyboard("DEXP", 1500, 20)
    item.change_lang()
    assert item.language == 'RU'
