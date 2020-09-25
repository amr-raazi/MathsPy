import math


def sieve(limit):
    numbers = list(range(2, limit))
    max_root = math.ceil(math.sqrt(limit))
    i = 0
    divisor = numbers[i]
    while divisor < max_root:
        divisor = numbers[i]
        for number in numbers[numbers.index(divisor) + 1:]:
            if not number % divisor:
                numbers.remove(number)
        i += 1
    return numbers


