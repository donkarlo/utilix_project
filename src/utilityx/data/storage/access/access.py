from utilityx.data.storage.access.modification.modification import ModificationSet


class Access:
    def __init__(self, modification:set[ModificationSet]):
        self._modification = modification