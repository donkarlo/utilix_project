


class Structure:
    """
    Utility to generate a stable unique name for a class
    based on its module, qualname and __init__ signature
    (including type hints).
    """

    def __init__(self, klass:type):
        self._klass = klass

    def get_klass(self)->type:
        return self._klass

