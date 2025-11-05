from typing import List


class Colection:
    def __init__(self, members: List) -> None:
        self._members = members

    def get_members(self) -> List:
        return self._members