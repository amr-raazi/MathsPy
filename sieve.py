import math


def sieve(limit):
    numbers = {i: True for i in range(2, limit)}
    max_root = math.ceil(math.sqrt(limit))
    i = 0
    keys = list(numbers.keys())
    divisor = keys[i]
    while divisor < max_root:
        divisor = keys[i]
        for number in keys[i + 1:]:
            if not number % divisor:
                numbers[number] = False
        i += 1
    return numbers
