from utilix.data.type.dic.interface import Interface as DicInterface
from utilix.data.type.dic.decorator.decorator import Decorator as DicDecorator


class IdAssigner(DicDecorator):
    def __init__(self, inner: DicInterface):
        super().__init__(inner)

    def get_paths_ids(self):
        pass

    def get_path_id(self):
        pass

    def __check_leaves_uniqness(self):
        pass