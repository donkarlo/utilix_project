from typing import override

from utilityx.data.format.format import Format as DataFormat
from utilityx.data.storage.decorator.decorator import Decorator
from utilityx.data.storage.decorator.multi_valued.multi_valued import MultiValue


class Formatted(Decorator):
    """
    - This meaningful only for multi units
    - To check each value to have the same data type as other units.
    - We do not validate when loading, because we expect it tobe validated
    """
    def __init__(self, inner:MultiValue, format:DataFormat):
        # to make sure that the units match
        if not isinstance(inner, MultiValue):
            raise TypeError(f"SingleDataFormat requires a MultiUnit, got {type(inner).__name__}")
        super().__init__(inner)
        self._format = format

    @override
    def save(self) -> bool:
        for i, value in enumerate(self._inner._ram_values):
            if not self._format.validate_value(value):
                raise ValueError(f"Unit #{i} is not valid for the specified format.")
        return self._inner.save()

    def add_value(self, value:str)->bool:
        if not self._format.validate_value(value):
            raise ValueError(f"Unit is not valid for the specified format.")

        return self._inner.add_value(value)