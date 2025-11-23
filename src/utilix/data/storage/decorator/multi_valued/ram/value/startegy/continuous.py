from utilix.data.storage.decorator.multi_valued.ram.value.startegy.strategy import Strategy


class Continuous(Strategy):
    """

    This is the normal ram value
    """
    def __init__(self):
        super().__init__(self.__class__.__name__)


