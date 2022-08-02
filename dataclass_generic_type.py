import dataclasses
from typing import Generic, TypeVar

import dataclasses_json

T = TypeVar("T")


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class ClassA(Generic[T]):
    data: T


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class ClassB:
    name: str


@dataclasses_json.dataclass_json
@dataclasses.dataclass
class ClassC(ClassA[ClassB]):
    pass


print(ClassA(data=ClassB(name="name")).to_json())
print(ClassC.from_json(ClassC(data=ClassB(name="name")).to_json()))
