from enum import Enum


class ModificationSet(Enum):
    READ = 0
    WRITE = 1
    DELETE = 2 # delete what? a whole storage? A whole file?
    UPDATE = 3