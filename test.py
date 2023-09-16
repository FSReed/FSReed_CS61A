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

#
#
#
#
#

# Testcode area down here:
# ------------My test code:----------------------
dictionary_test()
# -------------------------------------------------
