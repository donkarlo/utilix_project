from enum import Enum


class Kinds(Enum):
    """

    """
    READ = 0 # must be always readable unless it has no
    WRITE = 1
    DELETE = 2 # delete what? a whole storage? A whole file?
    UPDATE = 3