from typing import Any, override


from utilix.data.storage.interface import Interface as StorageInterface
from utilix.oop.design_pattern.structural.decorator.decorator import Decorator as BaseDecorator

class Decorator(BaseDecorator, StorageInterface):
    """
    Base storage decorator that forwards to an inner StorageInterface.
    """
    __slots__ = ("_inner",)

    def __init__(self, inner: StorageInterface):
        """
        .__inner is either the most basic object, in this case data.storage.basic.Yaml or a decorator
        Args:
            inner:
        """
        super(BaseDecorator,self).__init__(inner)

    @override
    def load(self) -> str:
        return self._inner.load()

    @override
    def save(self) -> bool:
        return self._inner.save()

    @override
    def set_ram(self,content:str)->None:
        self._inner.set_ram(content)

    @override
    def add_to_ram(self, content:str) -> None:
        self._inner.set_ram(self._inner.get_ram() + content)

    @override
    def earase_storage(self) -> bool:
        self._inner.earase_storage()

    @override
    def earase_ram(self) -> bool:
        self._inner.earase_ram()

    @override
    def get_ram(self) -> str:
        return self._inner.get_ram()
