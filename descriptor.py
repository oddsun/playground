from dataclasses import dataclass


@dataclass
class String:
    value: str = ''


class Ref:
    def __init__(self):
        self._value = String()

    def __get__(self, obj, objtype=None):
        return self._value

    def __set__(self, obj, value):
        self._value.value = value


@dataclass
class A:
    a: String
