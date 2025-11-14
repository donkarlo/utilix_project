import inspect
from functools import update_wrapper
from typing import Callable, Type


def _drop_self(sig: inspect.Signature) -> inspect.Signature:
    """Remove leading self/cls (if any) from the signature for fair comparison."""
    params = list(sig.parameters.values())
    if params and params[0].name in ("self", "cls"):
        params = params[1:]
    return inspect.Signature(params, return_annotation=sig.return_annotation)


class _OverrideDescriptor:
    """Descriptor that validates override against a specific base at class creation."""

    def __init__(self, func: Callable, base: Type):
        self.func = func
        self.base = base
        self.name = func.__name__
        update_wrapper(self, func)

    def __set_name__(self, owner: Type, name: str) -> None:
        # Validate that base actually defines the attribute
        if not hasattr(self.base, name):
            raise TypeError(
                f"{owner.__name__}.{name} marked as override of {self.base.__name__}, "
                f"but {self.base.__name__}.{name} does not exist."
            )

        base_attr = getattr(self.base, name)

        # Extract underlying callables in case of descriptors
        base_callable = base_attr.fget if isinstance(base_attr, property) else (
            base_attr.__func__ if isinstance(base_attr, (classmethod, staticmethod)) else base_attr
        )
        sub_callable = self.func

        if not callable(base_callable):
            raise TypeError(
                f"{owner.__name__}.{name} marked as override of {self.base.__name__}, "
                f"but {self.base.__name__}.{name} is not callable."
            )

        # Compare signatures (excluding self/cls)
        sig_base = _drop_self(inspect.signature(base_callable))
        sig_sub = _drop_self(inspect.signature(sub_callable))

        if sig_sub.parameters != sig_base.parameters:
            raise TypeError(
                f"Signature mismatch for {owner.__name__}.{name} overriding "
                f"{self.base.__name__}.{name}: {sig_sub} != {sig_base}"
            )

        # Optionally check return annotation (enforce exact match)
        if sig_sub.return_annotation != sig_base.return_annotation:
            raise TypeError(
                f"Return type mismatch for {owner.__name__}.{name} overriding "
                f"{self.base.__name__}.{name}: {sig_sub.return_annotation} != {sig_base.return_annotation}"
            )

        # Passed: keep method boundable via descriptor protocol

    def __get__(self, instance, owner):
        # Bind like a normal function (method)
        return self.func.__get__(instance, owner)


def override_from(base: Type):
    """Method decorator: perform override checks against `base` at class creation time."""

    def _decorate(func: Callable):
        return _OverrideDescriptor(func, base)

    return _decorate

if __name__== "__main__":
    class A:
        def do(self, x: int, y: int) -> int:
            return x + y

    class D:
        pass

    class C(A):
        pass

    class B(D,C):
        @override_from(D)
        def do(self, x: int, y: int) -> int:
            return x - y