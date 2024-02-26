from src.classes import Category, Product


class Smartphone(Product):
    performance: int  # производительность
    model: str  # модель
    memory_capacity: int  # объём встроенной памяти

    def __init__(self, name, description, price, color, quantity, performance, model, memory_capacity):
        super().__init__(name, description, color, price, quantity)
        self.performance = performance
        self.model = model
        self.memory_capacity = memory_capacity

    # def __add__(self, other):
    #     if not isinstance(other, Product):
    #         raise ValueError('Складывать можно только объекты Product и дочерние от них.')
    #     return (self.quantity * self.__price) + (other.quantity * other.__price)


class LawnGrass(Product):
    manufacturer_country: str  # страна-производитель
    germination_period: float  # срок прорастания

    def __init__(self, name, description, price, color, quantity, manufacturer_country, germination_period):
        super().__init__(name, description, price, color, quantity)
        self.manufacturer_country = manufacturer_country
        self.germination_period = germination_period

    # def __add__(self, other):
    #     if isinstance(other, Product):
    #         return (self.quantity * self.__price) + (other.quantity * other.__price)
    #     else:
    #         return


