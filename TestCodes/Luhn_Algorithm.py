"""The example of mutual recursive functions
What the luhn_sum function does:
    From the rightmost digit, which is the check digit, moving left,
    double the value of every second digit; if product of this doubling
    operation is greater than 9 (e.g., 7*2=14), then sum the digits of it.
    
    EXAMPLE:138743 → 23(16)783 → 237783 → 30
"""


def split(n):
    return n // 10, n % 10


def sum_digits(n):
    all_but_last, last_digit = split(n)
    if n < 10:
        return n
    else:
        return sum_digits(all_but_last) + last_digit


def luhn_sum(n):
    all_but_last, last_digit = split(n)
    if n < 10:
        return n
    else:
        return luhn_sum_double(all_but_last) + last_digit


def luhn_sum_double(n):
    all_but_last, last_digit = split(n)
    luhn_digit = sum_digits(2 * last_digit)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit
