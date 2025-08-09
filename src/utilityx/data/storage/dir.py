class Dir(Type):
    def __init__(self,path:Union[str, OsPath]):
        self._path = path