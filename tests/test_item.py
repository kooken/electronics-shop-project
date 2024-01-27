"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
import os
import csv
from src.item import Item
from src.phone import Phone


@pytest.fixture
def item_test():
    return Item('laptop', 20000, 1)

@pytest.fixture
def phone_test():
    return Phone('iPhone', 100000, 5, 1)

def test_item_init(item_test):
    assert item_test.name == 'laptop'
    assert item_test.price == 20000
    assert item_test.quantity == 1


def test_item_total_price(item_test):
    assert item_test.calculate_total_price() == 20000

def test_item_apply_discount(item_test):
    assert item_test.apply_discount() == 20000

def test_item_name(item_test):
    assert item_test.name == "laptop"

def test_item2_name_setter():
    item = Item('bigkeyboard', 25000, 3)
    item.name = 'bigkeyboard'
    assert item.name == 'bigkeyboar'


def test_instantiate_from_csv():
    Item.instantiate_from_csv('src/items.csv')  # создание объектов из данных файла
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('5') == 5

def test_repr(item_test):
    assert item_test.__repr__() == "Item('laptop', 20000, 1)"

def test_str(item_test):
    assert item_test.__str__() == 'laptop'

def test_add(item_test, phone_test):
    assert item_test + phone_test

