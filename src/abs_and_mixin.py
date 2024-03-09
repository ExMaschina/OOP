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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f'Объект {self.name}; {self.description}, {self.price}, {self.color}, {self.quantity}, {self.manufacturer_country}, {self.germination_period}'
