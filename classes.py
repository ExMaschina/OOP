class Category:
    name: str  # атрибуты (свойства) класса
    description: str
    products: int
    category_quantity: int
    unic_prod_count: int

    def __init__(self, name, description, products, category_quantity, unic_prod_count):  # конструктор
        self.name = name
        self.description = description
        self.products = products
        self.category_quantity = category_quantity
        self.unic_prod_count = unic_prod_count

    def category_counting(self):
        return self.category_quantity


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def product_quantity(self):
        return self.quantity
