class Factory:
    def __init__(self, values:List[List[Any]]):
        self._values = values
    def get_columned_rowed(self)->Tabular:
        return Columned(Rowed(Tabular(self._values)))