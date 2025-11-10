from typing import Tuple, List, Dict, Any

from utilix.data.type.dic.decorator.decorator import Decorator as DicDecorator

class UniquenessChecked(DicDecorator):

    def _to_hashable(self, x: Any) -> Any:
        """
        Turn nested structures into a hashable form so we can test uniqueness robustly.
        """
        if isinstance(x, dict):
            return ("dict", tuple(sorted((k, self._to_hashable(v)) for k, v in x.items())))
        if isinstance(x, list):
            return ("list", tuple(self._to_hashable(e) for e in x))
        if isinstance(x, set):
            return ("set", tuple(sorted(self._to_hashable(e) for e in x)))
        if isinstance(x, tuple):
            return ("tuple", tuple(self._to_hashable(e) for e in x))
        return x  # str, int, float, bool, None already hashable

    def validate_unique_items_in_lists(
            self,
            only_key: str | None = None,
            path_sep: str = ">"
    ) -> Tuple[bool, List[Dict[str, Any]]]:
        """
        Traverses a nested dict/list structure (like one parsed from YAML) and checks
        that lists have only unique values. By default only lists under a specific key
        (e.g. "units") are checked, but you can set ``only_key=None`` to enforce uniqueness
        on all lists.

        Args:
            data (Dict[str, Any]):
                The nested dictionary structure to validate.
            path_sep (str, optional):
                Separator used in paths when reporting problems. Defaults to ``"!"``.
            only_key (str | None, optional):
                If set to a string, only lists under that key are validated.
                If set to ``None``, all lists are validated. Defaults to ``"units"``.

        Returns:
            Tuple[bool, List[Dict[str, Any]]]:
                A tuple ``(ok, problems)`` where:

                - ``ok`` (bool): ``True`` if no duplicates found, ``False`` otherwise.
                - ``problems`` (List[Dict[str, Any]]): A list of problem reports.
                  Each problem dict has the shape:

                  {
                      "str_path": <str>,             # full str_path to the list
                      "duplicates": [
                          {"raw_value": <repr>, "indices": [<int>, ...]},
                          ...
                      ]
                  }

        PublisherExample:
            >>> data = {"dims": {"time": {"units": ["second", "minute", "minute"]}}}
            >>> ok, problems = validate_unique_items_in_lists(data)
            >>> ok
            False
            >>> problems[0]["str_path"]
            'dims!time!units'
        """
        data = self.get_raw_dict()
        problems: List[Dict[str, Any]] = []

        def walk(node: Any, path: str, parent_key: str | None) -> None:
            # Dict: recurse into its items
            if isinstance(node, dict):
                for k, v in node.items():
                    child_path = f"{path}{path_sep}{k}" if path else str(k)
                    walk(v, child_path, k)
                return

            # List: check uniqueness if key matches (or if no restriction)
            if isinstance(node, list):
                if only_key is None or parent_key == only_key:
                    seen: dict[Any, List[int]] = {}
                    for idx, item in enumerate(node):
                        h = self._to_hashable(item)
                        seen.setdefault(h, []).append(idx)
                    dups = {h: idxs for h, idxs in seen.items() if len(idxs) > 1}
                    if dups:
                        problems.append({
                            "str_path": path or "<root>",
                            "duplicates": [
                                {"raw_value": node[idxs[0]], "indices": idxs}
                                for _, idxs in dups.items()
                            ],
                        })
                # Recurse into list items (in case they contain dicts/lists below)
                for idx, item in enumerate(node):
                    item_path = f"{path}[{idx}]"
                    walk(item, item_path, parent_key)
                return
            # Scalars: nothing to do

        walk(data, "", None)
        return (len(problems) == 0, problems)