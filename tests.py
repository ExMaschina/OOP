import pytest
from classes import Category, Product


"""
Проверка корректности инициализации классов Category и Product
"""

@pytest.fixture
def category_products():
    return Category('Milk products', 'healthy foods', 'Milk, cheese', 5, 2)

@pytest.fixture
def producted():
    return Product('Milk', 'from cow', 100, 15)


def test_init_category(category_products):
    assert category_products.name == 'Milk products'
    assert category_products.description == 'healthy foods'
    assert category_products.products == 'Milk, cheese'
    assert category_products.category_count == 5
    assert category_products.unic_prod_count == 2


def test_init_product(producted):
    assert producted.name == 'Milk'
    assert producted.description == 'from cow'
    assert producted.price == 100
    assert producted.count == 15


def check_count_prod()
"""Проверка корректности подсчёта количества продуктов"""
