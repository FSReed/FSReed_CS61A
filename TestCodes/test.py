def make_adder(n):
    """This function returns a function that can add n to its argument
    >>> make_adder(3)(2)
    5
        >>> make_adder(4)(12)
    16
    """

    def adder(k):
        return n + k

    return adder
