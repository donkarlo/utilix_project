from utilityx.data.storage.decorator.decorator import Decorator


class MultiUnit(Decorator):
    """
    A kind of source full of  units such as a multi doc yaml file
    """
    def __init__(self, inner:Decorator, separator:str, single_unit:bool):
        """
        Args:
            inner:
            separator: holds the strategy for breaking string blob in the storage to units
        """
        super().__init__(inner)
        self._ram_units:list[str] = []
        self._separator = separator

    def add_to_ram_units_at(self, index: int, unit:str) -> bool:
        self._ram_units.insert(index, unit)


    def get_ram_slice(self, slice: slice) -> slice:
        return self._ram_units[slice]

    def add_ram_unit(self, unit:str):
        self._ram_units.append(unit)

    def earase_ram_units(self):
        self._ram_units = None

    @overrides
    def save(self):
        if self._separator is not None:
            self._ram = self._separator.join(self._ram_units)
        else:
            self._ram = "".join(self._ram_units)
        super().save()
