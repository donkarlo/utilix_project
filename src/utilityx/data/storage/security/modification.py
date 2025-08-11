from enum import Enum


class Modification(Enum):
    READ = 0
    WRITE = 1
    DELETE = 2
    UPDATE = 3