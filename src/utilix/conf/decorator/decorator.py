from utilix.conf.interface import Interface


class Decorator(Interface):
    def __init__(self, inner: Interface) -> None:
        self._inner:Interface = inner

    def _do_init_props(self):
        self._inner._do_init_props()

    def __getattr__(self, name: str) -> Any:
        """
        Walk the inner chain to find missing attributes/methods.
        This will pass all the arguments
        """
        target: Any = self._inner
        while True:
            if hasattr(target, name):
                return getattr(target, name)
            target = getattr(target, "_inner", None)
            if target is None:
                break
        raise AttributeError(
            f"{type(self).__name__} and its inner chain have no attribute {name!r}"
        )
