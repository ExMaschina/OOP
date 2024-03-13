from typing import Any

from abs_and_mixin import AbsProd, MixinRepr


class Category:
    """Класс Category"""
    global result
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
        """Геттер, выводящий список товаров"""
        product_list = []
        for product in self.__products:
            product_list.append(f'{product.name}, {int(product.price)} руб. Остаток: {product.quantity} шт.')
        return product_list

    def add_products(self, product):
        if isinstance(product, Product):
            if product.quantity == 0:
                raise ValueError('Товар с нулевым количеством не может быть добавлен')
            self.__products.append(product)
            return self.__products
        raise TypeError('Добавить только продукт')

    def __len__(self):
        quant = 0
        for product in self.__products:
            quant += product.quantity
        return quant

    def average_price_products(self):
        """Метод подсчитывает средний ценник всех товаров"""
        try:
            average = [i.price for i in self.products()]
            return sum(average) / len(average)
        except ZeroDivisionError:
            return 0

    def __str__(self):
        return f'{self.name}, количество продуктов: {len(self)} шт.'

    def __repr__(self):
        return f"Category{self.name}; {self.description}; {self.products}"


class Product(MixinRepr, AbsProd):
    """Класс Product"""
    name: str  # название
    description: str  # описание
    price: float  # цена
    color: str  # цвет
    quantity: int  # количество в наличии
    product_list = []  #

    def __init__(self, name, description, price, color, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.color = color
        self.quantity = quantity
        if quantity < 1:
            raise ValueError('Товар с нулевым количеством не может быть добавлен')
        super().__init__()

    @classmethod
    def creates_product(cls, name, description, price, quantity, color):
        """Создание нового объекта товара и проверка совпадения нового объекта товара с текущим"""
        return cls(name, description, price, quantity, color)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
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
        if not isinstance(other, Product):
            raise ValueError('Складывать можно только объекты Product и дочерние от них.')
        return (self.quantity * self.__price) + (other.quantity * other.__price)


prod = Product("prod", "good", 50, 'white', 10)
print(prod)

