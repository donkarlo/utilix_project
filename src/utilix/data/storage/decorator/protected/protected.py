from utilix.data.storage.decorator.protected.modification.modification import Modification


class Protected(Decorator):
    """
    TODO:
    - Should be a decorator
    """
    def __init__(self, modification:Modification):
        self._modification = modification