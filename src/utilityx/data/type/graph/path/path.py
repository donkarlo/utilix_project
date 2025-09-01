from typing import List, Optional

from utilityx.data.type.graph.edge import Edge
from utilityx.data.type.graph.node import Node

class Path:
    def __init__(self, nodes: Optional[Node[List]] = [], edges: Optional[List[List[Edge]]] = []):
        self._nodes = nodes
        self._edges = edges