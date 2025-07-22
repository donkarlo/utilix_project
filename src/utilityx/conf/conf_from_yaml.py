import yaml
from yaml import CLoader
from utilityx.conf.conf import Conf


class ConfFromYaml(Conf):
    def _do_init_props(self)->None:
        '''
        Returns:
        '''
        file_path = self.get_source().get_native_os_path()
        with open(file_path, "r") as file:
            self._props:dict = yaml.load(file, Loader=CLoader)