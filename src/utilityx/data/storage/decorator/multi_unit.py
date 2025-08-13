from utilityx.data.storage import Storage


class MultiUnit(Decorator):
    """
    A kind of source full of  units such as a multi doc yaml file
    """
    def __init__(self, inner:Storage, separator:str):
        """
        Args:
            inner:
            separator: holds the strategy for breaking string blob in the storage to units
        """
        super().__init__(inner)
        self._ram_memory_units:list[str] = []
        self._separator = separator

    def add_to_memory_content_at(self, index: int, unit: str) -> bool:
        self._ram_memory_units.insert(index, unit)


    def get_slice(self, slice: slice) -> slice:
        pass

    def add_ram_memory_unit(self, unit:str):
        self._ram_memory_units.append(unit)

    def add_save_unit(self, unit:str):
        self.add_ram_memory_unit(unit)
