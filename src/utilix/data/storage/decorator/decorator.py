from typing import Any, override


from utilix.data.storage.interface import Interface as StorageInterface
from utilix.oop.design_pattern.structural.decorator.decorator import Decorator as BaseDecorator

class Decorator(BaseDecorator, StorageInterface):
    """
    Base storage decorator that forwards to an inner StorageInterface.
    """

    def __init__(self, inner: StorageInterface):
        """
        .__inner is either the most basic object, in this case pair_set.storage.basic.Yaml or a decorator
        Args:
            inner:
        """
        BaseDecorator.__init__(self, inner)

    @override
    def load(self) -> Any:
        return self._inner.load()

    @override
    def save(self) -> None:
        return self._inner.save()

    @override
    def set_ram(self,content:Any)->None:
        self._inner.set_ram(content)

    @override
    def add_to_ram(self, content:Any) -> None:
        self._inner.set_ram(self._inner.get_ram() + content)

    @override
    def earase(self) -> None:
        self._inner.earase()

    @override
    def earase_ram(self) -> None:
        self._inner.earase_ram()

    @override
    def get_ram(self) -> Any:
        return self._inner.get_ram()
