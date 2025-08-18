from utilityx.data.storage.basic import Basic


class Dir(Basic):
    def __init__(self,path:Union[str, OsPath]):
        self._path = path