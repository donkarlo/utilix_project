from utilityx.data.storage.interface import Interface as StorageInterface

class Basic(StorageInterface):
    """
    This is the conceret Object of the Decorator pattern. Here it is not concerete because between what is in type
    - This is a single object if you want multi raw_value storage then multi_valued decoration
    """
    def __init__(self):
        # from source to python variable
        self._ram: str |  None = None

    def get_ram(self)->str:
        if self._ram is None:
            self._ram = self.load()
        return self._ram

    def set_ram(self, content:str):
        self._ram = content

    def earase_ram(self):
        self._ram = None