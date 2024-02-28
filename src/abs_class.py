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
