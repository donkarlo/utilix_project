from typing import List
from utilix.data.storage.interface import Interface as StorageInterface


class Interface(StorageInterface):
    def get_values_by_slice(self, slc:slice)->List:
        """
        Retirns a list of strings as document
        Args:
            slc:

        Returns:

        """
        ...