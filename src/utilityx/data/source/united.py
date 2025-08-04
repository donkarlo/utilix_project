from utilityx.data.access import Access
from utilityx.data.source import Source


class United(Source):
    """A kind of source full of simillar  units such as a multi doc yaml file"""
    def __init__(self, type:SupportingType, format:SupportingFormat, access:Access)->None:
        super().__init__(type, format, access)

        #units
        self._units = []

    def add_unit(self, unit):
        self._units.append(unit)

    def add_save_unit(self, unit:Unit):
        self.add_unit()
        self.
