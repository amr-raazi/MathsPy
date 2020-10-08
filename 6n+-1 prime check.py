from sieve import sieve

x = 10**7
sieve = sieve(x)

for i in range(x):
    if sieve.get(i):
        if i % 6 != 1 and i % 6 != 5:
            print(i)