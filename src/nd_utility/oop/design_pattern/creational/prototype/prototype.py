from abc import ABC, abstractmethod

class Prototype(ABC):
    @abstractmethod
    def get_clone(self):
        ...
