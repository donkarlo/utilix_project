from nd_utility.data.storage.storage import Storage


class Dir(Storage):
    def __init__(self,path:Union[str, OsPath]):
        self._path = path