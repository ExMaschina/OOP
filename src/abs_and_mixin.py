from abc import ABC, abstractmethod


class AbsProd(ABC):

    @abstractmethod
    def new_product(self):
        pass

    @abstractmethod
    def price(self):
        pass

    def __repr__(self):
        pass


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
        print(
            f'Объект {self.name}; {self.description}, {self.price}, {self.color}, {self.quantity}, {self.manufacturer_country}, {self.germination_period}')
