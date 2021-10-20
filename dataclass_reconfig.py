from dataclasses import dataclass, InitVar


@dataclass(frozen=True)
class A:
    a: str = ''
    b: int = 0
    config: InitVar[dict] = None

    def __post_init__(self, config: dict):
        if config:
            self.__init__(**config)
