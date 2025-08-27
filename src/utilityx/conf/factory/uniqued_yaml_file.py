from utilityx.conf.interface import Interface as ConfInterface
from utilityx.data.storage.factory.single_yaml_file import SingleYamlFile
from utilityx.os.path import Path
from utilityx.data.storage.type.file.file import File


class UniquedYamlFile(ConfInterface):
    """
    It is a configuration byuilder
    """
    def __init__(self, storage:SingleYamlFile):
        self._props = {}


        self._sorage:SingleYamlFile = storage

    def _do_init_props(self)->None:
        '''
        Returns:
        '''
        self._props = self._sorage.get_ram_dict()



    def get_props(self)->None:
        self._do_init_props()
        return self._props

if __name__ == '__main__':
    #this is the yaml file from sociomind
    syf = SingleYamlFile("/home/donkarlo/repo/sociomind_project/conf.yaml")
    ymc = UniquedYamlFile(syf)
    print(ymc.get_props())