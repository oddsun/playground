from dataclasses import dataclass, InitVar, field
from typing import List


@dataclass(frozen=True)
class A:
    a: str = ''
    b: int = 0
    lst: List[int] = field(default_factory=list)
    config: InitVar[dict] = None

    def __post_init__(self, config: dict):
        if config:
            self.__init__(**config)


assert A(a='no', config={'a': 'hi', 'b': 1, 'config': {'a': 'ohmy'}}) == A(a='ohmy', b=0)
assert A(a='no', lst=[1, 2, 3], config={'a': 'hi', 'b': 1}) == A(a='hi', b=1, lst=[])
