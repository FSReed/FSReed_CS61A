def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess


def golden_update(n):
    return 1 / n + 1


def golden_close(guess):
    return is_eq(guess * guess, guess + 1)


def is_eq(x, y, tolerance=1e-10):
    return abs(x - y) < tolerance


def golden_ratio():
    return improve(golden_update, golden_close)
