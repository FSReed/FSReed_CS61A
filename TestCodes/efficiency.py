# Video Link:
# https://www.youtube.com/watch?v=IB8VSP9EZQs&list=PL6BsET-8jgYXfOhsm5yEaOlblrdUVWyiY&index=3


def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)


def count(function):
    def counted(n):
        counted.call_count += 1
        return function(n)

    counted.call_count = 0
    return counted


def memo(function):
    def memoized(n):
        if n not in memoized.cache:
            memoized.cache[n] = function(n)
        return memoized.cache[n]

    memoized.cache = {}
    return memoized


fib = count(fib)
counted_fib = fib
fib = memo(fib)
fib = count(fib)
fib(30)
print(fib.call_count)
print(counted_fib.call_count)
