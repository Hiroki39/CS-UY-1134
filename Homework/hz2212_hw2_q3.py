import math


def factors(num):
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            yield i
    for i in range(int(math.sqrt(num)) - 1, 0, -1):
        if num % i == 0:
            yield num // i
