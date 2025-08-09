from utilityx.data.storage.access import Access
from utilityx.data.storage.supporting_type import SupportingType
from utilityx.data.storage.format import SupportingFormat
from utilityx.data.source.interface import Interface

class Source(Interface):
    def __init__(self, type:SupportingType, format:SupportingFormat, access:Access):
        self._type = type
        self._format = format
        self._access = access

        # from source to python variable
        self._content = None


    def load_content(self) -> str:
        pass

    def save_content(self) -> bool:
        print("Saving:", self._content)
        return True

    def get_type(self)->SupportingType:
        return self._type

    def get_format(self)->SupportingFormat:
        return self._format

    def get_access(self)->Access:
        return self._access

    def add_to_content(self, content:str)->bool:
        self._content += content