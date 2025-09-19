from typing import override, TypeVar, Generic

from utilix.data.storage.type.file.format.format import Format as DataFormat
from utilix.data.storage.decorator.decorator import Decorator
from utilix.data.storage.decorator.multi_valued.multi_valued import MultiValued

class UniFormated(Decorator):
    """
    - This meaningful only for sliced_value units
    - To check each raw_value to have the same data type as other units.
    - We do not validate when loading, because we expect it tobe validated
    """
    def __init__(self, inner:MultiValued, format:DataFormat):
        # to make sure that the units match
        if not isinstance(inner, MultiValued):
            raise TypeError(f"SingleDataFormat requires a MultiUnit, got {type(inner).__name__}")
        super().__init__(inner)
        self._format = format

    @override
    def save(self) -> bool:
        for i, value in enumerate(self._inner.get_ram_values()):
            if not self._format.validate_value(value):
                raise ValueError(f"Value #{i} is not valid for the specified format.")
        #it actually runs the inner save
        super().save()

    def add_value(self, value:str)->bool:
        if not self._format.validate_value(value):
            raise ValueError(f"Unit is not valid for the specified format.")

        return self._inner.add_value(value)