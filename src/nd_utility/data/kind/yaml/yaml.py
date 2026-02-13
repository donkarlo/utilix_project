from typing import Any, overload, Dict

from nd_utility.data.kind.dic.dic import Dic
from nd_utility.data.kind.core.kind import Kind
from nd_utility.data.kind.core.kinds import Kinds


class Yaml(Kind):
    def __init__(self):
        super().__init__(Kinds.YAML)

    def is_of_my_kind(self, value: Any):
        if isinstance(value, Dic):
            pass
