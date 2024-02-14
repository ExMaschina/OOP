import pytest

from src.classes import Category, Product


@pytest.fixture()
def electronic_category():
    return Category('Современные смартфоны', 'Современные смартфоны', ['Iphone 15', 'Iphone  15 Pro'])


def test_init_category(electronic_category):
    assert electronic_category.category_name == 'Современные смартфоны'
    assert electronic_category.category_description == 'Современные смартфоны'
    assert electronic_category.products == ['Iphone 15', 'Iphone  15 Pro']


def test_catergory_quantity():
    assert type(Category.gener_category_quantity) == int
    assert type(Category.gener_unic_prod_quantity) == int


@pytest.fixture()
def electronic_product():
    return Product('Iphone 15', 'Смартфон с USB-C-разъёмом', 85000.0, 10)


def test_init_product(electronic_product):
    assert electronic_product.product_name == 'Iphone 15'
    assert electronic_product.product_description == 'Смартфон с USB-C-разъёмом'
    assert electronic_product.price == 85000.0
    assert electronic_product.prod_quantity_in_stock == 10
