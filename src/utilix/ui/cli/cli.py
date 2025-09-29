from typing import List

import sys
from abc import ABC, abstractmethod

class Cli(ABC):
    def __init__(self):
        self._program = sys.argv[0]
        self._args = sys.argv[1:]

    @abstractmethod
    def run(self):
        pass

    def get_program(self) -> str:
        return self._program

    def get_args(self) -> List[str]:
        return self._args


