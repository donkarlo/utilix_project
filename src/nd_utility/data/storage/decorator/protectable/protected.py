from nd_utility.data.storage.decorator.protected.modificationed.modificationed import Modificationed


class Protected(Decorator):
    """
    TODO:
    - Should be a decoration
    """
    def __init__(self, modification:Modificationed):
        self._modification = modification