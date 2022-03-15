from logging_decorator import log


@log('recursion')
def fibonacci(a):
    if a == 1:
        return a
    return a * fibonacci(a - 1)


fibonacci(10)
