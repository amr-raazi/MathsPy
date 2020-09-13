import random
from utilities import is_prime

count = 0
lower_limit = 0
upper_limit = 100
numbers_needed = int(input("How many random primes do you need?"))
primes = []

for number in range(lower_limit, upper_limit):
    if is_prime(number):
        primes.append(number)
if len(primes) < numbers_needed:
    print(f"Upper and Lower limits are too low to produce {numbers_needed} random primes")
else:
    while count < numbers_needed:
        selection = random.choice(primes)
        primes.remove(selection)
        print(f"{selection} is your random prime")
        count += 1
