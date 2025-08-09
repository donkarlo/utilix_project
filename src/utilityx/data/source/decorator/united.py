from utilityx.data.source.interface import SourceDecorator, Source
from utilityx.data.source.decorator.partial import Partial
from utilityx.data.source.unit import Unit


class United(Decorator):
    """
    A kind of source full of simillar  units such as a multi doc yaml file
    """
    def __init__(self, inner:Source):
        super().__init__(inner)
        self._units = []

    def add_unit(self, unit:Unit):
        self._units.append(unit)

    def add_save_unit(self, unit:Unit):
        self.add_unit(unit)


if __name__ == "__main__":
    partial_united = United(Partial(Source()))