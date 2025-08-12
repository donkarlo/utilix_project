from src.utilityx.data.storage import Storage


class United(Decorator):
    """
    A kind of source full of simillar  units such as a multi doc yaml file
    """
    def __init__(self, inner:Storage):
        super().__init__(inner)
        self._units = []

    def add_unit(self, unit:Unit):
        self._units.append(unit)

    def add_save_unit(self, unit:Unit):
        self.add_unit(unit)


if __name__ == "__main__":
    partial_united = United(Partial(Source()))