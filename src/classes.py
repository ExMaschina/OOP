class Category:
    """Класс Category"""
    name: str  # название
    description: str  # описание
    products: int  # продукты

    category_quantity = 0  # общее количество категорий
    unic_prod_quantity = 0  # общее количество уникальных продуктов

    def __init__(self, name, description, products, category_quantity, unic_prod_quantity):  # конструктор
        self.name = name
        self.description = description
        self.__products = products
        self.category_quantity = category_quantity
        self.unic_prod_quantity = unic_prod_quantity

        Category.category_quantity += 1
        quantity = len(set(product.name for product in self.__products))
        self.unic_prod_quantity += quantity

    @property
    def products(self):
        return self.__products

    @property
    def goods(self):
        product_list = []
        for product in self.__products:
            product_list.append(f'{product.name}, {int(product.price)} руб. Остаток: {product.quantity} шт.')
        return product_list

    def add_products(self, product):
        self.__products.append(product)

    def __len__(self):
        return len(self.products)

    def __str__(self):
        return f'{self.name}, количество продуктов: {len(Product.product_list)} шт.'

    def __repr__(self):
        return f"Category{self.name}; {self.description}; {self.products}"


class Product:
    """Класс Product"""
    name: str  # название
    description: str  # описание
    price: float  # цена
    quantity: int  # количество в наличии
    product_list = []  #

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_list, name, description, price, quantity):
        """Возврат нового объекта товара и проверка совпадения нового объекта товара с текущим"""
        new_object = cls(name, description, price, quantity)

        for product in product_list:
            if product.name == new_object.name:
                product.quantity += new_object.quantity
                if new_object.price > product.price:
                    product.price = new_object.price
        return new_object

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self,price):
        if price > self.__price:
            self.__price = price
        elif price < 0 or price == self.__price:
            print("Цена введена некорректно.")
        else:
            while True:
                user_answer = input("Цена снижена. Установить эту цену?(yes-да, no-нет).")
                if user_answer == "yes":
                    self.__price = price
                    break
                elif user_answer == "no":
                    print("Цена не изменилась.")
                    break
                else:
                    print("Введите корректный ответ: 'yes' или 'no'.")

    def __str__(self):
        return f'{self.name}, {int(self.__price)} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        return (self.quantity * self.__price) + (other.quantity * other.__price)

    def __repr__(self):
        return f"Product{self.name}; {self.description}; {self.price}; {self.quantity}"
