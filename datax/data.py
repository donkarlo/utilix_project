from datax.format.Format import Format
from datax.type.Type import Type


class Data():
    def __init__(self, type:Type,format:Format):
        self._type = type
        self._format = format
