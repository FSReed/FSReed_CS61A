def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# Question 1.1:
def multiple(m, n):
    """Write a function that takes two numbers m and n and returns their product"""
    if m == 1:
        return n
    elif n == 1:
        return m
    else:
        return multiple(m - 1, n) + n


# Question 1.2:
def rec(x, y):
    if y == 0:
        return 1
    else:
        return x * rec(x, y - 1)


# Question 1.3:
def hailstone(n):
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 1:
        return hailstone(3 * n + 1) + 1
    elif n % 2 == 0:
        return hailstone(n // 2) + 1


# Question 1.4:
def merge(n1, n2):
    """
    Write a procedure merge(n1, n2) which takes numbers with digits in de-
    creasing order and returns a single number with all of the digits of the two,
    in decreasing order. Any number merged with 0 will be that number (treat
    0 as having no digits). Use recursion.

    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31)
    3211
    """
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    else:
        digit1, digit2 = n1 % 10, n2 % 10
        if digit1 < digit2:
            n1 = n1 // 10
            return digit1 + 10 * merge(n1, n2)
        else:
            n2 = n2 // 10
            return digit2 + 10 * merge(n1, n2)


# Question 1.5(Optional):
"""
NOTE:
Define a function make fn repeater which takes in a one-argument function
f and an integer x. It should return another function which takes in one
argument, another integer. This function returns the result of applying f to
x this number of times.
Make sure to use recursion in your solution.
"""


def make_func_repeater(f, x):
    """
    >>> incr_1 = make_func_repeater(lambda x: x + 1, 1)
    >>> incr_1(2) #same as f(f(x))
    3
    >>> incr_1(5)
    6
    """

    def repeat(n):
        if n == 1:
            return f(x)
        else:
            return f(repeat(n - 1))

    return repeat


# Question 1.6:
"""
Implement the recursive is prime function. Do not use a while loop, use
recursion. As a reminder, an integer is considered prime if it has exactly two
unique factors: 1 and itself.
"""


def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        return prime_helper(n, 2)


def prime_helper(n, i):
    if n % i == 0:
        return False
    elif i > n / 2:
        return True
    else:
        return prime_helper(n, i + 1)
