from utilityx.data.storage.interface import Interface

from utilityx.data.storage.type.file import File

from utilityx.data.storage.decorator.multi_unit import MultiUnit

from utilityx.data.storage.decorator.single_data_type import SingleDataType
from utilityx.os.path import Path


class Factory:
    @staticmethod
    def get_multi_doc_yaml_file(file_path:str) -> Interface:
        file = File(Path(file_path))
        return SingleDataType(MultiUnit(file))

