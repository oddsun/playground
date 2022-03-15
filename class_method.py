import functools
import inspect


class A:
    def __init__(self, y):
        self.y = y

    def sum(self, a: int, b: int):
        return (a + b) * self.y

    def x(self):
        f = functools.partial(A.sum, self)
        print(f(1, 2))
        print(inspect.getfullargspec(f).args)


print(A(3).sum(1, 2), A.sum(A(3), 1, 2))
A(3).x()
