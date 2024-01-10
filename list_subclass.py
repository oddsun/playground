"""
desc
"""

from typing import TypeVar, List

T = TypeVar('T')


class BetterList(List[T]):
    """A custom list subclass that provides additional functionality."""

    def __init__(self, *args: T):
        super().__init__(args)


class IntList(BetterList[int]):
    """A custom list subclass specifically for integers."""
    pass


class StrList(BetterList[str]):
    """A custom list subclass specifically for strings."""
    pass


i = IntList('1')
s = StrList(1, 2, 3)

for j in i:
    print(j)
