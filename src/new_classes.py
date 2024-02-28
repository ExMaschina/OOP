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

    def new_product(self):
        pass

    def price(self):
        pass

    def __repr__(self):
        return f'Объект {self.name} с атрибутами {self.description}, {self.price}, {self.color}, {self.quantity}, {self.performance}, {self.model}, {self.memory_capacity}.'


class LawnGrass(Product):
    manufacturer_country: str  # страна-производитель
    germination_period: float  # срок прорастания

    def __init__(self, name, description, price, color, quantity, manufacturer_country, germination_period):
        super().__init__(name, description, price, color, quantity)
        self.manufacturer_country = manufacturer_country
        self.germination_period = germination_period

    def new_product(self):
        pass

    def price(self):
        pass

    def __repr__(self):
        return f'Объект {self.name} с атрибутами {self.description}, {self.price}, {self.color}, {self.quantity}, {self.manufacturer_country}, {self.germination_period}.'


class MixinRepr:

    def __init__(self):
        self.name = self.name
        self.description = self.description
        self.price = self.price
        self.color = self.color
        self.quantity = self.quantity
        self.manufacturer_country = self.manufacturer_country
        self.germination_period = self.germination_period
        self.performance = self.performance
        self.model = self.model
        self.capacity = self.capacity

    def repr_out(self):
        print(f'Объект {self.name}; {self.description}, {self.price}, {self.color}, {self.quantity}, {self.manufacturer_country}, {self.germination_period}')
