from typing import Type, List

class Categorized:
    def __init__(self, allowed_klasses:List[Type]):
        self.__allowed_klasses = allowed_klasses

