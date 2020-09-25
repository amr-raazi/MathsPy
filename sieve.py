import math

limit = 100
numbers = list(range(2, limit))
max_root = math.ceil(math.sqrt(limit))
divisor = 1
while divisor < max_root:
    divisor += 1
    if divisor not in numbers:
        continue
    for number in numbers[numbers.index(divisor):]:
        if not number % divisor:
            numbers.remove(number)
print(numbers)
