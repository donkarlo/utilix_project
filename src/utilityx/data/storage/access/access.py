from utilityx.data.storage.access.modification.modification import Modification


class Access:
    def __init__(self, modification:Modification):
        self._modification = modification