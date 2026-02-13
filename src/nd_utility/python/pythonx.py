import sys
from typing import Sequence


class Pythonx:
    def __init__(self):
        pass

    @staticmethod
    def print_system_paths():
        for p in sys.path:
            print(p)

    @staticmethod
    def get_system_paths()->Sequence[str]:
        return sys.path