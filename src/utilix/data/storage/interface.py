from typing import Protocol, Any

class Interface(Protocol):
    """
    - This class determines what is it to be a storage. Storage is accessing a static storage on hard and bring it to RAM mememory and write it back to the storage
    This class is an interface. Dont add anything other than abstract methods. if you need to add concrete properties and
    """
    _ram: str

    
    def load(self) -> None:
        """
        Loadsfrom storage to RAM
        Returns:

        """
        ...

    def save(self)->None:
        """saves what is inside _ram into the storage"""
        ...

    def earase_storage(self)->None:
        """
        earase the raw_value of the storage and not the storage i.e. not the file or DB themselves but their content
        Returns:

        """
        ...

    def  delete_storage(self)->None:
        """
        For example deletinga file
        Returns:

        """
        ...

    def earase_ram(self) -> None:
        ...

    def set_ram(self, ram:str)->None:
        ...

    def get_ram(self)->str:
        ...


