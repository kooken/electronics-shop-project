"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

@pytest.fixture
def item_test():
    return Item('laptop', 20000, 1)


def test_item_init(item_test):
    assert item_test.name == 'laptop'
    assert item_test.price == 20000
    assert item_test.quantity == 1


def test_item_total_price(item_test):
    assert item_test.calculate_total_price() == 20000

def test_item_apply_discount(item_test):
    assert item_test.apply_discount() == 20000