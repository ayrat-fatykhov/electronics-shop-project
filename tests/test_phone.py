from src.phone import Phone


def test_repr():
    phone = Phone("Pixel 8", 100_000, 10, 1)
    assert repr(phone) == "Phone('Pixel 8', 100000, 10, 1)"
