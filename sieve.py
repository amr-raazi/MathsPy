import math

limit = 100
numbers = {}
for i in range(2, limit):
    numbers[i] = True
max_root = math.ceil(math.sqrt(limit))
for i in range(max_root):
    keys = list(numbers.keys())
    prime = keys[i]
    index = keys[i]
    for number in list(numbers.keys())[index:]:
        if not number % prime:
            numbers[number] = False
primes = []
for element in numbers:
    if numbers[element]:
        primes.append(element)
print(primes)
