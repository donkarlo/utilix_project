from utilityx.data.storage import Storage


class Dir(Storage):
    def __init__(self,path:Union[str, OsPath]):
        self._path = path