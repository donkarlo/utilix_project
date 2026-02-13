from typing import List, Optional

import sys
from abc import ABC, abstractmethod

class Cli(ABC):
    def __init__(self, faked_argv:Optional[List[str]]=None):
        if faked_argv != None:
            self._program = faked_argv[0]
            self._args = faked_argv[1:]
        else:
            self._program = sys.argv[0]
            self._args = sys.argv[1:]

    @abstractmethod
    def run(self):
        pass

    def get_program(self) -> str:
        return self._program

    def get_args(self) -> List[str]:
        return self._args

    def get_program_args(self) -> List[str]:
        return [self._program]+self._args


