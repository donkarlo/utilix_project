class Contented:
    def __init__(self, content:str, type:Type):
        self._content = content
        self._type = type

    def get_content(self)->str:
        return self._content

    def get_type(self)->str:
        return self._type