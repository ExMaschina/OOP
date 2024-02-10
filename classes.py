class Category:
    name: str  # атрибуты (свойства) класса
    description: str
    products: int
    category_count: int
    unic_prod_count: int

    def __init__(self, name, description, products, category_count, unic_prod_count):  # конструктор
        self.name = name
        self.description = description
        self.products = products
        self.category_count = category_count
        self.unic_prod_count = unic_prod_count


class Product:
    name: str
    description: str
    price: float
    count: int

    def __init__(self, name, description, price, count):
        self.name = name
        self.description = description
        self.price = price
        self.count = count
