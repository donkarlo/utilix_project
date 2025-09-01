from utilityx.data.storage.interface import Interface as StorageInterface
from utilityx.os.path import Path
from utilityx.data.storage.type.file.file import File
from ruamel.yaml import YAML

class SingleYamlFile(StorageInterface):
    def __init__(self, file_path: str):
        self._ram: str | None = None #will not be used
        self._ram_dict: Dict[str, None] = None
        self._storage:StorageInterface = File(Path(file_path))
        self._yaml = YAML(typ="safe")  # plain Python types
        self._yaml.explicit_start = True

    def load(self) -> None:
        if self._ram_dict is None:
            self.load_dict()
        self._ram = str(self._ram_dict)

    def load_dict(self) -> None:
        with open(self.__get_path(), "r") as stream:
            self._ram_dict = self._yaml.load(stream)

    def save(self) -> None:
        pass

    def earase_storage(self) -> None:
        pass

    def delete_storage(self) -> None:
        pass

    def earase_ram(self) -> None:
        pass

    def set_ram(self, ram: str) -> None:
        self._ram = ram

    def get_ram(self) -> str:
        if self._ram is None:
            self.load()
        return self._ram

    def get_ram_dict(self) -> str:
        if self._ram_dict is None:
            self.load_dict()
        return self._ram_dict

    def __get_path(self) -> str:
        #calls get_native_absolute_path from File
        return self._storage.get_native_absolute_path()

if __name__ == "__main__":
    syf = SingleYamlFile("/home/donkarlo/repo/sociomind_project/conf.yaml")
    print(type(syf.get_ram_dict()))



