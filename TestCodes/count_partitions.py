def counting_partitions(n, m):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 1:
        return 1
    else:
        return counting_partitions(n - m, m) + counting_partitions(n, m - 1)


result = counting_partitions(6, 4)
print(result)
