from utilix.data.storage.decorator.protected.modificationed.modificationed import Modificationed


class Protected(Decorator):
    """
    TODO:
    - Should be a decorator
    """
    def __init__(self, modification:Modificationed):
        self._modification = modification