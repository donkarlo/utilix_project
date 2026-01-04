from typing import List, Optional, Any


class SlidingWindow:
    def __init__(self, sequence: List[Any], size: int):
        if size <= 0:
            raise ValueError("size must be a positive integer")
        if len(sequence) == 0:
            raise ValueError("sequence must not be empty")
        if size > len(sequence):
            raise ValueError("size must not be greater than len(sequence)")

        self._sequence = sequence
        self._size = size
        self._windows: Optional[List[List[Any]]] = None

    def get_windows(self) -> List[List[Any]]:
        if self._windows is None:
            self._windows = self._build_windows()
        return self._windows

    def _build_windows(self) -> List[List[float]]:
        windows: List[List[Any]] = []
        last_start_index = len(self._sequence) - self._size
        for start_index in range(0, last_start_index + 1):
            end_index = start_index + self._size
            windows.append(self._sequence[start_index:end_index])
        return windows
