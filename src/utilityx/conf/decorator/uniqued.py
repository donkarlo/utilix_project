from utilityx.conf.interface import Interface


class Uniqued(Decorator):
    """
    To give the basic unique ids
    """
    def __init__(self, inner:Interface):
        super().__init__(inner)
        self._counter = counter
        self._ids = []
        self._assign_ids()

    def _assign_ids(self) -> None:
        def walk(d: Dict[str, Any], prefix: str = "") -> None:
            for k, v in d.items():
                path = f"{prefix}/{k}" if prefix else k
                if isinstance(v, dict):
                    walk(v, path)
                else:
                    self._ids[path] = self._counter
                    self._counter += 1
        walk(self._inner._props)