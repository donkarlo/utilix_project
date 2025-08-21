from utilityx.data.storage.basic import Basic
from utilityx.data.storage.type.file.file import File


class Pickloid(Basic):
    def __init__(self, file:File):
        self._file = file
