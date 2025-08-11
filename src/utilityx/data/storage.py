from utilityx.data.storage.security import Security


class Storage:
    """
    Only discess the where the source is and how to unlock it
    """
    def __init__(self, security:Security):
        self._security = security