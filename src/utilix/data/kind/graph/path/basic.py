from typing import List, Optional
from utilix.data.kind.graph.node import Node


class Basic:
    """
    This str_path just has nodes and it assumes that all edges are so equal that it is not necessary to mention them
    """
    def __init__(self, nodes: Optional[Node[List]] = None):
        if nodes is None:
            nodes = []
        self._nodes = nodes

    @classmethod
    def build_from_str(cls, raw_path_string: str, separator: str):
        str_nodes = raw_path_string.split(separator)
        nodes = []
        for str_node in str_nodes:
            nodes.append(Node(str_node))
        return cls(nodes)

    def add_node(self, node: Node):
        self._nodes.append(node)