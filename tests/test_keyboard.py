import pytest

from src.item import Item
from src.keyboard import Keyboard


@pytest.fixture
def item_test():
    return Item('laptop', 20000, 1)


@pytest.fixture
def keyboard_test():
    return Keyboard('Logitech G', 15000, 5)


def test_lang(keyboard_test):
    assert keyboard_test.language == 'EN'


def test_change_lang(keyboard_test):
    keyboard_test.change_lang()
    assert keyboard_test.language == 'RU'
    keyboard_test.change_lang()
    assert keyboard_test.language == 'EN'
