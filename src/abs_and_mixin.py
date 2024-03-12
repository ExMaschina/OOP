from abc import ABC, abstractmethod


class AbsProd(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def creates_product(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __str__(self):
        pass


class MixinRepr:
    
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        object_attributes = f'Создан объект {self.__class__.__name__} '
        for k, v in self.__dict__.items():
            object_attributes += f'{k}: {v}; '
        return object_attributes
