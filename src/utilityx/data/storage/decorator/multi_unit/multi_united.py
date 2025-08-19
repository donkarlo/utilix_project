from typing import override

from utilityx.data.storage.decorator.decorator import Decorator


class MultiUnited(Decorator):
    """
    A kind of source full of  units such as a multi doc yaml file
    """
    __slots__ = ("_ram_units", "_separator")

    def __init__(self, inner:Decorator, separator:str, single_unit:bool):
        """
        Args:
            inner:
            separator: holds the strategy for breaking string blob in the storage to units
        """
        super().__init__(inner)
        self._ram_units:list[str] = []
        self._separator = separator

    @override
    def save(self):
        if self._separator is not None:
            self._ram = self._separator.join(self._ram_units)
        else:
            self._ram = "".join(self._ram_units)
        super().save()

    def set_ram_units(self, ram_units:list[str]):
        self._ram_units = ram_units

    def get_ram_units(self):
        return self._ram_units

    def get_ram_unit_at(self, at:int):
        return self._ram_units[at]

    def add_to_ram_units_at(self, index: int, units: list[str]) -> None:
        for offset, unit in enumerate(units):
            self._ram_units.insert(index + offset, unit)


    def get_ram_slice(self, s: slice) -> list[str]:
        return self._ram_units[s]

    def add_ram_unit(self, unit:str):
        self._ram_units.append(unit)

    def earase_ram_units(self):
        self._ram_units.clear()

    def load_slice(self, s:slice) -> list[str]:
        return self._ram_units[s]


