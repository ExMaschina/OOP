class Category:
    category_name: str
    category_description: str
    products: list

    gener_category_quantity = 0
    gener_unic_prod_quantity = 0

    def __init__(self, category_name, category_description, products):
        self.category_name = category_name
        self.category_description = category_description
        self.products = products

        Category.gener_category_quantity += 1
        quantity = len(set(product for product in self.products))
        Category.gener_unic_prod_quantity += quantity


class Product:
    product_name: str
    product_description: str
    price: float
    prod_quantity_in_stock: int

    def __init__(self, product_name, product_description, price, prod_quantity_in_stock):
        self.product_name = product_name
        self.product_description = product_description
        self.price = price
        self.prod_quantity_in_stock = prod_quantity_in_stock
