"""
Before any code is represented, one thing that needs to be 
clarified is that Data_Abstraction is a methodology that is suggested
to be used when coding.You can find how annoying it is if someone 
crosses the abstraction barrier. Here's the video link :
https://www.youtube.com/watch?v=7zu30DhJLKU&list=PL6BsET-8jgYUYq2VR6hWSGLw2RvCWwPiD&index=4
Can start from 05:40 of this video.

"""

from fractions import gcd


def mul_rational(x, y):
    """
    >>> mul_rational([5, 4], [3, 25])
    [3, 20]
    """
    return rational(numer(x) * numer(y), denom(x) * denom(y))


def div_rational(x, y):
    return rational(numer(x) * denom(y), denom(x) * numer(y))


def add_rational(x, y):
    """
    >>> add_rational([1, 4], [5, 7])
    [27, 28]
    """
    nx, ny = numer(x), numer(y)
    dx, dy = denom(x), denom(y)
    return rational(nx * dy + ny * dx, dx * dy)


def equal_rational(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)


def print_rational(x):
    print(str(numer(x)) + "/" + str(denom(x)))


def numer(x):
    return x[0]


def denom(x):
    return x[1]


def rational(x, y):
    max_divisor = gcd(x, y)
    return [x // max_divisor, y // max_divisor]
