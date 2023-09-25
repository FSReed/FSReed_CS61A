def lambda_returns():
    f = lambda z: print(z)
    a = f(2)
    print(a)
    return


# Tested on 2023-09-06


def recursion_test():
    def sum_digits(n):
        assert n >= 0, "Should put in a positive integer."
        if n < 10:
            return n
        else:
            new_n = n // 10
            digit = n % 10
            return sum_digits(new_n) + digit

    result = sum_digits(1877)
    print(result)
    return


# Tested on 2023-09-08


def Sequence_Unpacking():
    pairs = [[1, 2], [2, 2], [3, 2], [4, 4]]
    count_same = 0
    for x, y in pairs:
        if x == y:
            count_same += 1
    print(count_same)
    return


def divisor(n):
    return [x for x in range(1, n) if n % x == 0]


def reverse_string(s):
    if len(s) == 1:
        return s
    else:
        return reverse_string(s[1:]) + s[0]


# Tested on 2023-09-13


def dictionary_test():
    # Dictionaries are unordered collections of key-values.
    # Two keys cannot be equal.
    # Keys cannot be lists or dictionaries.
    dic = {"I": 1, "V": 5, "X": 10}
    print(dic["X"])
    keys = dic.keys()
    values = dic.values()
    items = dic.items()
    print(keys, "\n", values, "\n", items)
    print("X" in dic)
    square_dic = {x: x * x for x in range(1, 10)}
    print(square_dic)
    list_dic = {1: [2, 3]}
    print(list_dic)
    error_dic = {[1]: 3}  # List cannot be keys
    print(error_dic)


# Tested on 2023-09-16
def sequence_aggregation():
    # See the documentation of some built-in functions!
    print(sum([2, 3, 4]))
    print(sum([2, 3, 4], 5))
    print(sum([[2, 3], [4]], []))
    # NOTE:print(sum([[2, 3], [4]]))  will cause Error!
    #
    try_max = max(range(10), key=lambda x: 12 - (x - 4) * (x - 1))
    print(try_max)
    #
    try_all = all(x < 5 for x in range(5))
    print(try_all)
    try_all = all(x > 0 for x in range(5))
    print(try_all)
    return


# Tested on 2023-09-18


def default_mutable_argument():
    def length(s=[]):
        s.append(3)
        return len(s)

    length()
    length()
    print(length())


def list_example():
    """NOTE:
    All complicated examples can be viewed here:
    https://www.youtube.com/watch?v=tpfpNR3u4zk&list=PL6BsET-8jgYVDEchBIdQeqrUhlN2MZE6F&index=7
    """

    def reset():
        s = [2, 3]
        t = [5, 6]
        return s, t

    def eprint(s, t):
        print(s, "\n", t, "\n")

    #
    print("First try:")
    s, t = reset()
    s.append(t)
    t = 0
    eprint(s, t)
    s, t = reset()
    s.append(t)
    t[1] = 9
    eprint(s, t)

    #
    print("Second try:")
    s, t = reset()
    s.extend(t)
    t[1] = 0
    eprint(s, t)

    # b is a slice of a. And we can see the change in a doesn't affect b.
    # But the change in t will affect both a and b.
    print("Third try:")
    s, t = reset()
    a = s + [t]
    b = a[1:]
    a[1] = 9
    b[1][1] = 0
    eprint(a, b)
    t[0] = 99
    eprint(a, b)

    #
    print(" Fourth try:")
    s, t = reset()
    t = list(s)
    s[1] = 4
    eprint(s, t)
    #
    print("Fifth try:")
    s, t = reset()
    s[0:0] = t
    s[3:] = t
    t[1] = 9
    eprint(s, t)
    s[0:0] = [t]
    t[1] = 8
    eprint(s, t)


# Tested on 2023-09-24
def nonlocal_test():
    def make_accout(balance):
        def withdraw(amount):
            nonlocal balance
            if amount > balance:
                return "Insufficient money."
            else:
                balance = balance - amount
                return balance

        return withdraw

    withdraw = make_accout(100)
    print(withdraw(10))
    print(withdraw(10))
    print(withdraw(60))
    print(withdraw(40))
    print(withdraw(10))


# Tested on 2023-09-25
#
#
#
#

# Testcode area down here:
# ------------Gonna test on:----------------------
nonlocal_test()
# -------------------------------------------------
