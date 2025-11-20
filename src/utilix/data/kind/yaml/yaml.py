from typing import Any, overload, Dict

from utilix.data.kind.dic.dic import Dic
from utilix.data.kind.kind import Kind
from utilix.data.kind.kinds import Kinds


class Yaml(Kind):
    def __init__(self):
        super().__init__(Kinds.YAML)

    @overload
    def validate(self, value: Dic):
        ...

    @overload
    def validate(self, value: Dict):
        ...

    @overload
    def validate(self, value: str):
        ...

    def is_of_my_kind(self, value: Any):
        if isinstance(value, Dic):
            pass
