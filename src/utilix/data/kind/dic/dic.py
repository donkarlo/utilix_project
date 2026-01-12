from typing import Any, Dict, List, Tuple, Union, Sequence, Optional, overload
from utilix.data.kind.dic.interface import Interface as DicInterface
import io
import matplotlib.pyplot as plt
from pprint import pprint
from collections import deque

Key = Union[str, int]
KeySeq = Sequence[Key]


class Dic(DicInterface):
    @overload
    def __init__(self, raw_dict: Dict) -> None:
        pass

    @overload
    def __init__(self, raw_dict: "Dic") -> None:
        pass

    def __init__(self, raw_dict: Union[Dict, "Dic"]):
        if not isinstance(raw_dict, (dict, Dic)):
            raise TypeError(f"Dic expects dict, got {type(raw_dict).__name__}")

        if isinstance(raw_dict, Dic):
            self._raw_dict = raw_dict.get_raw_dict()
        else:
            self._raw_dict = raw_dict

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._raw_dict})"

    def get_raw_dict(self) -> Dict:
        return self._raw_dict

    def get_keys_values(self) -> List[Tuple[Key, Any]]:
        """
        Always wrap any dict value into Dic.
        Existing Dic instances are kept.
        """
        items: List[Tuple[Key, Any]] = []

        for key, value in self._raw_dict.items():
            # wrap dict into Dic
            if isinstance(value, Dic):
                wrapped = value
            elif isinstance(value, dict):
                wrapped = Dic(value)
            else:
                wrapped = value
            items.append((key, wrapped))

        return items

    def get_items(self) -> List[Tuple[Key, Any]]:
        return self.get_keys_values()

    def has_nested_keys(self, keys: List[Key]) -> bool:
        current: Any = self._raw_dict
        for k in keys:
            if isinstance(current, dict) and k in current:
                current = current[k]
            else:
                return False
        return True

    def __getitem__(self, key_or_keys: Union[Key, KeySeq]) -> Any:
        if isinstance(key_or_keys, (str, int)):
            keys: Tuple[Key, ...] = (key_or_keys,)
        elif isinstance(key_or_keys, (list, tuple)):
            keys = tuple(key_or_keys)
        else:
            raise TypeError("Key must be str/int or a list/tuple of them.")

        current: Any = self._raw_dict
        for k in keys:
            if isinstance(current, Dic):
                current = current._raw_dict

            if isinstance(current, dict):
                if isinstance(k, str):
                    if k in current:
                        current = current[k]
                    else:
                        raise KeyError(f"Key path {keys} not found.")
                elif isinstance(k, int):
                    values_list = list(current.values())
                    try:
                        current = values_list[k]
                    except IndexError:
                        raise KeyError(f"Dict index {k} out of range.")
                else:
                    raise TypeError("Dict key must be str or int.")
            elif isinstance(current, list):
                if not isinstance(k, int):
                    raise TypeError("List indices must be integers.")
                try:
                    current = current[k]
                except IndexError:
                    raise KeyError(f"List index {k} out of range.")
            else:
                raise TypeError(f"Cannot index into {type(current).__name__}.")

        if isinstance(current, Dic):
            current = current._raw_dict
        return Dic(current) if isinstance(current, dict) else current

    def add_key_value(self, key: Key, value: Any, create_if_key_not_exists: bool) -> None:
        if create_if_key_not_exists or key in self._raw_dict:
            self._raw_dict[key] = value
        else:
            raise KeyError("The key does not exist.")

    def add_values_to_key(self, key: Key, values: List[Any], create_if_key_not_exists: bool) -> None:
        """
        Ensure the value at `key` is a list and extend it with `values`.
        """
        if key not in self._raw_dict:
            if not create_if_key_not_exists:
                raise KeyError("The key does not exist.")
            self._raw_dict[key] = []

        existing = self._raw_dict[key]
        if existing is None:
            self._raw_dict[key] = []
        elif not isinstance(existing, list):
            self._raw_dict[key] = [existing]

        self._raw_dict[key].extend(values)

    def get_keys(self) -> List[Key]:
        return self._raw_dict.keys()

    def get_values(self) -> List[Any]:
        return list(self._raw_dict.values())

    # -----------------------------
    # NEW: shortest path in nested dict
    # -----------------------------
    def get_unique_shortest_path_from_top_to_bottom(self, top: Key, bottom: Key, separator: Optional[str] = None) -> \
    Union[str, List]:
        """
        Find a unique shortest path (fewest edges) from a node `top` to a descendant key `bottom`.
        Unlike the previous version, `top` may appear anywhere in the tree, not only at top-level.

        If multiple different paths share the same shortest length, a ValueError is raised
        because the path is not unique.
        """

        def unwrap(node: Any) -> Any:
            if isinstance(node, Dic):
                return node.get_raw_dict()
            return node

        def iter_children(node: Any):
            node = unwrap(node)

            if isinstance(node, dict):
                for child_key, child_subtree in node.items():
                    yield child_key, child_subtree
                return

            if isinstance(node, (set, list, tuple)):
                for child_key in node:
                    yield child_key, {}
                return

            return

        def find_all_start_occurrences() -> List[Tuple[List[Key], Any]]:
            occurrences: List[Tuple[List[Key], Any]] = []

            root_node = self._raw_dict
            root_node = unwrap(root_node)

            if isinstance(root_node, dict):
                initial_items = list(root_node.items())
            else:
                initial_items = []

            stack: List[Tuple[Any, List[Key]]] = []
            for top_key, top_subtree in initial_items:
                stack.append((top_subtree, [top_key]))
                if top_key == top:
                    occurrences.append(([top_key], top_subtree))

            while len(stack) > 0:
                node, path_to_node = stack.pop()
                for child_key, child_subtree in iter_children(node):
                    child_path = path_to_node + [child_key]
                    if child_key == top:
                        occurrences.append((child_path, child_subtree))
                    stack.append((child_subtree, child_path))

            return occurrences

        def shortest_path_from_subtree(start_subtree: Any) -> Optional[List[Key]]:
            queue = deque()
            queue.append((start_subtree, [top]))

            best_path: Optional[List[Key]] = None

            while len(queue) > 0:
                node, path_so_far = queue.popleft()

                if best_path is not None:
                    if len(path_so_far) >= len(best_path):
                        continue

                for child_key, child_subtree in iter_children(node):
                    new_path = path_so_far + [child_key]
                    if child_key == bottom:
                        if best_path is None:
                            best_path = new_path
                        else:
                            if len(new_path) < len(best_path):
                                best_path = new_path
                            elif len(new_path) == len(best_path) and new_path != best_path:
                                raise ValueError(
                                    f"Shortest path is not unique from top={top!r} to bottom={bottom!r}.")
                        continue
                    queue.append((child_subtree, new_path))

            return best_path

        start_occurrences = find_all_start_occurrences()
        if len(start_occurrences) == 0:
            raise KeyError(f"Start key {top!r} was not found anywhere in the tree.")

        global_best: Optional[List[Key]] = None

        for _, start_subtree in start_occurrences:
            candidate = shortest_path_from_subtree(start_subtree)
            if candidate is None:
                continue

            if global_best is None:
                global_best = candidate
            else:
                if len(candidate) < len(global_best):
                    global_best = candidate
                elif len(candidate) == len(global_best) and candidate != global_best:
                    raise ValueError(
                        f"Shortest path is not unique from top={top!r} to bottom={bottom!r} across multiple top occurrences.")

        if global_best is None:
            raise KeyError(f"No path from top={top!r} to bottom={bottom!r} was found.")

        parts_as_str = [str(p) for p in global_best]
        if separator is None:
            return parts_as_str
        return separator.join(parts_as_str)

    def wrap_as_parent(self, parent_key: Key, child_key: Optional[Key] = None) -> None:
        """
        Wrap the current raw dict under a new parent key.

        If child_key is None:
            self._raw_dict becomes {parent_key: self._raw_dict}
        If child_key is given:
            self._raw_dict must contain child_key at top level and becomes:
                {parent_key: {child_key: <old_subtree>}}
        """
        if child_key is None:
            self._raw_dict = {parent_key: self._raw_dict}
            return

        if child_key not in self._raw_dict:
            raise KeyError(f"Child key {child_key!r} not found at top level.")

        subtree = self._raw_dict[child_key]
        self._raw_dict = {parent_key: {child_key: subtree}}

    def build_graphviz_tree(self) -> "Digraph":
        from graphviz import Digraph

        dot = Digraph(comment="Dic tree", name="dic_tree")
        dot.graph_attr["dpi"] = "300"

        counter = {"n": 0}

        def new_id() -> str:
            counter["n"] += 1
            return f"n{counter['n']}"

        def walk(node: Any, parent_id: str) -> None:
            # unwrap Dic
            if isinstance(node, Dic):
                node = node.get_raw_dict()

            # ---------- CASE 1: dict ----------
            if isinstance(node, dict):
                for k, v in node.items():
                    node_id = new_id()
                    dot.node(node_id, label=str(k))
                    dot.edge(parent_id, node_id)
                    walk(v, node_id)

            # ---------- CASE 2: list / tuple / set ----------
            elif isinstance(node, (list, tuple, set)):
                for index, item in enumerate(node):
                    index_id = new_id()
                    dot.node(index_id, label=f"[{index}]")
                    dot.edge(parent_id, index_id)
                    walk(item, index_id)

            # ---------- CASE 3: LEAF ----------
            else:
                leaf_id = new_id()
                dot.node(leaf_id, label=repr(node), shape="box")
                dot.edge(parent_id, leaf_id)

        # select root
        if isinstance(self._raw_dict, dict) and len(self._raw_dict) == 1:
            (top_key, top_val), = self._raw_dict.items()
            root_id = new_id()
            dot.node(root_id, label=str(top_key))
            walk(top_val, root_id)
        else:
            root_id = new_id()
            dot.node(root_id, label="root")
            walk(self._raw_dict, root_id)

        return dot

    def draw(self, format: str = "png") -> None:
        """
        Render the Graphviz tree in memory and display it using matplotlib.

        No files are written to disk.
        """


        dot = self.build_graphviz_tree()
        img_bytes = dot.pipe(format=format)
        img = plt.imread(io.BytesIO(img_bytes), format=format)

        plt.figure(figsize=(16, 16), dpi=300)
        plt.imshow(img)
        plt.axis("off")
        plt.tight_layout()
        plt.show()

    def __contains__(self, key: Key) -> bool:
        return key in self._raw_dict

    def __iter__(self):
        return iter(self._raw_dict)

    def print(self)->None:
        pprint(self._raw_dict)
