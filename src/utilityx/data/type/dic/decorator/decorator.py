from utilityx.data.type.dic.Interface import Interface as DicInterface


class Decorator(Interface):
    def __init__(self, inner: DicInterface):
        self._inner :DicInterface = inner