from enum import IntEnum
from functools import cache
from typing import Protocol, Any, TypeVar, Callable

from utilix.data.storage.storage import Storage  # base class (assumed)


class StaticFactory(IntEnum):
    FILE = 0
    DIR  = 1
    DB   = 2


# Storage builder protocol and registry
TStorage = TypeVar("TStorage", bound=Storage)

class StorageBuilder(Protocol):
    def __call__(self, *args: Any, **kwargs: Any) -> TStorage: ...


_REGISTRY: dict[StaticFactory, StorageBuilder] = {}


def register_factory(kind: StaticFactory) -> Callable[[StorageBuilder], StorageBuilder]:
    """Decorator to register a builder function for a specific kind."""
    def _wrap(fn: StorageBuilder) -> StorageBuilder:
        _REGISTRY[kind] = fn
        return fn
    return _wrap


# Default builders
@register_factory(StaticFactory.FILE)
def _build_file(path: str, **kwargs: Any) -> Storage:
    """
    Example:
        get_storage(StaticFactory.FILE, "/tmp/pair_set.bin", mode="rw")
    """
    from utilix.data.storage.type import File
    return File(path=path, **kwargs)


@register_factory(StaticFactory.DIR)
def _build_dir(path: str, **kwargs: Any) -> Storage:
    """
    Example:
        get_storage("dir", "/var/pair_set", create_if_missing=True)
    """
    from utilix.data.storage.type import Dir
    return Dir(path=path, **kwargs)


@register_factory(StaticFactory.DB)
def _build_db(conn: str, **kwargs: Any) -> Storage:
    """
    Example:
        get_storage(StaticFactory.DB, "postgresql://user:pass@host/db", pool_size=10)
    """
    from utilix.data.storage.type import Db
    return Db(conn=conn, **kwargs)


# Public API
def get_storage(kind: int | str | StaticFactory, /, *args: Any, **kwargs: Any) -> Storage:
    """
    Flexible factory that dispatches to kind-specific builders.

    Examples:
        f = get_storage(StaticFactory.FILE, "/tmp/a.bin")
        d = get_storage("dir", "/pair_set", create_if_missing=True)
        db = get_storage(StaticFactory.DB, "sqlite:///x.db", timeout=5)

    The required arguments are defined by each registered builder:
    - FILE, DIR: expect `str_path: str`
    - DB: expects `conn: str`
    """
    member = _coerce(kind)
    if member is None:
        raise ValueError(f"Unsupported kind: {kind!r}")

    builder = _REGISTRY.get(member)
    if builder is None:
        raise RuntimeError(f"No builder registered for kind: {member.name}")

    try:
        return builder(*args, **kwargs)
    except TypeError as e:
        # Clear error if arguments do not match the builder signature
        raise TypeError(f"{member.name} builder argument mismatch: {e}") from e


def is_supporting_type(kind: int | str | StaticFactory) -> bool:
    return _coerce(kind) is not None


@cache
def get_all_as_str_int_tuple() -> tuple[tuple[str, int], ...]:
    return tuple((m.name, m.value) for m in StaticFactory)


@cache
def get_all_as_str_tuple() -> tuple[str, ...]:
    return tuple(m.name for m in StaticFactory)


def _coerce(kind: int | str | StaticFactory) -> StaticFactory | None:
    """Map int/str/enum to StaticFactory, rejecting bool (bool is a subclass of int)."""
    if isinstance(kind, StaticFactory):
        return kind
    if isinstance(kind, int) and not isinstance(kind, bool):
        try:
            return StaticFactory(kind)
        except ValueError:
            return None
    if isinstance(kind, str):
        try:
            return StaticFactory[kind.upper()]
        except KeyError:
            return None
    return None
