"""Класс Category"""
class Category:
    name: str  # атрибуты (свойства) класса
    description: str
    products: int

    category_quantity = 0
    unic_prod_quantity = 0

    def __init__(self, name, description, products, category_quantity, unic_prod_quantity):  # конструктор
        self.name = name
        self.description = description
        self.__products = products
        self.category_quantity = category_quantity
        self.unic_prod_quantity = unic_prod_quantity

        Category.category_quantity += 1
        quantity = len(set(product.name for product in self.__products))
        self.unic_prod_quantity += quantity


    # @property
    # def products(self):
    #     return self.__products
    #
    # @property
    # def goods(self):
    #     product_list = []
    #     for product in self.__products:
    #         product_list.append(f'{product.name}, {int(product.price)} руб. Остаток: {product.quantity} шт.')
    #     return product_list
    #
    # def add_products(self, product):
    #     self.__products.append(product)



"""Класс Product"""

class Product:
    name: str
    description: str
    price: float
    quantity: int  # количество в наличии
    product_list = []

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def product_quantity(self):
        return self.quantity

    def create_product(self, product):
        return product.append(product_list)

