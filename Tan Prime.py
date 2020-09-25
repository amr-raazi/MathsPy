from sympy import tan
from sympy.ntheory import isprime

limit = 1169809367327212570704813632106852886389036911 + 1
while True:
    strnum = str(limit)
    tannum = tan(limit)
    if limit % 100000 == 0:
        print(strnum + " has been checked")
        limit += 1
    elif limit % 2 == 0 or limit % 3 == 0 or limit % 5 == 0 or limit % 7 == 0 or limit % 11 == 0 or limit % 13 == 0 or limit % 17 == 0 or limit % 23 == 0 or limit % 29 == 0 or limit % 31 == 0 or limit % 37 == 0 or limit % 41 == 0 or limit % 43 == 0 or limit % 47 == 0 or limit % 53 == 0 or limit % 59 == 0 or limit % 61 == 0 or limit % 67 == 0 or limit % 71 == 0 or limit % 73 == 0 or limit % 79 == 0 or limit % 83 == 0 or limit % 89 == 0 or limit % 97 == 0:
        limit += 1
    elif isprime(limit) and tannum > limit:
        print(f"{limit} + is prime and it's tan is greater than it.")
        break
    else:
        limit += 1
