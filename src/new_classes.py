from classes import Category, Product
from abs_and_mixin import MixinRepr, AbsProd


class Smartphone(Product, MixinRepr):
    performance: int  # производительность
    model: str  # модель
    memory_capacity: int  # объём встроенной памяти

    def __init__(self, name, description, price, color, quantity, performance, model, memory_capacity):
        super().__init__(name, description, price, color, quantity)
        self.performance = performance
        self.model = model
        self.memory_capacity = memory_capacity
        print(repr(self))


    @classmethod
    def creates_product(cls, name, description, price, quantity, color, performance, model, memory_capacity):
        """Создание нового объекта товара и проверка совпадения нового объекта товара с текущим"""
        return cls(name, description, price, quantity, color, performance, model, memory_capacity)


class LawnGrass(Product, MixinRepr):
    manufacturer_country: str  # страна-производитель
    germination_period: float  # срок прорастания

    def __init__(self, name, description, price, color, quantity, manufacturer_country, germination_period):
        super().__init__(name, description, price, color, quantity)
        self.manufacturer_country = manufacturer_country
        self.germination_period = germination_period
        print(repr(self))


    @classmethod
    def creates_product(cls, name, description, price, color, quantity, manufacturer_country, germination_period):
        """Создание нового объекта товара и проверка совпадения нового объекта товара с текущим"""
        return cls(name, description, price, color, quantity, manufacturer_country, germination_period)


smart = Smartphone("iPhone", "good smartphone", 55, "red", 40, 10000, "pro", 4000)
print(smart)

grass = LawnGrass('grass', 'good grass', 2, 'green', 4, 'Germany', 4.5)
print(grass)

