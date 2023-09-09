def repeat(k):
    """
    When called repeatedly,print each repeated argument.
    >>> repeat(1)(7)(7)(3)(4)(2)(5)(1)(6)(5)(1)
    7
    1
    5
    1
    """
    return detector(lambda j: False)(k)


def detector(have_seen_it_before):
    def g(i):
        if have_seen_it_before(i):
            print(i)
        return detector(lambda j: j == i or have_seen_it_before(j))

    return g


repeat(1)(7)(7)(3)(4)(2)(5)(1)(6)(5)(1)
