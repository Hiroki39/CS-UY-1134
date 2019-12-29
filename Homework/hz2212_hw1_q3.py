def sqrsum(n):
    sum = 0
    for i in range(n):
        sum += i * i
    return sum


sum([i * i for i in range(10)])


def sqrsumodd(n):
    sum = 0
    for i in range(1, n, 2):
        sum += i * i
    return sum


sum([i * i for i in range(1, 10, 2)])
