import pytest

from src.item import Item
from src.phone import Phone

@pytest.fixture
def item_test():
    return Item('laptop', 20000, 1)

@pytest.fixture
def phone_test():
    return Phone('iPhone', 100000, 5, 1)

def test_repr(phone_test):
    assert phone_test.__repr__() == "Phone('iPhone', 100000, 5, 1)"

def test_add(item_test, phone_test):
    assert item_test + phone_test == 6


def test_sim():
    phone1 = Phone('iPhone', 100000, 5, 1)
    assert phone1.number_of_sim == 1
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0