from typing import Any, Dict, List, Tuple, Union, Sequence, Optional, overload
from utilix.data.kind.dic.interface import Interface as DicInterface
import io
import matplotlib.pyplot as plt
from pprint import pprint

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
    def get_shortest_path(self, start: Key, target: Key, separator: Optional[str] = None) -> Union[str, List]:
        """
        Find the shortest path (in number of edges) from the node `start`
        down to a descendant key `target` in the nested dict structure.
        Returns a string like 'memory/long_term/explicit/episodic/experience'.

        The search assumes that the structure under this Dic is primarily
        nested dicts. Sets, lists and tuples are also handled in a minimal way:
        - For sets/tuples/lists, each element is treated as a child key with
          an empty dict as its subtree.
        """
        if start not in self._raw_dict:
            raise KeyError(f"Start key {start!r} not found at the top level.")

        subtree = self._raw_dict[start]
        current_path: List[Key] = [start]

        best_path: List[List[Key]] = []

        def add_candidate_path(candidate: List[Key]) -> None:
            if len(best_path) == 0:
                best_path.append(candidate)
            else:
                if len(candidate) < len(best_path[0]):
                    best_path[0] = candidate

        def iter_children(node: Any):
            # Yield (child_key, child_subtree)
            if isinstance(node, dict):
                for child_key, child_val in node.items():
                    yield child_key, child_val
            elif isinstance(node, (set, list, tuple)):
                # Treat elements as keys with empty dict as subtree
                for child_key in node:
                    yield child_key, {}
            else:
                # No children
                return

        def dfs(node: Any, path_so_far: List[Key]) -> None:
            for child_key, child_subtree in iter_children(node):
                new_path = path_so_far + [child_key]
                if child_key == target:
                    add_candidate_path(new_path)
                dfs(child_subtree, new_path)

        dfs(subtree, current_path)

        if len(best_path) == 0:
            raise KeyError(f"No path from start={start!r} to target={target!r} was found.")

        parts_as_str = [str(p) for p in best_path[0]]

        if separator is None:
            return parts_as_str
        else:
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
