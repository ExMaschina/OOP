import pytest
from src.classes import Category, Product

"""Проверка корректности инициализации классов Category и Product"""

"""Класс Catedory"""


@pytest.fixture
def category_products():
    return Category('Milk products', 'healthy foods', 'Milk, cheese', 5, 2)


def test_init_category(category_products):
    assert category_products.name == 'Milk products'
    assert category_products.description == 'healthy foods'
    assert category_products.products == 'Milk, cheese'
    assert category_products.category_quantity == 5
    assert category_products.unic_prod_quantity == 2


"""Класс Product"""


@pytest.fixture
def producted():
    return Product('Milk', 'from cow', 100, 15)


def test_init_product(producted):
    assert producted.name == 'Milk'
    assert producted.description == 'from cow'
    assert producted.price == 100
    assert producted.quantity == 15


"""Тест подсчёта количества продуктов"""


@pytest.fixture
def quantity_product():
    return Product(None, None, None, 3)


def test_product_quantity(quantity_product):
    assert quantity_product.quantity == 3


"""Тест подсчёта количества категорий"""


@pytest.fixture
def counting_category():
    return Category(None, None, None, 3, None)


def test_category_counting(counting_category):
    assert counting_category.category_quantity == 3
