from utilix.conf.interface import Interface as ConfInterface
from utilix.data.storage.factory.single_yaml_file import SingleYamlFile


class UniquedYamlFile(ConfInterface):
    """
    It is a configuration byuilder
    """
    def __init__(self, storage:SingleYamlFile):
        self._props:dict = {}


        self._sorage:SingleYamlFile = storage

    def _do_init_props(self)->None:
        '''
        Returns:
        '''
        self._props = self._sorage.get_ram_dict()



    def get_props(self)->dict:
        self._do_init_props()
        return self._props