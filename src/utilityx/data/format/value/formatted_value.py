class FormattedValue(ABC):
    def __init__(self, format: Format, value:Union[Value, str]):
        self._format = format
        self._value = value
