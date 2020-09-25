import math


def sieve(limit):
    numbers = {i: True for i in range(2, limit + 1)}
    max_root = math.ceil(math.sqrt(limit + 1))
    i = 0
    keys = list(numbers.keys())
    divisor = 0
    while divisor < max_root:
        divisor = keys[i]
        i += 1
        if not numbers[divisor]:
            continue
        for number in keys[i:]:
            if not number % divisor:
                numbers[number] = False
    return numbers
