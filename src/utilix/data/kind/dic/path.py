from typing import List
from utilix.data.kind.graph.path.basic import Basic as GraphBasicPath


class Path(GraphBasicPath):
    def __init__(self ,nodes:List[str]):
        self._nodes = nodes

