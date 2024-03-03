from classes import Category, Product
from abs_and_mixin import MixinRepr


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

    def new_product(self):
        pass

    def price(self):
        pass


class LawnGrass(Product, MixinRepr):
    manufacturer_country: str  # страна-производитель
    germination_period: float  # срок прорастания

    def __init__(self, name, description, price, color, quantity, manufacturer_country, germination_period):
        super().__init__(name, description, price, color, quantity)
        self.manufacturer_country = manufacturer_country
        self.germination_period = germination_period
        print(repr(self))
    def new_product(self):
        pass

    def price(self):
        pass


smart = Smartphone("iphone", "good", 55, "red", 43, 10000, "pro", 4000)
