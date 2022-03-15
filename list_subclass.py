"""
desc
"""

from typing import TypeVar, List

T = TypeVar('T')


class BetterList(List[T]):
    """ hi """

    def __init__(self, *args: T):
        super().__init__(args)


class IntList(BetterList[int]):
    """ hi """
    pass


class StrList(BetterList[str]):
    """ hi """
    pass


i = IntList('1')
s = StrList(1, 2, 3)

for j in i:
    print(j)
