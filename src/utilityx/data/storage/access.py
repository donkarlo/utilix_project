from utilityx.data.storage.security.modification_set import ModificationSet


class Access:
    def __init__(self, modification:set[ModificationSet]):
        self._modification = modification