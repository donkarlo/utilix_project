from utilityx.data.storage.access import Access


class Storage:
    def __init__(self, access:Access=None):
        self._access = access