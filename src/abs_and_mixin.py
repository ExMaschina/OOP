from abc import ABC, abstractmethod


class AbsProd(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __add__(self):
        pass

    @abstractmethod
    def new_product(self):
        pass

    @abstractmethod
    def price(self):
        pass

    def __repr__(self):
        pass


class MixinRepr:

    def __repr__(self):
        object_attributes = ''
        for k, v in self.__dict__.items():
            object_attributes += f'создан объект{self.__class__.__name__} {k}: {v},'
        return object_attributes

