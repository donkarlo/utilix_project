from utilix.data.storage.decorator.multi_valued.ram.value.startegy.continuous import Continuous
from utilix.data.storage.decorator.multi_valued.ram.value.startegy.discrete import Discrete


class Strategies:
    def __init__(self):
        self._all = []
        self._all.append(Continuous(), Discrete(), )

    def get_all():
        pass
