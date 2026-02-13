from typing import List, Optional

from nd_utility.data.kind.graph.edge import Edge
from nd_utility.data.kind.graph.node import Node

class Path:
    def __init__(self, nodes: Optional[Node[List]] = [], edges: Optional[List[List[Edge]]] = []):
        self._nodes = nodes
        self._edges = edges