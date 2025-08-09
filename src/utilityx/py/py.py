import sys
from typing import Sequence


class Pyx:
    def __init__(self):
        pass

    @staticmethod
    def print_sys_paths():
        for p in sys.path:
            print(p)

    @staticmethod
    def get_sys_paths()->Sequence[str]:
        return sys.path