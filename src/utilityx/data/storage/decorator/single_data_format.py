from utilityx.data.format.format import Format as DataFormat
from utilityx.data.storage.decorator.decorator import Decorator
from utilityx.data.storage.decorator.multi_unit import MultiUnit


class SingleDataFormat(Decorator):
    """
    - This meaningful only for multi units
    - To check each unit to have the same data type as other units.
    """
    def __init__(self, inner:MultiUnit, format:DataFormat):
        super().__init__(inner)
        self._format = format

    def save(self)->bool:
        if self._format.validate_value(self._ram):
            super().save(self._ram)