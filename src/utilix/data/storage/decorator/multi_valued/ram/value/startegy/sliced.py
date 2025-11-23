from utilix.data.storage.decorator.multi_valued.ram.value.startegy.strategy import Strategy


class Sliced(Strategy):
    def __init__(self):
        """
        For caching
        """
        super().__init__(self.__class__.__name__)