from __future__ import annotations

from typing import (
    Generic, TypeVar, Callable, Iterable, Sequence, Mapping, Any
)

T = TypeVar("T")
Constructor = Callable[..., T] | type[T]


class CollectionManager(Generic[T]):
    """
    Hold and build a homogeneous collection of objects of type T.
    - Build many from (args tuples) or (kwargs dicts)
    - Optionally accept ready-made instances
    - Support random generation via a user-supplied generator function
    """

    def __init__(self, cls: Constructor):
        self._cls: Constructor = cls
        self._objects: list[T] = []

    # ---------- creation ----------
    def create_many(
            self,
            data: Iterable[Sequence[Any] | Mapping[str, Any] | T],
    ) -> list[T]:
        """
        Create objects from an iterable of:
          - Sequence[Any]  -> passed as *args
          - Mapping[str, Any] -> passed as **kwargs
          - T -> used as-is (already constructed)
        Returns only the newly created/appended objects.
        """
        created: list[T] = []
        for item in data:
            if isinstance(item, Mapping):
                obj = self._cls(**item)  # type: ignore[arg-type]
            elif isinstance(item, Sequence) and not isinstance(item, (str, bytes)):
                obj = self._cls(*item)  # type: ignore[misc]
            else:
                # assume it's already an instance of T
                obj = item  # type: ignore[assignment]
            self._objects.append(obj)
            created.append(obj)
        return created

    def create_random(
            self,
            n: int,
            generator: Callable[[int], T],
    ) -> list[T]:
        """
        Generate n items using the supplied generator(index) -> T.
        Avoids brittle class-name checks and keeps randomness policy outside.
        """
        created: list[T] = []
        for i in range(n):
            obj = generator(i)
            self._objects.append(obj)
            created.append(obj)
        return created

    # ---------- management ----------
    def add(self, obj: T) -> None:
        """Append a single instance."""
        self._objects.append(obj)

    def extend(self, objs: Iterable[T]) -> None:
        """Append multiple instances."""
        self._objects.extend(objs)

    def clear(self) -> None:
        """Remove all stored objects."""
        self._objects.clear()

    # ---------- access ----------
    def get_all(self) -> tuple[T, ...]:
        """Return an immutable snapshot of the collection."""
        return tuple(self._objects)

    def __iter__(self):
        yield from self._objects

    def __len__(self) -> int:
        return len(self._objects)

    def __getitem__(self, idx: int) -> T:
        return self._objects[idx]
