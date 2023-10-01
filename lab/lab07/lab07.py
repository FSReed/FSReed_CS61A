def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    i = 1
    while True:
        yield i
        i += 1


def scale(it, multiplier):
    """Yield elements of the iterable it scaled by a number multiplier.

    >>> m = scale([1, 5, 2], 5)
    >>> type(m)
    <class 'generator'>
    >>> list(m)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    "*** YOUR CODE HERE ***"

    # def new_generator(it, mult):
    #     iterator = iter(it)
    #     while 1:
    #         result = next(iterator)
    #         if result != None:
    #             result = mult * result
    #             yield result
    #
    # yield from new_generator(it, multiplier)
    "Upper solution will cause StopIteration Error."
    "But this problem can be solved within 1 line."
    yield from map(lambda x: x * multiplier, it)


def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        yield 1
    elif n % 2 == 1:
        yield n
        yield from hailstone(3 * n + 1)
    elif n % 2 == 0:
        yield n
        yield from hailstone(n // 2)
